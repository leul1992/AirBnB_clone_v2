#!/usr/bin/python3
"""module starts flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def pri():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def pri2():
    return "HBNB"


@app.route('/c/<text>')
def pri3(text):
    text = text.replace('_', ' ')
    return "C %s" % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
