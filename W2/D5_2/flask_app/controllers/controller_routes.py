from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_dogs import Dog
from flask_app.models.model_collar import Collar
from flask_app.models.model_toys import Toy

@app.route('/')
def index():
    # TODO: get all dogs from db
    context = {
    "all_collars_with_dogs" : Collar.join_dogs(),
    "all_dogs" : Dog.get_all()
    }
    return render_template('index.html', context=context)

@app.route('/toys/all')
def all_toys():
    all_toys = Toy.get_all()
    return render_template('all_toys.html', all_toys=all_toys)