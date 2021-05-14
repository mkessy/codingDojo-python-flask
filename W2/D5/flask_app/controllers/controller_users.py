from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_users import User
from flask_app.models.model_products import Product
from flask_app.models.model_store import Store

@app.route('/')
def index():
    all_users = User.get_all()
    all_stores = Store.get_all()
    # context = {
    #     all_users: all_users
    # }
    return render_template('index.html', all_users=all_users, all_stores=all_stores)

@app.route('/user/create', methods=['POST'])
def create_user():
    info = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
    }
    User.new(info)
    return redirect('/')