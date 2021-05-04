# Debug
def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list

a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# >>>[2,4,10,16]

def printing_something_cool(*args, **kwrgs):
    print(f"args: {args}")
    print(f"kwrgs: {kwrgs}")

printing_something_cool(num=10, something_cool="Sean is cool")
printing_something_cool(10, "Christian is cool") 
printing_something_cool(10, something_cool="Christian is cool") 