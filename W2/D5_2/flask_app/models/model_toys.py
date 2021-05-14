from flask_app.config.mysqlconnection import connectToMySQL

db = "dogs_db"

class Toy:
    def __init__(self, data):
        self.id = data['id']

# C
    @classmethod
    def new(cls, info):
        query = "INSERT INTO dog_toys (name) VALUES (%(name)s)"
        data = {
            "name": info['name'],
        }
        created_toy_id = connectToMySQL(db).query_db(query, data)

        # query = "SELECT * FROM collars WHERE id = %(toy_id)s"
        # data = {
        #     "toy_id": created_toy_id
        # }
        # created_toy = connectToMySQL(db).query_db(query, data)[0]

        return created_toy_id
    
# R
    @classmethod
    def get_all(cls, dog_id=None):
        if dog_id != None:
            query = 'SELECT * FROM dogs JOIN dogs_has_dog_toys ON dogs.id = dogs_has_dog_toys.dogs_id JOIN dog_toys ON dog_toys.id = dogs_has_dog_toys.dog_toys_id WHERE dogs.id != %(dog_id)s;'
            data = {
                "dog_id": dog_id
            }
            all_toys = connectToMySQL(db).query_db(query, data)
            print(all_toys)
        else:
            query = 'SELECT * FROM dog_toys;'
            all_toys = connectToMySQL(db).query_db(query)
        return all_toys

    @classmethod
    def get_one(cls, id):
        query = 'SELECT * FROM dog_toys WHERE id = %(toy_id)s;'
        data = {
            "toy_id": id
        }
        one_user = connectToMySQL(db).query_db(query, data)[0]
        return one_user
# U
    @classmethod
    def update_one():
        pass

# D
    @classmethod
    def delete_one():
        pass