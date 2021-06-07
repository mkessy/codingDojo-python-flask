

## javaScript

```js
function random(listOfStuff){
    // Do something
    for (leti=0; i<listOfStuff.lenth, i++){
        console.log(listOfStuff[i])
    }
}
```

## python

```py
def random(list_of_stuff):
    # do something
    for item in list_of_stuff:
        print(item)
        item = "joe"
    # do something else outside of the for loop

# another function
```

## Vars

```js
var x = 0
let x = 0
const x  = "tyler"

function something(arr){
    const x = "tyler"
    for (let i=0; i.arr.length; i++){
        console.log(i)
    }
    console.log(i)
    x = "joe" // error out because you can't change a const once it is set
}

x  = "joe"

output: "tyler4"
```

```py
x = "tyler"
x + 4
```

**types**
1. strings
1. numbers -> ints
1. booleans
1. lists -> array
1. tuples 
1. dictionaries -> objects

```py
string = "a string"
list = [item1, item2, item3]
dict = {
    "key1": "value1"
}

dict["key1"]
list[1]

```


## codeblocks
- def -> functions
- if, elif, else -> if, else if, else
- for, while
- class = blueprints


## Type casting

```py

x = 5
y = "2"

def add(int(x), int(y)):
    print("you are adding %s and %s" %(x, y))
    print("you are adding %s and %s".format(x, y))
    print(f"you are adding {x} and {y}")
    return x + y



def print_name(given_name):
    name = given_name.upper() # TYLER
    name = given_name.lower() # tyler
    name = given_name.capitalize() # Tyler
    return name

whatever = "tyler"
my_name = "lawrence"

print_name(whatever)
print_name(my_name)


```

```js
console.log(`something ${var1}`)

```