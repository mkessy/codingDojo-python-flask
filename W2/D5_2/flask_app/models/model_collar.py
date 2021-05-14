from flask_app.config.mysqlconnection import connectToMySQL

db = "dogs_db"

class Collar:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, info):
        query = "INSERT INTO collars (name, color, material, dog_id) VALUES (%(name)s, %(color)s, %(material)s, %(dog_id)s)"
        data = {
            "name": info['name'],
            "color": info['color'],
            "material": info['material'],
            "dog_id": info['dog_id'],
        }
        created_collar_id = connectToMySQL(db).query_db(query, data)

        query = "SELECT * FROM collars WHERE id = %(collar_id)s"
        data = {
            "collar_id": created_collar_id
        }
        created_collar = connectToMySQL(db).query_db(query, data)[0]

        return created_collar
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM collars;'
        all_users = connectToMySQL(db).query_db(query)
        return all_users

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM collars WHERE id = %(users_id)s;'
        data = {
            "users_id": id
        }
        one_user = connectToMySQL(db).query_db(query, data)[0]
        return one_user

    @classmethod
    def join_dogs(cls):
        query = "SELECT * FROM collars JOIN dogs ON dogs.id = collars.dog_id;"
        joined_tables = connectToMySQL(db).query_db(query)
        return joined_tables
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass