from .utils import get_soup
from .utils import now

def parse_page(url):
    if '/report/' in url:
        return parse_report(url)
    if '/news/' in url:
        return parse_news(url)
    return None

def parse_report(url):

    def parse_title(soup):
        main_title = soup.find('h1', class_='title--huge')
        sub_title = soup.find('p', class_="subtitle")
        if not sub_title:
            return main_title.text
        title = main_title.text + sub_title.text
        return title

    def parse_date(soup):
        date = soup.find('time', class_='date')['datetime']
        if not date:
            return ''
        return date

    def parse_content(soup):
        content = soup.find('div', class_= 'report-body').text
        if not content:
            return ''
        return content

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
        if not sub_title:
            return main_title.text
        title = main_title.text + sub_title.text
        return title

    def parse_date(soup):
        date = soup.find('time', class_='date')['datetime']
        if not date:
            return ''
        return date

    def parse_content(soup):
        content = soup.find('div', class_= 'article-body article-body--contained').text
        if not content:
            return ''
        return content

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
