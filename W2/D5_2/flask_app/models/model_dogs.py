from flask_app.config.mysqlconnection import connectToMySQL

db = "dogs_db"

class Dog:
    def __init__(self, info):
        self.id = info['id']

# C
    @classmethod
    def new(cls, info):
        query = "INSERT INTO dogs (name, type) VALUES (%(name)s, %(type)s)"
        data = {
            "name": info['name'],
            "type": info['type'],
        }
        created_dog_id = connectToMySQL(db).query_db(query, data)

        query = "SELECT * FROM dogs WHERE id = %(dog_id)s"
        data = {
            "dog_id": created_dog_id
        }
        created_dog = connectToMySQL(db).query_db(query, data)[0]

        return created_dog

    @classmethod
    def add_toy(cls, dog_id, toy_id):
        query = "INSERT INTO dogs_has_dog_toys (dogs_id, dog_toys_id) VALUES (%(dog_id)s,%(toy_id)s)"
        data = {
            "dog_id": dog_id,
            "toy_id": toy_id
        }
        new_relationship = connectToMySQL(db).query_db(query, data)
        return new_relationship
    
# R
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dogs;'
        all_dogs = connectToMySQL(db).query_db(query)
        return all_dogs

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM dogs WHERE id = %(dog_id)s;'
        data = {
            "dog_id": id
        }
        one_dog = connectToMySQL(db).query_db(query, data)[0]
        return one_dog

    @classmethod
    def join_collars(cls):
        query = "SELECT * FROM dogs JOIN collars ON dogs.id = collars.dog_id;"
        joined_tables = connectToMySQL(db).query_db(query)
        return joined_tables

    @classmethod
    def join_collars_one_dog(cls, dog_id):
        query = "SELECT * FROM dogs JOIN collars ON dogs.id = collars.dog_id WHERE dogs.id = %(dog_id)s;"
        data = {
            "dog_id": dog_id
        }
        joined_tables = connectToMySQL(db).query_db(query, data)
        return joined_tables

    @classmethod
    def join_dog_toys(cls, dog_id):
        query = "SELECT * FROM dog_toys JOIN dogs_has_dog_toys ON dog_toys.id = dogs_has_dog_toys.dog_toys_id JOIN dogs ON dogs.id = dogs_has_dog_toys.dogs_id WHERE dogs.id = %(dog_id)s;"
        data = {
            "dog_id": dog_id
        }
        return connectToMySQL(db).query_db(query, data)
# U
    @classmethod
    def update_one():
        pass
    


# D
    @classmethod
    def delete_one():
        pass
    
    @classmethod
    def remove_toy(cls, dog_id, toy_id):
        query = "DELETE FROM dogs_has_dog_toys WHERE dog_toys_id = %(toy_id)s AND dogs_id = %(dog_id)s"
        data = {
            "toy_id": toy_id,
            "dog_id" : dog_id
        }
        return connectToMySQL(db).query_db(query, data)