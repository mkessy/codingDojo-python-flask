from flask_app.config.mysqlconnection import connectToMySQL

class Product:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, data):
        pass
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        all_users = connectToMySQL('db_name').query_db(query)
        return all_users

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id = %(users_id)s;'
        data = {
            "users_id": id
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