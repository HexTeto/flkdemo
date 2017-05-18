#!/usr/bin/env python3

import sys
from flask import Flask
# from flask_request import Resource, Api

app = Flask(__name__)

class Hello(object):
    @route('/')
    def __init__(self):
        self.msg = 'Hello, World!'
    @route('/<username>'):
    def userPage(self, username):
        return 'Welcome back, ' + username


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')