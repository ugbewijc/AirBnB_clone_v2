#!/usr/bin/python3
"""
Starts Flask web applications on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display "HBNB"
    /c/<text>: display "c" followed by the value of the text variable
    /python/(<text>): display "Python" followed by the value of text variable
                     default value of text = cool
    /number/<n>: display "n is a number" only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
    /number_odd_or_even/<n>: display a HTML page only if n is an integer
    /states_list: display HTML page with list of all State objects in DBStorage
    /cities_by_states: display HTML page with list of all states and related
                      cities
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display: Hello HBNB
    """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Display: HBNB
    """
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_path(text):
    """
    Replace underscore _ symbol with a space
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_path(text="is cool"):
    """
    Replace underscore _ symbol with a space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_path(n):
    """
    Display "n is a number
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display a HTML page only if n is an integer
    """
    if isinstance(n, int):
        return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display a HTML page only if n is an integer
    """
    return render_template("6-number_odd_or_even.html", num=n)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays HTML page with a list of all State objects in DBStorage.
    Sort States by name.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Displays HTML page with  list of all states and related cities.
    Sort States/Cities by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


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
