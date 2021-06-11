class Person:
    def __init__(self, first_name, last_name, age, is_living=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_living = is_living

    def dead(self):
        self.is_living = False
        print("YOU ARE DEAD!")
        return self