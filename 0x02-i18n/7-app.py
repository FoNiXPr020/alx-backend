#!/usr/bin/env python3
""" 0x02-i18n/7-app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config(object):
    """ Config class """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.timezoneselector
def get_timezone() -> str:
    """ get timezone """
    try:
        if request.args.get("timezone"):
            return pytz.timezone(request.args.get("timezone")).zone
        if g.user and g.user.get("timezone"):
            return pytz.timezone(g.user["timezone"]).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return "UTC"


def get_user() -> dict:
    """ get user by ID. """
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """ request before each request. """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """ Returns based on the user's preferred language. """
    if request.args.get("locale") in app.config["LANGUAGES"]:
        return request.args.get("locale")
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """ Index page """
    from datetime import datetime
    from flask_babel import format_datetime

    current_time = format_datetime(datetime.utcnow())
    return render_template("7-index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
