import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

app = Flask(__name__)
app.config.from_object(app_config["development"])
db = SQLAlchemy(app)

from flights.views.flights import *  # noqa
from flights.views.user import *  # noqa

app.config['JWT_SECRET_KEY'] = 'supersecretishere'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

