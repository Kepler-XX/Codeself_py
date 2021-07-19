import requests

utl = "https://fanyi.baidu.com/sug"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
kw = input("翻译内容：")
data = {

    "kw": kw
}
resp = requests.request(url=utl, method="POST", data=data)
print(resp.json())
resp.close()