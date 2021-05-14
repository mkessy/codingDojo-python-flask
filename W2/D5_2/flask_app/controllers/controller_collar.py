from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_collar import Collar


@app.route('/collar/create', methods=['POST'])
def create_collar():
    info = {
        "color": request.form['color'],
        "name": request.form['name'],
        "material": request.form['material'],
        "dog_id": request.form['dog_id'],
    }
    new_collar = Collar.new(info)
    print(new_collar)
    return redirect('/')

