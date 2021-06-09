from person import Person
from force_user import ForceUser

Bob = Person("bob", "bobbet", 35)
Tyler = ForceUser("tyler", "Tbo", 32, "blue")
Christian = ForceUser("christian", "L", 28, "black", force_side_scale=-50)

while (Christian.is_living and Tyler.is_living):
    print("%"*50)
    print(f"Christian: {Christian.is_living} || Health: {Christian.health}")
    print(f"Tyler: {Tyler.is_living} || Health: {Tyler.health}")
    print("%"*50)
    Christian.attack(Tyler)
    Tyler.attack(Christian)



# def game_loop():
#     players = [Tyler]
#     running = True
#     while (running):
#         user_input = input("what do you want to do? ")

#         if user_input == 'exit':
#             running = False

#         elif user_input == 'create new player':
#             new_player = create_force_user()
#             players.append(new_player)
        
#         elif user_input == 'show all players':
#             for player in players:
#                 player.printInfo()

# def create_force_user():
#     first_name  = input('first name: ')
#     last_name = input('last name: ')
#     age = input('age: ')
#     lightsaber_color = input('lightsaber color: ')

#     return ForceUser(first_name, last_name, age, lightsaber_color)

# game_loop()