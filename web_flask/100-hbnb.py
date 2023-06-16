#!/usr/bin/python3
"""
Starts Flask web applications on 0.0.0.0, port 5000.
Routes:
    /hbnb: Displays HBnB Home Page
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    DIsplay HBnB Main Page with neccessary filtes
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """
    Close SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    """
    Starts app on 0.0.0.0:5000
    """
    app.run(host="0.0.0.0", port=5000)
