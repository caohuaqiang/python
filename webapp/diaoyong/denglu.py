import requests
from pprint import pprint


class DL():
    def __init__(self):
        self.yuming = 'https://www-t.jfcaifu.com'

    def wap_dl(self, phone: str, pwd: str='a1234567') -> 'response':
        url = '/wap/user/doLogin.html'
        data = {'mobilePhone': phone,
                'pwd': pwd}
        session = requests.session()
        response = session.request(method='post', url=self.yuming+url, params=data)
        return response
