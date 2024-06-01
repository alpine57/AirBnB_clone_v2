#!/usr/bin/python3
"""scriptthat starts a web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    state = storage.all(State).get('State.' + id)
    if state:
        cities = state.cities if hasattr(state, 'cities') else state.get_cities()
        sorted_cities = sorted(cities, key=lambda city: city.name)
        return render_template('state_cities.html', state=state, cities=sorted_cities)
    else:
        return render_template('state_not_found.html')

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

