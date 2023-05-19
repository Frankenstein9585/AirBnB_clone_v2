#!/usr/bin/python3
"""Simple Flask Web app"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Print n only if it's an integer"""
    if type(n) == int:
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if type(n) == int:
        if n % 2 == 0:
            num_type = 'even'
        else:
            num_type = 'odd'
        return render_template('6-number_odd_or_even.html', n=n, num_type=num_type)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
