import re
import requests

url = 'http://liuyan.people.com.cn/forum/list?fid=13'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
people = requests.request(method='GET', url=url, headers=header)
print(people.content.decode('utf-8'))