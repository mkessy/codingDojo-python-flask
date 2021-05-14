from flask_app import app
from flask import render_template, redirect, request, session
# from flask_app.models.model_user import Product

@app.route('/product/create')
def create_product():

   return render_template('index.html')