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
"""


from flask import Flask
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


if __name__ == "__main__":
    """
    Starts app on 0.0.0.0:5000
    """
    app.run(host="0.0.0.0", port=5000)
