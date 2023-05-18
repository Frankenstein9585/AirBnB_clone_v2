#!/usr/bin/python3
"""Simple Flask Web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Displays some text on the browser"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Displays some text on the browser"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
