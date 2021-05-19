from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/user/register', methods=['POST'])
def register_user():
    is_valid = User.validate_user(request.form)
    if is_valid:
        # check to makes sure the email is unique
        list_of_users = User.get_one_by_email(request.form['email'])
        print(list_of_users)
        if len(list_of_users) == 0:
            # hash pw
            pw_hash = bcrypt.generate_password_hash(request.form['pw'])
            # create the user
            info = {
                "first_name": request.form['first_name'],
                "last_name": request.form['last_name'],
                "email": request.form['email'],
                "pw_hash": pw_hash,
            }
            new_user_id = User.new(info)
            
            # store id into session
            session['uuid'] = new_user_id

            return redirect('/dashboard')
    return redirect('/register')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')