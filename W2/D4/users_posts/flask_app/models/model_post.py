from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_user import User

DATABASE_SCHEMA = 'users_and_posts_db'

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

# C
    @classmethod
    def create(cls, info):
        query = 'INSERT INTO posts ( title, content, user_id) VALUES (%(title)s, %(content)s, %(user_id)s)'
        data = {
            "title": info['title'],
            "content": info['content'],
            "user_id": info['user_id'],
        }
        new_user_id = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        return new_user_id
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT posts.*, username FROM posts JOIN users ON user_id = users.id;'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query) # returns a list of dictionaries

        # all_posts = [cls(post) for post in results] # A BETTER WAY
        all_posts = []
        for post in results:
            all_posts.append(cls(post))

        return all_posts

    @property
    def user(self):
        return User.get_one(id=self.user_id)

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM posts WHERE id = %(id)s;'
        data ={
            'id': id
        }
        one_user = connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        return one_user[0]
    
# U
    @classmethod
    def update_one(cls, info):
        query = 'UPDATE posts SET title=%(title)s, content=%(content)s WHERE id=%(id)s '
        data = {
            "title": info['title'],
            "content": info['content'],
            "id": info['id'],
        }

        return connectToMySQL(DATABASE_SCHEMA).query_db(query,data)

# D
    @classmethod
    def delete_one(cls, id):
        query = 'DELETE FROM posts WHERE id=%(id)s'
        data = {
            "id": id
        }
        connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        print(f"post with the id {id} has been deleted")
        return id