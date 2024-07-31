#!/usr/bin/env python3
""" 0x02-i18n/3-app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Configuration class for the application."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Returns based on the user's preferred language. """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """ Index page """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
