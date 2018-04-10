from url_utils import gen_from_urls
from pprint import pprint

urls = ('https://www.baidu.com', 'https://www-t.jfcaifu.com', 'http://caohuaqiang.pythonanywhere.com')

# for a, b, c in gen_from_urls(urls):
#     print(a, b, c)

urls_res = {url: size
            for size, _, url in gen_from_urls(urls)}
pprint(urls_res)
