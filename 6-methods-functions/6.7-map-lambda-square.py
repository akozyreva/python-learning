def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]
# map - 1 arg is function, second is the list of variables
# we create for-loop for passing function through all args
for item in map(square, my_nums):
    print(item)

# if you want to return list, run this
print(list(map(square, my_nums)))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]
names = ['Andy', 'Eve', 'Brayan']
print(list(map(splicer, names)))

def check_even(num):
    return num % 2 == 0
my_nums = [1, 2, 3, 4, 5, 6]
# filter show only results, which match the condition from function
print(list(filter(check_even, my_nums)))

for n in filter(check_even, my_nums):
    print(n)

# lambda
# here is function which returns a square of num
new_square = lambda num: num ** 2
print(new_square(5))
# but usually we don't assign variable to lambda expression
# we use it as helper function as in example bellow
print(list(map(lambda num: num ** 2, my_nums)))
print(list(filter(lambda num: num % 2 == 0, my_nums)))
print(list(map(lambda name: name[::-1], names)))
