from .utils import get_soup
from .utils import now
from dateutil.parser import parse

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """
    try:
        if '/report/' in url:
            return parse_report(url)
        if '/news/' in url:
            return parse_news(url)
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None

def parse_report(url):

    def parse_title(soup):
        main_title = soup.find('h1', class_='title--huge')
        sub_title = soup.find('p', class_="subtitle")
        if not main_title:
            return ''
        if not sub_title:
            return main_title.text
        title = main_title.text + sub_title.text
        return title

    def parse_date(soup):
        date = soup.find('time', class_='date')
        if not date:
            return None
        return parse(date['datetime'], ignoretz=True)

    def parse_content(soup):
        content = soup.find('div', class_= 'report-body')
        if not content:
            return ''
        return content.text

    def parse_tag(soup):
        tag = soup.find('div', class_= 'tags')
        if not tag:
            return 'no tag'
        return tag.text

    soup = get_soup(url)

    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'tag': parse_tag(soup)
    }

def parse_news(url):

    def parse_title(soup):
        main_title = soup.find('h1', class_='title--huge')
        sub_title = soup.find('p', class_="subtitle")
        if not main_title:
            return 'no title'
        if not sub_title:
            return main_title.text
        title = main_title.text + sub_title.text
        return title

    def parse_date(soup):
        date = soup.find('time', class_='date')
        if not date:
            return None
        return parse(date['datetime'], ignoretz=True)

    def parse_content(soup):
        content = soup.find('div', class_= 'article-body article-body--contained')
        if not content:
            return ''
        return content.text

    def parse_tag(soup):
        tag = soup.find('div', class_= 'tags')
        if not tag:
            return 'no tag'
        return tag.text

    soup = get_soup(url)

    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'content': parse_content(soup),
        'tag': parse_tag(soup)
    }
