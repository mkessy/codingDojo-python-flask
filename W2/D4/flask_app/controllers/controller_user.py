from flask_app import app
from flask import render_template, redirect, request, session
# from flask_app.config.mysqlconnection import connectToMySQL 
from flask_app.models.model_user import User


# TODO: create a templates folder
@app.route('/')
def index():
    all_users = User.get_all()
    return render_template("index.html", all_users=all_users)

# R
@app.route('/user/<int:id>')
def show(id):
    user = User.get_one(id)
    return render_template('show.html', user=user)

# C
@app.route("/user/create", methods=['POST'])
def create_new_user():
    mysql = connectToMySQL('first_flask')
    query = 'INSERT INTO users (first_name, last_name, occupation) VALUES (%(first_name)s,%(last_name)s,%(occupation)s);'
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "occupation": request.form['occupation'],
    }
    newUser = mysql.query_db(query, data)
    return redirect('/')

# U
# display route
@app.route('/user/<int:id>/edit')
def edit_user(id):
    mysql = connectToMySQL('first_flask')
    query = 'SELECT * FROM users WHERE id = %(id)s;'
    data = {
        "id": id
    }
    user = mysql.query_db(query, data)
    return render_template('edit_user.html', user=user[0])

# action route
@app.route('/user/<int:id>/update', methods=['POST'])
def update_user(id):
    mysql = connectToMySQL('first_flask')
    query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, occupation = %(occupation)s WHERE id = %(id)s;'
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "occupation": request.form['occupation'],
        "id": id,
    }
    user = mysql.query_db(query, data)
    return redirect('/')

# D
@app.route("/user/<int:id>/delete")
def delete_user(id):
    mysql = connectToMySQL('first_flask')
    query = "DELETE FROM users WHERE id = %(id)s"
    data = {
        "id": id
    }
    mysql.query_db(query, data)
    return redirect('/')
