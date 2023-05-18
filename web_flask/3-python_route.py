#!/usr/bin/python3
"""Simple Flask Web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays some text on the browser"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays some text on the browser"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display C followed by the value of the text variable"""
    text = str.replace(text, '_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False, defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Display C followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
