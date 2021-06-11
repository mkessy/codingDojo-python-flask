from person import Person
import random
import math

class ForceUser(Person):
    def __init__(self, first_name, last_name, age, lightsaber_color, force_side_scale=0, health=1, strength=1.05):
        super().__init__(first_name, last_name, age)
        self.health = health*100
        self.force_side_scale = force_side_scale
        self.lightsaber_color = lightsaber_color
        self.strength = strength
    
    def printInfo(self):
        print("^"*80)
        print(f"name: {self.first_name} {self.last_name}")
        print(f"health: {self.health}")
        print(f"force_side_scale: {self.force_side_scale}")
        print(f"lightsaber_color: {self.lightsaber_color}")
        return self
    
    def attack(self, victim):
        attack_roll = math.floor(random.randrange(1,20) * self.strength)
        victim.defend(attack_roll, self)
        return attack_roll

    def defend(self, amount, attacker):
        print("^"*80)
        defence_roll = random.randrange(1,20)
        # print(f"(defence roll) {self.first_name} {self.last_name} rolled a {defence_roll}")
        if defence_roll < 10:
            print(f"{self.first_name} {self.last_name} rolled a {defence_roll} and was hit for {amount}")
            self.health -= amount
            if self.health <= 0:
                self.dead()
            return self
        elif defence_roll > 16:
            damage = self.attack(attacker)
            print(f"{self.first_name} {self.last_name} rolled a {defence_roll} and parry dealting {damage} damage.")
        else:
            print(f"{self.first_name} {self.last_name} rolled {defence_roll} and blocked that!")
            print("^"*80)
        return self

    def printForceSide(self):
        if self.force_side_scale > 0:
            print("You are on the light side")
        elif self.force_side_scale < 0:
            print("You are on the dark side")
        else:
            print("You are nothing")

    @classmethod
    def forceJump(cls):
        print("You jumped!")


