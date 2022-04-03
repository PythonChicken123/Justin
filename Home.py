import flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index.html")
def home():
    return flask.render_template("home.html")


if __name__ == '__main__':
    app.run()
