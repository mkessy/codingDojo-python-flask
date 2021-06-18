from werkzeug.utils import redirect
from flask_app import app
from flask import render_template, redirect, session

from flask_app.models.model_user import User

@app.route("/")
def index():
    session['uuid'] = 5 # id of whoever's logged in
    # call the get all classmethod to get all friends
    one_user = User.get_one(session['uuid'])
    print(one_user)
    return render_template("index.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')