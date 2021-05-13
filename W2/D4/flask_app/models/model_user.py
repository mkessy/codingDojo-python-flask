from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# C
    @classmethod
    def new(cls, data):
        pass
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        all_users = connectToMySQL('first_flask').query_db(query)
        return all_users

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id = %(users_id)s;'
        data = {
            "users_id": id
        }
        one_user = connectToMySQL('first_flask').query_db(query, data)[0]
        return one_user
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass