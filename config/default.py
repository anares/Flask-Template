import pathlib
import os

STATIC = str(pathlib.Path.joinpath(pathlib.Path(__file__).parent.absolute().parent, 'static/'))
SECRET = os.urandom(24).hex()

SEND_FILE_MAX_AGE_DEFAULT = 0
MAX_COOKIE_SIZE = 8196
DEBUG = True
TESTING = False

SUPPORTED_LANGUAGES = {'bg_BG': 'Bulgarian', 'en_US': 'English', 'ru_RU': 'Russian'}
BABEL_DEFAULT_LOCALE = 'bg_BG'
BABEL_DEFAULT_TIMEZONE = 'UTC+3'
TEMPLATES_AUTO_RELOAD = True
TIMEOUT = 60

USERCOLLECTION = 'users'