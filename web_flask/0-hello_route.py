#!/usr/bin/python3
<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def pri():
    return "Hello HBNB!"
=======
""" script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes: /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route definition """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ hello_hbnb method """
    return ('Hello HBNB!')
>>>>>>> c8a9fcf1ff8526e1c9e554099fe49772e0435321

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
