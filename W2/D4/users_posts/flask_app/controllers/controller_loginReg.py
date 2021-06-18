from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User

@app.route('/login')
def login():
    if 'uuid' in session:
        return redirect('/')
    return render_template('login.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    # get the user by username
    list_of_users = User.get_one_by_username(request.form['username'])

    if len(list_of_users) <= 0:
        # create a message saying no user found
        return redirect('/login')

    user = list_of_users[0]
    if user['pw'] == request.form['pw']:
        session['uuid'] = user['id']
        return redirect('/')
    # check the pw with the db pw
    return render_template('login.html')

@app.route('/register')
def register():
    if 'uuid' in session:
        return redirect('/')
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')