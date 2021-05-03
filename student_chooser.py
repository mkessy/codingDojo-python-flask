import random

students = [
    "Antonio Brunetto",
    "Austin Carson",
    "Branden Holmes",
    "Dennis Klykavka",
    "Eric Nuss",
    "Gary Mckinnon",
    "Ikmann Bhullar",
    "Kris Bratvold",
    "Kyle Emerson",
    "Nardos Hiluf",
    "Nicholas Towne",
    "Sean Caylor",
    "Sean Ruddell",
    "Si Chen",
    "Steven Moore",
    "Vince Ling",
]

random_student = random.randrange(0,len(students))
print(f"************************************************* {students[random_student]} **************************************")