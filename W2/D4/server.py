from flask import Flask, render_template, redirect, request, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/return_string')
def hello_world():
    return 'Hello World!'

# TODO: create a templates folder
@app.route('/')
def index():
    mysql = connectToMySQL('first_flask') # call the function, passing in the name of our db
    all_users = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    print(all_users)
    return render_template("index.html", all_users=all_users)
# R
@app.route('/users/<int:id>')
def show(id):
    mysql = connectToMySQL('first_flask')
    query = 'SELECT * FROM users WHERE id = %(users_id)s;'
    data = {
        "users_id": id
    }
    user = mysql.query_db(query, data)
    return render_template('show.html', user=user[0])

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

if __name__=="__main__":
    app.run(debug=True)