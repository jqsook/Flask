from flask import Flask, app, render_template


app = Flask(__name__)


@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')
