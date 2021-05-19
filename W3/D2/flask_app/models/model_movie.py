from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session

db = 'movies_and_reviews_db'

class Movie:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.rating = data['rating']
        self.synopsis = data['synopsis']
        self.year_released = data['year_released']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def display_title(self):
        display_name = f"{self.title} - {self.year_released}"
        return display_name

# C
    @classmethod
    def new(cls, info):
        query = 'INSERT INTO movies (title, year_released, rating, synopsis, user_id) VALUES (%(title)s,%(year_released)s,%(rating)s,%(synopsis)s, %(user_id)s)'
        data = {
            "title": info['title'],
            "year_released": info['year_released'],
            "rating": info['rating'],
            "synopsis": info['synopsis'],
            "user_id": session['uuid']
        }
        new_movie_id = connectToMySQL(db).query_db(query, data)
        return new_movie_id

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM movies'

        movies = connectToMySQL(db).query_db(query)

        all_movies = []
        for movie in movies:
            all_movies.append(cls(movie))

        return all_movies

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM movies WHERE id = %(id)s'
        data = {
            "id": id
        }
        return connectToMySQL(db).query_db(query, data)[0]
# U
    @classmethod
    def update_one(cls, id, info):
        query = 'UPDATE movies SET title=%(title)s, year_released=%(year_released)s, rating=%(rating)s, synopsis=%(synopsis)s'
        data = {
            "title": info['title'],
            "year_released": info['year_released'],
            "rating": info['rating'],
            "synopsis": info['synopsis'].strip(" "),
        }
        return connectToMySQL(db).query_db(query, data)

# D
    @classmethod
    def delete_one(cls, id):
        query = 'DELETE FROM movies WHERE id = %(id)s'
        data = {
            "id": id
        }
        return connectToMySQL(db).query_db(query, data)

# Movie Validation
    @staticmethod
    def validate_movie(form_info):
        is_valid = True
        
        if len(form_info['title']) == 0:
            is_valid = False
            flash("must have a title")

        rating = int(form_info['rating'])
        if len(form_info['rating']) == 0 or type(rating) != int:
            is_valid = False
            flash("must have a rating")

        if len(form_info['synopsis']) == 0:
            is_valid = False
            flash("must have a synopsis")

        return is_valid