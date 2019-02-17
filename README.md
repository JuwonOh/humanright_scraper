# humanright_scraper

미국의 씽크탱크인 Human Right Watch의 자료들(Blog, report)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py download.py로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.
downdload는 parser에서 parsing된 각 보고서를 다운로드 해줍니다.

```
전체 카테고리의 자료를 일정한 조건으로 크롤링하기 위해서는 python scraping_latest_news.py를 사용하세요.
```
특정한 페이지를 parse하기 위해서는 usage.ipynb의 다음 함수들을 참고하세요.
```
[1 / 10] (2019-02-04) “What Hell Feels Like”Acid Violence in Cambodia
[2 / 10] (2019-01-31) Dashed HopesThe Criminalization of Peaceful Expression in Myanmar
[3 / 10] (2019-01-23) “No Room to Bargain”Unfair and Abusive Labor Practices in Pakistan
[4 / 10] (2019-01-21) No Escape from HellEU Policies Contribute to Abuse of Migrants in Libya
[5 / 10] (2019-01-09) Unmet NeedsImproper Social Care Assessments for Older People in England
Stop scrapping. 5 / 10 report was scrapped
The oldest blog article has been created after 2019-01-01
```

```
from Humanright_scraper import yield_latest_report

begin_date = '2019-01-01'
max_num = 10
sleep = 1.0

for i, json_obj in enumerate(yield_latest_report(begin_date, max_num, sleep)):
    title = json_obj['title']
    time = json_obj['date']
    print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))
```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
