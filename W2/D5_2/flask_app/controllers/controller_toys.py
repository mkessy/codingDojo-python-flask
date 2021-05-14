from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_toys import Toy

# C
@app.route('/toy/create', methods=['POST'])
def create_toy():
   info = {
      "name": request.form['name']
   }
   Toy.new(info)
   return redirect('/toys/all')

# R
# U
# D