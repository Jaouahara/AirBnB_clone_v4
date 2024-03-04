#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/1-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    my_states = storage.all(State).values()
    my_states = sorted(my_states, key=lambda k: k.name)
    st_ct = []

    for my_state in my_states:
        st_ct.append([my_state, sorted(my_state.cities, key=lambda k: k.name)])

    my_amenities = storage.all(Amenity).values()
    my_amenities = sorted(my_amenities, key=lambda k: k.name)

    my_places = storage.all(Place).values()
    my_places = sorted(my_places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=my_amenities,
                           places=my_places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
