# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect, escape
import requests
import json
from pprint import pprint
from vsearch import search4letters


app = Flask(__name__)


def log_request(req: 'request', res: str) -> None:
    """写日志"""
    with open('vsearch.log', mode='a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(req=request, res=results)
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
    with open('vsearch.log', mode='r') as log:
        contents = []
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')  #创建描述性标题的元组
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run()
    app.run(debug=True)


    caonima 