def hello(name='Jose'):
    print("The hello() fucntion has been executed!")

    def greet():
        return '\t This is the greet() function inside hello'

    def welcome():
        return '\t This is welcome() inside hello'

    print("I'm going to return a function!")

    # we return the function, which we can execute then
    if name == 'Jose':
        return greet
    else:
        return welcome


my_new_func = hello()
# now in variable my_new_func we have greet function
# it's the way, how we can access to the function
# which was inside in another function
print(my_new_func())
