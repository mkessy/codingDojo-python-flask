from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.model_dogs import Dog
from flask_app.models.model_toys import Toy

@app.route('/dog/create', methods=['POST'])
def create_dog():
   info = {
      "name": request.form['name'],
      "type": request.form['type'],
   }
   new_dog = Dog.new(info)
   print(f"new dogs id is: {new_dog}")
   return redirect('/')

@app.route('/dog/<int:dog_id>/show')
def show_dog(dog_id):
   context = {
      "dog" : Dog.join_collars_one_dog(dog_id),
      "dog_toys": Dog.join_dog_toys(dog_id),
      "all_toys" : Toy.get_all(dog_id),
   }
   return render_template('show_dog.html', **context)

@app.route('/dog/<int:dog_id>/toy/new', methods=['POST'])
def add_new_toy(dog_id):
   toy_id = request.form['toy_id']
   Dog.add_toy(dog_id, toy_id)

   return redirect(f'/dog/{dog_id}/show')

@app.route('/dog/<int:dog_id>/<int:toy_id>/delete')
def remove_toy(dog_id, toy_id):
   Dog.remove_toy(dog_id, toy_id)
   return redirect(f'/dog/{dog_id}/show')