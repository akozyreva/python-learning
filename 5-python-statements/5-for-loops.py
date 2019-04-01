mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# simple example
for num in mylist:
    print(num)

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        # syntax for inserting the val of variable in print function
        print(f'Odd number: {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
print(list_sum)

# we can iterrate through strings
myString = 'Hello World'
for letter in myString:
    print(letter)

tup = (1, 2, 3)
for i in tup:
    print(i)

mylist = [(1, 2, 3), (3, 4, 5), (5,6,7)]
# you can reproduce the type of sequence and have access directly in them, so you don't
# need to execute for in for
for (a, b, c) in mylist:
    print(a,b,c)
 # or you can print only second element of every tuple in list
for (a,b,c) in mylist:
    print(b)

# example with dicts
d = {'k1': 1, 'k2': 2, 'k3': 3}
# by default it iterates only through keys!
for item in d:
    print(item)

#in order to receive values of dict, use this construction
for item in d.items():
    print(item)
# or
for key, val in d:
    print(val)

# or - antoher method for retrieveing values
for val in d.values():
    print(val)
