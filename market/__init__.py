from enum import unique
from flask import Flask, app, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# see vid at 138 for database creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)  # must pass in the name of the app here.

# To run the server
#       export FLASK_APP=hello.py
#       export FLASK_ENV=development
#       flask run
