# coding = utf-8
import requests

urls = ('https://www.baidu.com', 'https://www-t.jfcaifu.com', 'http://caohuaqiang.pythonanywhere.com')

A = [requests.get(url) for url in urls]
# for resp in [requests.get(url) for url in urls]:
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)
