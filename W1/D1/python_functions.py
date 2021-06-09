# DRY -> do not repeat yourself

# a function becomes what it returns
def add(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    return sum

def sub(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 - num2

def div(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 / num2
    return sum

def mult(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 * num2
    return sum

run = True
while (run):
    opperation = input("what opperation? add, sub, div, mult, exit: ")
    if opperation == 'exit':
        run = False
    else:
        num1 = input("what number for num 1: ")
        num2 = input("what number for num 2: ")
        sum = 0
        if opperation == 'add':
            sum = add(num1, num2)
        if opperation == 'sub':
            sum = sub(num1, num2)
        if opperation == 'div':
            sum = div(num1, num2)
        if opperation == 'mult':
            sum = mult(num1, num2)
        print(sum)
