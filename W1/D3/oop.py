class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class ForceUser(Person):
    def __init__(self, first_name, last_name, age, lightsaber_color, force_side_scale=0, health=1):
        super().__init__(first_name, last_name, age)
        self.health = health*100
        self.force_side_scale = force_side_scale
        self.lightsaber_color = lightsaber_color
    
    def printInfo(self):
        print("^"*80)
        # print(f"name: {self.name}")
        print(f"health: {self.health}")
        print(f"force_side_scale: {self.force_side_scale}")
        print(f"lightsaber_color: {self.lightsaber_color}")
        return self
    
    def loseHealth(self):
        self.health += -10
        return self

    @classmethod
    def forceJump(cls):
        print("You jumped!")

    @staticmethod
    def printForceSide(FSS):
        if FSS > 0:
            print("You are on the light side")
        elif FSS < 0:
            print("You are on the dark side")
        else:
            print("You are nothing")

Tyler = ForceUser("tyler", "Tbo", 32, "blue")
# Christian = ForceUser("Christian", "dark purple", health=0.9)
# Lawrence = ForceUser("Lawrence", "yellow", -15)

Tyler.printInfo().loseHealth().printInfo()
tyler_force_Scale = Tyler.force_side_scale
ForceUser.printForceSide(tyler_force_Scale)


# Tyler.loseHealth()
# Tyler.printInfo()


# Christian.printInfo()
# Lawrence.printInfo()