class Pacman(object):
    def __init__(self, name, color, position=[0,0], is_vulnerable=True, life_count=3):
        self.name = name
        self.color = color
        self.position = [*position]
        self.is_vulnerable = is_vulnerable
        self.life_count = life_count
    
    def print_info(self):
        print("*"*80)
        print(f"name: {self.name}")
        print(f"color: {self.color}")
        print(f"position: {self.position}")
        print(f"is_vulnerable: {self.is_vulnerable}")
        print(f"life_count: {self.life_count}")
        return self
    
    def move(self, direction):
        self.position[0] += 1 
        return self

pac1 = Pacman("pac1","green")
pac2 = Pacman("pac2","blue")

pac1.move("down").print_info().move("up").print_info()

pac2.print_info()