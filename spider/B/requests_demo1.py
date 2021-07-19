import requests

utl = "http://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
resp = requests.request(url=utl, method='GET', headers=headers)
print(resp.content.decode('utf-8'))
resp.close()