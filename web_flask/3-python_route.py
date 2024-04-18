#!/usr/bin/python3
"""Create Flask App"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def listen_c(text):
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python/", defaults={'text': "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def listen_python(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
