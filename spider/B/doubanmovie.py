from pprint import pprint

import requests
import re

from spider.B.db import insert_mon


li = list()
for i in range(0, 10):
    url = "https://movie.douban.com/top250?start=%d&filter=" % i*25
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    douban = requests.request(method='GET', url=url, headers=headers)

    douban = douban.content.decode('utf-8')
    a = '(?P<country>.&?)&nbsp;/&nbsp;(?P<type>.*?).*?'

    p = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                   r'<p class="">(?P<director>.*?)&nbsp;&nbsp;&nbsp;(?P<star>.*?)<br>'
                   r'(?P<year>.*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;(?P<type>.*?)</p>'
                   r'.*?<div class="star">.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                   r'.*?<span>(?P<number>.*?)</span>', re.S)
    l = p.finditer(douban)

    for i in l:
        data = dict()
        pprint(f'电影:{i.group("name")}')
        pprint(i.group("director").strip())
        pprint(i.group('star'))
        pprint(f'年份：{i.group("year").strip()}')
        pprint(f'国家:{i.group("country")}')
        pprint(f'类型:{i.group("type")}'.strip())
        pprint(f'评分:{i.group("score")}')
        pprint(f'评价数:{i.group("number")}')
        print("********")

        data['name'] = i.group("name")
        data['director'] = i.group("director").strip()
        data['star'] = i.group("star")
        data['year'] = i.group("year").strip()
        data['country'] = i.group("country")
        data['type'] = i.group("type").strip()
        data['score'] = i.group("score")
        data['number'] = i.group("number")
        li.append(data)
if __name__ == '__main__':
    insert_mon(li)