# 1.

x = [ [5,2,3], [10,8,9] ] 

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

'''
a. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
b. Change the last_name of the first student from 'Jordan' to 'Bryant'
c. In the sports_directory, change 'Messi' to 'Andres'
d. Change the value 20 in z to 30
'''
# 1.a
x[1][0] = 15
# print(x)

# 1.b
students[0]['last_name'] = 'Bryant'
# print(students)

# 1.c
sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# 1.d
z[0]['y'] = 30
# print(z)

# 2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(incoming_list):
    for dict in incoming_list:
        print(f"first_name - {dict['first_name']}, last_name - {dict['last_name']}")

# iterateDictionary(students) 

'''
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''

# 3

def iterateDictionary2(key_name, some_list):
    for dict in some_list:
        print(dict[key_name])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

'''
if key_name == 'first_name'
Michael
John
Mark
KB

if key_name == 'last_name'
Jordan
Rosales
Guillen
Tonel
'''

# 4

'''
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
1. prints the name of each key along with the size of its list, 
2. and then prints the associated values within each key's list. For example:

# output:
7 LOCATIONS x
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS x
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

'''

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        some_list = some_dict[key]
        for item in some_list:
            print(item)
        print('')

printInfo(dojo)



# some_list = ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank']
# for item in some_list:
#     print(item)