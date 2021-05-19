from flask_app.config.mysqlconnection import connectToMySQL

db = 'movies_and_reviews_db'

class Review:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, info):
        pass
# R
    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_one(cls, id):
        pass
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass