import random

class ForceWielder(object):
    def __init__(self, name, race, health=100, ac=10, force_side="light", alignment=10, midichlorian_count="mid"):
        self.name = name
        self.race = race
        self.health = health
        self.ac = ac
        self.force_side = force_side
        self.alignment = alignment
        self.midichlorian_count = midichlorian_count
        self.log = []

    def print_info(self):
        print("*"*80)
        print(f"name: {self.name}")
        print(f"race: {self.race}")
        print(f"health: {self.health}")
        print(f"force_side: {self.force_side}")
        print(f"alignment: {self.alignment}")
        print(f"midichlorian_count: {self.midichlorian_count}")
        print("^"*80)
        print("LOG")
        for item in self.log:
            print(item)
        print("^"*80)
        return self

    def alignment_modification(self, amount):
        self.alignment += amount
        if (self.alignment < 0):
            self.force_side = "dark"
        else:
            self.force_side = "light"
        return self
    
    def defence(self, amount, person):
        attack = random.randrange(1,20)
        # attack = 20
        msg = ''
        if self.ac < attack:
            if attack == 1:
                self.health -= amount * 2
                msg = f"You were looking the other way, and lost {amount * 2} || crit fail"
            else:
                self.health -= amount
                msg = f"You were attacked and lost {amount} || defence roll: {attack}"
            if attack == 20:
                person.attack(amount/2, self)
                msg = f"AMAZING! you sent back half the damage to {person.name} and took no damage!"
        else:
            msg = f"you successfully blocked the attack || defence roll: {attack} - your ac: {self.ac}"
        self.add_to_log(msg)
        return self

    def add_to_log(self, msg):
        self.log.insert(0, msg)
        return self

    def attack(self, amount, person):
        person.defence(amount, person)
        return self

    def force_attack(self):
        pass


while(True):
    user_input = input("what do you want do?")

    if user_input == 'exit':
        break
    