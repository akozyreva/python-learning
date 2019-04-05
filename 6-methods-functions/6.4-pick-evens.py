# Define a function  that takes in an arbitrary number of arguments, and returns a
# containing only those arguments that are even.

def even_func(*args):
    mylist = []
    for i in args:
        print(i)
        if not(i%2):
            mylist.append(i)
    return mylist
print(even_func(1,2,4,5,6))
