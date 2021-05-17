from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_users import User

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('dashboard.html')