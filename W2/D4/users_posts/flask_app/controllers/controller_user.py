from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User

@app.route('/user/create', methods=['POST'])
def user_create():
    print(request.form)
    user_id = User.create(request.form)
    session['uuid'] = user_id
    return redirect('/')

@app.route('/user/edit')
def user_edit():
    if 'uuid' not in session:
        return redirect('/login')
    context = {
        "user": User.get_one(session['uuid'])
    }
    return render_template('user_edit.html', **context)

@app.route('/user/update', methods=['POST'])
def user_update():
    user =  User.get_one(session['uuid'])
    info = {
        "username": request.form['username'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "pw": user['pw'],
        "id": session['uuid'],
    }
    User.update_one(info)
    return redirect('/')

@app.route('/user/delete')
def user_delete():
    User.delete_one(session['uuid'])
    session.clear()
    return redirect('/')




'''
RESTFULL
1. /table_type/new -> display for creating a new table obj
2. /table_type/create -> action route that will process the creations of that table row
3. /table_type/<id> -> get the row 
4. /table_type/all
5. /table_type/<id>/edit -> display route showing the form to update
6. /table_type/<id>/update -> action route that processes the form
7. /table_type/delete
'''