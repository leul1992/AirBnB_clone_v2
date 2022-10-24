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


@app.route('/c/<text>', strict_slashes=False)
def pri3(text):
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pri4(text=None):
    if text is None:
        text = "is cool"
    else:
        text = text.replace('_', ' ')

    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def pri_num(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def pri_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
