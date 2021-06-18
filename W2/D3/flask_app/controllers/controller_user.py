from flask_app import app

from flask import render_template, redirect, request, session
from flask_app.models.model_user import User

@app.route('/')
def index():
    context = {
        "all_users": User.get_all()
    }
    return render_template('index.html', **context)