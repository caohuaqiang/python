# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, session, copy_current_request_context
from vsearch import search4letters
from threading import Thread
from time import sleep

from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in


app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': '123456',
                          'database': 'vsearchlogDB',}

app.secret_key = 'caohuaqianghenniubi'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


# def log_request(req: 'request', res: str) -> None:
#     """将web请求的数据和返回结果写日志(db)"""
#     # dbconfig = {'host': '127.0.0.1',
#     #             'user': 'vsearch',
#     #             'password': '123456',
#     #             'database': 'vsearchlogDB',}
#     # conn = mysql.connector.connect(**dbconfig)
#     # cursor = conn.cursor()
#     # _SQL = """insert into log
#     #           (phrase, letters, ip, browser_string, results)
#     #           values
#     #           (%s, %s, %s, %s, %s)"""
#     # cursor.execute(_SQL, params=(req.form['phrase'],
#     #                              req.form['letters'],
#     #                              req.remote_addr,
#     #                              req.user_agent.browser,
#     #                              res,))
#     # conn.commit()
#     # cursor.close()
#     # conn.close()
#     sleep(15)
#     with UseDatabase(config=app.config['dbconfig']) as cursor:
#         _SQL = """insert into log
#               (phrase, letters, ip, browser_string, results)
#               values
#               (%s, %s, %s, %s, %s)"""
#         cursor.execute(_SQL, params=(req.form['phrase'],
#                                      req.form['letters'],
#                                      req.remote_addr,
#                                      req.user_agent.browser,
#                                      res,))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'request', res: str) -> None:
        sleep(15)
        with UseDatabase(config=app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, params=(req.form['phrase'],
                                         req.form['letters'],
                                         req.remote_addr,
                                         req.user_agent.browser,
                                         res,))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))             # 写日志（db）
        t.start()
    except Exception as err:
        print('*******Logginf failed with this error:', str(err))

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """读db日志数据(返回html，内含表格)"""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()        # 返回一个元组列表
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')  # 创建描述性标题的元组
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,)
    except ConnectionError as err:
        print('Is your database switched on?Error: ', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is your query correct? Error: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))
    return 'Error'


if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run()
    app.run(debug=True)
