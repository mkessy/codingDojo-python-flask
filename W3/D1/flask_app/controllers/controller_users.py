from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_users import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/user/create', methods=['POST'])
def create_user():
    is_valid = User.validate_user(request.form)

    if is_valid:
        list_of_users = User.get_one_by_email(request.form['email'])
        if len(list_of_users) > 0:
            flash("email already exists")
            return redirect('/')
        '''
        Working with Bcrypt:
        1. bcrypt.generate_password_hash(password_string)

        2. bcrypt.check_password_hash(hashed_password, password_string)
        '''
        pw_hash = bcrypt.generate_password_hash(request.form['pw'])

        print(pw_hash)

        info = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "pw_hash": pw_hash,
        }
        new_user = User.new(info)
        print(new_user)
        session['uuid'] = new_user[0]['id']
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/user/logout')
def logout_user():
    session.clear()
    return redirect('/')

@app.route('/user/login', methods=['POST'])
def login_user():
    # see if user is in the db
    list_of_users = User.get_one_by_email(request.form['email'])
    if len(list_of_users) == 0:
        print("email not found")
        flash("Invalid credentials")
        return redirect('/')
    else:
        print("email found")
        user = list_of_users[0]
        if bcrypt.check_password_hash(user['pw_hash'], request.form['pw']):
            session['uuid'] = user['id']
            return redirect('/dashboard')
    
