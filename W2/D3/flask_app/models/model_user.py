# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class User: # pascal case -> first letter Uppercase and the word is singular
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.

        results = connectToMySQL('mydb').query_db(query)
        # Create an empty list to append our instances of friends

        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
            
    @classmethod
    def get_one_by_id(cls, id):
        query = "SELECT * FROM users WHERE id=%(user_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.

        data = {
            "user_id": id
        }

        results = connectToMySQL('mydb').query_db(query, data)
        # Create an empty list to append our instances of friends

        if len(results) < 1:
            print("false")
            return False
        
        return cls(results[0])

    @classmethod
    def get_one_by_username(cls, username):
        query = "SELECT * FROM users WHERE username=%(username)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.

        data = {
            "username": username
        }

        results = connectToMySQL('mydb').query_db(query, data)
        # Create an empty list to append our instances of friends

        if len(results) < 1:
            print("false")
            return False
        
        return cls(results[0])