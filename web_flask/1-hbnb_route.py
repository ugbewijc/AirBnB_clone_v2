#!/usr/bin/python3
"""
Starts Flask web applications on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display "HBNB"
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    display: Hello HBNB
    """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display: HBNB
    """
    return 'HBNB'


if __name__ == "__main__":
    """
    Starts app on 0.0.0.0:5000
    """
    app.run(host="0.0.0.0", port=5000)
