# code block
# function
# conditional
# loop
# class

# **** Data Types
'''
1.. Strings
2. Numbers
3. Bools
4. Arrays -> Lists
5. Objects -> Dictionaries
6. Tuples
'''

'''
Strings: -> ""
    "Hello" + "World" = "HelloWorld"
    "2" + 2 = error

    Type Casting
    message = "Hello Tyler!"
    1. %-formatting
        name = Tyler
        message = "Hello %s" % (name)
    2. string.format
        name = Tyle
        message = "Hello {}".format(name)
    3. f-string
        name = Tyler
        age = 32
        message = f"Hello {name} and I am {age} years old"

    common function/methods
    name = "tyler"
    name.upper() -> TYLER
    name.lower() -> tyler


'''

'''
Numbers 
1. Integers -> 1 = 1
2. Floats -> 1 = 1.0
3. complex -> 1a + 2a 

'''

'''
Lists/Array -> []
    1. index
    2. multiple Items
    3. Different Data Types

    my_list = ["Tyler", 32, ["green", "dogs", "motorcycles"], {key1: value1, key2: value2}]
    my_list[0] -> "Tyler"
    my_list[2][1] -> "dogs"
    my_list[3]['key2']

    function/methods
    enumerate
    min()
    sorted(my_list)

    my_list.pop()
'''
my_list = ["Tyler", 32, ["green","dogs", "motorcycles"], {"phone": "Samsung note", "computer_os": "windows/linux"}]
# print(my_list)
# print(my_list[0])
# print(my_list[2][1])
# print(my_list[3]['phone'])
'''
Bools
var x = true
x = True

y = 100 
x = True
sum = y * x
print(sum)

'''

'''
Dictionaries -> {}
1. key and value
2. non index

'''

my_dict = {
    "keyboard": "keychron",
    "phone": "samsung",
    "fav_num": 77,
    "mouse": "Logi",
}

my_list_inside_dict = {
    "list1": ["cats", "dogs", "monkeys"]
}

# print(my_list_inside_dict['list1'][0])

# print(my_dict['phone'])
my_keys = my_dict.keys()
my_vals = my_dict.values()
# for val in my_vals:
#     print(val)

# for key in my_keys:
#     print(my_dict[key])

# print(type(my_list))


'''
Tuples = ()
    tuple1 = ("test1", "test2")
    tuple2 = "test3", "test4"
'''

'''
Loops
1. for loop
2. while loop

for loop 
javaScript
for(let i=0; i<100; i++){
    doJumpingJacks()
}

range()
for i in range(1, 100, 2):


JAVASCRIPT
my_list = ["cats", "dogs", "monkeys"]

for (let i=0; i<my_list.length; i++){
    var animal = my_list[i]
}

for animal in my_list: 
    print(animal)

for animal_index in range(len(my_list)): 
    print(my_list[animal_index])

WHILE 
i = 0
while(i<100):
    print("test")
    i += 1
'''

'''
Condiionals

JAVASCRIPT
if (){}
else if (){} 
else {}

PYTHON
if (x == y): 
    do something cool
elif():

else:

Logic Operators
x == y 
x != y
x > y
x < y
x <= y
x >= y

&& -> And
|| - OR

and 
or 
not

if (x == y and x is z or x == y x is not z):
    more cool stuff

'''
