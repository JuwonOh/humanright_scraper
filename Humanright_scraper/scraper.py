import re
import time
import datetime
from dateutil.parser import parse
from .parser import parse_page
from .utils import get_soup

patterns = [
    re.compile('https://www.hrw.org/report/[\w]+'),
    re.compile('https://www.hrw.org/news[\w]+')]

def is_matched(url):
    for pattern in patterns:
        if pattern.match(url):
            return True
    return False

url_report = 'https://www.hrw.org/publications?keyword=&date%5Bvalue%5D%5Byear%5D=&page={}/'

def yield_latest_report(begin_date, max_num=10, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec
    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = parse(begin_date)
    end_page = 120
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all= []
        url = url_report.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h3', class_= 'title')
        links = ['https://www.hrw.org' + i.find('a')['href'] for i in sub_links]
        links_all += links
        links_all = [url for url in links_all if is_matched(url)]

        # scrap
        for url in links_all:
            news_json = parse_page(url)
            try:
                # check date
                d_news = news_json['time']
                if d_begin > d_news:
                    outdate = True
                    print('Stop scrapping. {} / {} blog was scrapped'.format(n_news, max_num))
                    print('The oldest article has been created after {}'.format(begin_date))
                    break

                # yield
                yield news_json
            except Exception as e:
                print(e)
                print('Parsing error from {}'.format(url))
                return None

            # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_report_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status
    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_report.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h3', class_= 'title')
        links = ['https://www.hrw.org' + i.find('a')['href'] for i in sub_links]
        links_all += links
        links_all = [url for url in links_all if is_matched(url)]

    return links_all

url_news = 'https://www.hrw.org/news?keyword=&date%5Bvalue%5D%5Byear%5D=&page={}/'

def yield_latest_news(begin_date, max_num=10, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec
    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = parse(begin_date)
    end_page = 200
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        for page in range(0, end_page+1):
            url = url_news.format(page)
            soup = get_soup(url)
            sub_links = soup.find_all('h3', class_= 'title')
            links = ['https://www.hrw.org' + i.find('a')['href'] for i in sub_links]
            links_all += links
        # scrap
        for url in links_all:
            news_json = parse_page(url)

            if news_json['date'] is not None:
                # check date
                d_news = news_json['date']
                if d_begin > d_news:
                    outdate = True
                    print('Stop scrapping. {} / {} blog was scrapped'.format(n_news, max_num))
                    print('The oldest testimony article has been created after {}'.format(begin_date))
                    break

                # yield
                yield news_json
            else:
                continue

                # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_news_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status
    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_news.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h3', class_= 'title')
        links = ['https://www.hrw.org' + i.find('a')['href'] for i in sub_links]
        links_all += links

    return links_all
