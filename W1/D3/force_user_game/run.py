from person import Person
from force_user import ForceUser

Tyler = ForceUser("tyler", "Tbo", 32, "blue", strength=1.15)
Christian = ForceUser("christian", "L", 28, "black", force_side_scale=-50, strength=1.13)

class Game:
    def __init__(self):
        self.players = [Tyler, Christian]
        self.is_running = True
        self.stage = 'start'
        
    def run(self):
        while(self.is_running):
            if self.stage == 'start':
                self.starting_menu()
        return self

    def quit_game(self):
        self.is_running = False
        return self

    def create_force_user(self):
        first_name  = input('first name: ')
        last_name = input('last name: ')
        age = input('age: ')
        lightsaber_color = input('lightsaber color: ')

        self.players.append(ForceUser(first_name, last_name, age, lightsaber_color))
        return self

    def load_a_player(self):
        for player in self.players:
            player.printInfo()
        return self

    def starting_menu(self):
        starting_choices = {
            "q": {
                "function": self.quit_game,
                "desc": "q -> Quit Game" 
                },  
            "1": {
                "function": self.create_force_user,
                "desc": "1 -> Create New Character"
            },
            "2": {
                "function": self.load_a_player,
                "desc": "2 -> Load a player"
            }
        }
        for key in starting_choices:
            print(starting_choices[key]['desc'])
        
        user_input = input("what do you want to do? ")

        choice = starting_choices[user_input]['function']
        choice()

        return self

                
Game1 = Game()
Game1.run()

# Bob = Person("bob", "bobbet", 35)

# running = True
# start = True
# players = [Tyler, Christian]

# def quitGame():
#     global running
#     running = False

# def create_force_user():
#     first_name  = input('first name: ')
#     last_name = input('last name: ')
#     age = input('age: ')
#     lightsaber_color = input('lightsaber color: ')

#     return ForceUser(first_name, last_name, age, lightsaber_color)

# def show_all_players():
#     global players
#     for player in players:
#         player.printInfo()

# starting_choices = {
#         "q": {
#             "function": quitGame,
#             "desc": "q -> Quit Game" 
#         },
#         "1": {
#             "function": create_force_user,
#             "desc": "1 -> Create New Character"
#         },
#         "2": {
#             "function": show_all_players,
#             "desc": "2 -> Show all players"
#         }
#     }

# def game_loop():
#     global start, running, starting_choices, players

#     while (running):
#         if start:
#             for key in starting_choices:
#                 print(starting_choices[key]['desc'])
            
#         user_input = input("what do you want to do? ")

#         choice = starting_choices[user_input]['function']
#         choice()

# game_loop()