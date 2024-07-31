#!/usr/bin/env python3
"""
Flask app
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel


class Config(object):
    """
    Configuration for Babel
    """
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


def get_user():
    """_summary_

    Returns:
        _type_: _description_
    """

    id = request.args.get('login_as')
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    This function is executed before each request is processed.
    It retrieves the user and assigns it to the global variable g.user.
    """
    user = get_user()
    g.user = user


def get_locale():
    """
    Select and return best language match based on supported languages
    """
    loc_url = request.args.get('locale')
    user_settings_locale = g.user.get('locale')
    loc_header = request.headers.get('Accept-Language')

    if loc_url in app.config['LANGUAGES']:
        return loc_url
    if (g.user and user_settings_locale in app.config['LANGUAGES']):
        return user_settings_locale
    if (loc_header and loc_header in app.config['LANGUAGES']):
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return app.config['LANGUAGES'][0]


babel.init_app(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)