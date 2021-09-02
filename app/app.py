import datetime
from flask import Flask, render_template, Blueprint, session

from flask_babel import Babel

from database.db import Database


app = Flask(__name__)
app.config.from_object('app.config')
app.secret_key = app.config['SECRET']
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.jinja_environment.auto_reload = True

babel = Babel(app)

@app.before_first_request
def init_app():
    pass
    #Database.initilize()


@app.context_processor
def inject_now():
    return {'now': datetime.datetime.utcnow()}


@app.route('/')
def home():
    return render_template('coming_soon.html')