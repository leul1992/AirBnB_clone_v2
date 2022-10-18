#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
"""module starts flask web application"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ hello_hbnb method """
    return ('Hello HBNB!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
