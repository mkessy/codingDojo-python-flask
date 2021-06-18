# class User:
#     def __init__(self, data): # data == a dictionary
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.email = data['email']
#         self.password = data['password']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
    
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     @classmethod
#     def get_one():
#         response = [{
#             'id': 1,
#             'first_name': "tyler",
#             'last_name': "Tbo",
#             'email': 'tt@email.com',
#             'password': 'thibault',
#             'created_at': '1900/01/01',
#             'updated_at': '1900/01/01'
#         }]

#     tyler = User()

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DATABASE_SCHEMA = 'mydb'

class class_name:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, info):
        query = "INSERT INTO users (first_name) VALUES (%(first_name)s)"
        data = {
            "first_name" : info['first_name'],
        }

        new_users_id = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

        return new_users_id
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        all_users = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        return all_users

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id = %(first_name_id)s;'
        data = {
            "first_name_id": id
        }
        one_users = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)[0]
        return one_users
    
    # Delete if not a user model
    @classmethod
    def get_one_by_email(cls, email):
        query = 'SELECT * FROM users WHERE email = %(users_email)s;'
        data = {
            "users_email": email
        }
        one_users = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return one_users
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass

    # Delete if not a user model
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