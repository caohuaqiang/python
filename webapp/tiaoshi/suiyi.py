from __future__ import unicode_literals
import requests
import json
from vsearch import search4letters


def chq():
    session = requests.session()
    url = 'https://www-t.jfcaifu.com/wap/user/doLogin.html'
    login_data = {'mobilePhone': '15821903152',
                  'pwd': 'a1234567'}
    response = session.request(method='post', url=url, params=login_data)
    # return json.dumps(response.json(), ensure_ascii=False)
    print(type(response.text))
    print(response.json()['msg'])


if __name__ == '__main__':
    chq()