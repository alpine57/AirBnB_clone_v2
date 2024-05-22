#!/usr/bin/pyhon3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    cities = storage.all(City).values()
    sorted_cities = sorted(cities, key=lambda city: city.name)

    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)

    return render_template('10-hbnb_filters.html',
                           states=sorted_states,
                           cities=sorted_cities,
                           amenities=sorted_amenities)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

