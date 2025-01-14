#!/usr/bin/python3
"""
This simple Flask Web app retrieves states from the db
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(exception):
    """
    This removes the current session after each request
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    This retrieves the states from the database
    """

    states = storage.all(State)
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
