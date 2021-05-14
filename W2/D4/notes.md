# MVC

What is the point of following the MVC framework? 

- Break the files up into smaller chunks. 

1. Models
    - things that interact with the database
    - Handle the logic that deals with db
1. Views
    - templates
    - What the users sees
    - HTML files
1. Controllers
    - takes care of the routes
    - "/users/<id>/edit" -> render_template()

## Main app Folder

1. create new dir "flask_app"
1. file __init__.py
    ```py
    from flask import Flask
    app = Flask(__name__)
    app.secret_key = "shhhhhh"
    ```
1. delete above from the server.py
1. add to server.py file
    ```py
    from flask_app import app
    ```
1. Move static and templates into the flask_app folder

1. create config folder inside flask_app folder and move the mysqlconnection.py into the config

### controllers

1. create a controllers folder with a file named after your model
1. move all the "@app.routes" into the controller
1. add the imports 
    ```py
    from flask_app import app
    from flask import render_template, redirect, request, session
    from flask_app.config.mysqlconnection import connectToMySQL 
    ```
1. remove above from server.py
1. add to server.py 
    ```py
    from flask_app.controllers import controller_user
    ```

### Models

1. create a models folder inside flask_app folder
1. create a file inside models folder
1. create a class inside the above folder. 
    - interact with the db
    - create name based off of table name of db
    - create __init__ with attributes
1. Create class methods that query the db
