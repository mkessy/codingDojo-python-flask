from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM users WHERE id=%(user_id)s'
        data = {
            "user_id": id
        }
        result = connectToMySQL('mydb').query_db(query, data) # returns a LIST of DICTIONARIES
        return cls(result[0])