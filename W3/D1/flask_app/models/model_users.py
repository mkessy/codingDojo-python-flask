from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

db = 'my_site'

class User:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, info):
        query = "INSERT INTO users (first_name, last_name, email, pw_hash) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(pw_hash)s)"
        data = {
            "first_name" : info['first_name'],
            "last_name" : info['last_name'],
            "email" : info['email'],
            "pw_hash" : info['pw_hash'],
        }

        new_users_id = connectToMySQL(db).query_db(query, data)

        query = "SELECT * FROM users WHERE id = %(new_users_id)s"
        data = {
            "new_users_id": new_users_id
        }
        new_users = connectToMySQL(db).query_db(query, data)
        return new_users
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        all_users = connectToMySQL(db).query_db(query)
        return all_users

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id = %(users_id)s;'
        data = {
            "users_id": id
        }
        one_user = connectToMySQL(db).query_db(query, data)[0]
        return one_user
    
    @classmethod
    def get_one_by_email(cls, email):
        query = 'SELECT * FROM users WHERE email = %(users_email)s;'
        data = {
            "users_email": email
        }
        one_user = connectToMySQL(db).query_db(query, data)
        return one_user
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass

    @staticmethod
    def validate_user(user_data):
        is_valid = True

        if len(user_data['first_name']) < 3: 
            is_valid = False
            flash("first name must be greater than 3 characters")
        if len(user_data['last_name']) < 3: 
            is_valid = False
            flash("last name must be greater than 3 characters")

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if len(user_data['email']) < 3: 
            is_valid = False
            flash("first name must be greater than 3 characters")
        if not EMAIL_REGEX.match(user_data['email']):
            is_valid = False
            flash("invalid email address")

        if len(user_data['pw']) < 3: 
            is_valid = False
            flash("password must be greater than 3 characters")
        if user_data['pw'] != user_data['confirm_pw']:
            is_valid = False
            flash("passwords don't match")
        
        return is_valid