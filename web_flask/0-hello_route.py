#!/usr/bin/python3
"""Simple Flask Web app"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def display():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)