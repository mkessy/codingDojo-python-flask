from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_store import Store

@app.route('/store/create', methods=['POST'])
def create_store():
    info = {
        "name": request.form['name'],
        "user_id": request.form['user_id']
    }
    Store.new(info)
    return redirect('/')