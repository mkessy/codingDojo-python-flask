x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'Basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1.1. Change 10 -> 15 inside x
x[1][0] = 15
# print(x[1][0])

# 1.2. 
y = 'last_name'
students[0][y] = 'Bryant'
# print(students)

# 1.3
sports_directory['soccer'][0] = "Andres"
# print(sports_directory)

# 1.4
z[0]['y'] = 30
# print(z)

# 2.
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(incoming_list):
    for dict_index in range(len(incoming_list)):
        dict = incoming_list[dict_index]

        f_name = dict['first_name']
        l_name = dict['last_name']
        print(f"first_name - {f_name}, last_name - {l_name}")

# iterateDictionary(students)

# 3.
def print_dict_info(key, incoming_list):
    # print(f"key: {key} incoming_list: {incoming_list}")
    for dict in incoming_list:
        print(dict[key])

# print_dict_info('first_name', students)

# 4.
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_loc_and_instructors(incoming_dict):
    all_keys = incoming_dict.keys()
    for key in all_keys:

        total_len = len(incoming_dict[key])
        current_list = incoming_dict[key]

        print(f"{total_len} {key.upper()}")
        
        for item in current_list:
            print(item)
            if item == "Devon":
                break
        else:
            print('')

print_loc_and_instructors(dojo)

'''
OUTPUT: 
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

'''