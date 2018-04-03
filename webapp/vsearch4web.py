# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
from DBcm import UseDatabase


app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': '123456',
                          'database': 'vsearchlogDB',}


def log_request(req: 'request', res: str) -> None:
    """将web请求的数据和返回结果写日志(db)"""
    # dbconfig = {'host': '127.0.0.1',
    #             'user': 'vsearch',
    #             'password': '123456',
    #             'database': 'vsearchlogDB',}
    # conn = mysql.connector.connect(**dbconfig)
    # cursor = conn.cursor()
    # _SQL = """insert into log
    #           (phrase, letters, ip, browser_string, results)
    #           values
    #           (%s, %s, %s, %s, %s)"""
    # cursor.execute(_SQL, params=(req.form['phrase'],
    #                              req.form['letters'],
    #                              req.remote_addr,
    #                              req.user_agent.browser,
    #                              res,))
    # conn.commit()
    # cursor.close()
    # conn.close()
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


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(req=request, res=results)           # 写日志（db）
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
def view_the_log() -> 'html':
    """读日志(做成表格，返回html)"""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()        # 返回一个元组列表
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')  # 创建描述性标题的元组
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run()
    app.run(debug=True)
