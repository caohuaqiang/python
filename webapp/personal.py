from flask import Flask, render_template, request
from pprint import pprint
import requests
import json
from diaoyong.denglu import DL


app = Flask('__name__')


@app.route('/login')
def login_page() -> 'html':
    """登录页面"""
    return render_template('login.html', biaoti='欢迎访问曹华强专用测试接口登录页面')


@app.route('/login/wap', methods=['POST'])
def wap_login() -> 'html':
    """返回登录json"""
    phone = request.form['name']
    pwd = request.form['pwd']
    response_login = DL().wap_dl(phone=phone, pwd=pwd)
    return render_template('response_login.html',
                           the_title='登录接口返回json',
                           the_phone=phone,
                           the_pwd=pwd,
                           the_results=response_login.text)
# return json.dumps(response.json(), ensure_ascii=False)        #ensure_ascii=False 就不会用 ASCII 编码，中文就可以正常显示了


# @app.route('/login/treasure')
# def treasure() -> 'str':


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(debug=True)
