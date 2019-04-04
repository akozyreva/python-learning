# *args - returns a tuple
# kwargs return a dictionary
# **kwargs
def myfunc(a, b, c=0, d=0, e=0 ):
    # REturns 5% of the sum of a and b
    return sum((a,b,c,d,e)) * 0.05

print(myfunc(2,4))
# but it's not convenient. we can cpesify args, which has no limit in variables
# and it will be 1 tuple
def myfunc(*args):
    print(args)
    for item in args:
        print(item)
    return sum(args) * 0.05

print(myfunc(1,2,3,4,5,6,7,8))

def myfunc(**kwargs):
    print(kwargs)
    # output is {'fruit': 'apple', 'veggie': 'lettuce'}
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I didn\'t find any fruit here')

myfunc(fruit='apple', veggie='lettuce')

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
myfunc(10,'test', path='relative')
# it returns empty tuple and dict
myfunc()
