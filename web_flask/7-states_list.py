#!/usr/bin/python3
"""Simple Flask Web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
