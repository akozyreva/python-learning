x = 25

def printer():
    x = 50
    return x

# it shows 25, because x in function has its own scope
print(x)

name = 'GLOBAL STRING'

def greet():
    name = 'Sammy'

    def hello():
        print('Hello ' + name)

    hello()

# it show Hello Sammy, because it goes from local scope to global scope
greet()

name = 'GLOBAL STRING'

def greet():

    def hello():
        print('Hello ' + name)

    hello()

# and now it shows Hello GLOBAL STRING, because there is no variable inside of function
greet()


name = 'GLOBAL STRING'

def greet():
    name = 'Sammy'
    def hello():
        name = 'Tommy'
        print('Hello ' + name)

    hello()

# and now it shows Hello Tommy, because variable was found in local scope
greet()

x = 50
def func():
    # we declare to use x from global scope for chang
    global x
    print(f'X is {x}')
   # and now we change the value of global x
    x = 'new value'
    print(f'I just locally changed x to {x}')

# shows 50
print(x)

func()
# now it shows 'new value'
print(x)
