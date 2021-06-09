class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class ForceUser:
    def __init__(self, force_side, lightsaber_color, force_side_scale=0, health=1):
        self.health = health*100
        self.force_side = force_side
        self.force_side_scale = force_side_scale
        self.lightsaber_color = lightsaber_color
    
    def printInfo(self):
        print("^"*80)
        print(f"name: {self.name}")
        print(f"health: {self.health}")
        print(f"force_side: {self.force_side}")
        print(f"force_side_scale: {self.force_side_scale}")
        print(f"lightsaber_color: {self.lightsaber_color}")
        return self
    
    def loseHealth(self):
        self.health += -10
        return self


Tyler = ForceUser("tyler", "light", "blue")
Christian = ForceUser("Christian", "dark", "dark purple", health=0.9)
Lawrence = ForceUser("Lawrence", "dark", "yellow", -15)

Tyler.printInfo().loseHealth().printInfo()
# Tyler.loseHealth()
# Tyler.printInfo()


# Christian.printInfo()
# Lawrence.printInfo()