from flask import session


def check_logged_in(func):
    def wapper():
        if 'logged_in' in session:
            return func()
        return 'You are NOT logged in.'
    return wapper
