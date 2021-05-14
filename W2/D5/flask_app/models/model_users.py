from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, info):
        query = 'INSERT INTO users (first_name, last_name) VALUES (%(first_name)s,%(last_name)s);'
        data = {
            "first_name": info['first_name'],
            "last_name": info['last_name'],
        }
        new_user_id = connectToMySQL('store_db').query_db(query, data)
        return new_user_id
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        all_users = connectToMySQL('store_db').query_db(query)
        return all_users

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id = %(users_id)s;'
        data = {
            "user_id": id
        }
        one_user = connectToMySQL('db_name').query_db(query, data)[0]
        return one_user
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass