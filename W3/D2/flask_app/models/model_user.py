from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

db = 'movies_and_reviews_db'

class User:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, info):
        query = 'INSERT INTO users (first_name, last_name, email, pw) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(pw_hash)s)'
        data = {
            "first_name": info['first_name'],
            "last_name": info['last_name'],
            "email": info['email'],
            "pw_hash": info['pw_hash'],
        }
        new_user_id = connectToMySQL(db).query_db(query, data)
        return new_user_id
# R
    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        data = {
            "id": id
        }
        return connectToMySQL(db).query_db(query, data)[0] # give us a list of 1 user

    @classmethod
    def get_one_by_email(cls, email):
        query = 'SELECT * FROM users WHERE email = %(email)s'
        data = {
            "email": email
        }
        user = connectToMySQL(db).query_db(query, data)
        print("*"*80)
        print(user)
        return user
    
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass

# Validate user
    @staticmethod
    def validate_user(form_data):
        is_valid = True
        
        if len(form_data['first_name']) == 0 or type(form_data['first_name']) != str:
            is_valid = False
            flash("first name must be a letters and must be 1 or more characters long.")
        if len(form_data['last_name']) == 0 or type(form_data['last_name']) != str:
            is_valid = False
            flash("last name must be a letters and must be 1 or more characters long.")
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if not EMAIL_REGEX.match(form_data['email']):
            is_valid = False
            flash("Invalid email")

        if form_data['pw'] != form_data['confirm_pw']:
            is_valid = False
            flash("Passwords do not match")

        if len(form_data['pw']) < 8:
            is_valid = False
            flash("Passwords must be 8 characters or longer")

        return is_valid