from enum import unique
from flask import Flask, app, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# see vid at 138 for database creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)  # must pass in the name of the app here.


class Item(db.Model):
    # THis field is required with sqlalchemy
    id = db.Column(db.Integer(), primary_key=True)
    # This sets limits on the information stored in the db
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)

    def __repr__(self):
        # This makes the name that shows up the database custom to the name in the
        return f'Item {self.name}'


@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()

    return render_template('market.html', items=items)


# To run the server
#       export FLASK_APP=hello.py
#       export FLASK_ENV=development
#       flask run
