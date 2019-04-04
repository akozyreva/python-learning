# range operator
mylist = [1, 2, 3]
for num in range(10):
    # it prints all numbers from 0 to 9
    print(num)

for num in range(3, 10):
    # it prints all numbers from 3 to 9
    print(num)

for num in range(0, 10, 2):
    # it prints all numbers from 0 to 9, with the step =2
    print(num)
# I can append to a list result of range
print(list(range(0,11,2)))


word = 'abcde'
for item in enumerate(word):
    print(item)
    # returns a tuple: (0, 'a') (1, 'b')....

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 =  [100, 200, 300]
# zip combines together lists
for item in zip(mylist1, mylist2, mylist3):
    print(item)
    # returns a tuple: (0, 'a', 100) (1, 'b', 200)....

list(zip(mylist1, mylist2))
# return a list of tuples [(0,'a'), (1,'b')]

# check th occurence. result is false
print('x' in [1, 2, 3])

# check th occurence. result will be true
print('x' in ['x', 'y', 'z'])

# you can do it, searching in the word, result will be true
print('a' in 'a world')

# you can check, is key exists in dict. result will be true
print('mykey' in {'mykey': 1})

# or we can check, if value exists.result will be true
d = {'mykey': 345}
print(345 in d.values())
# this returns false
print(345 in d.keys())

mylist = [10, 20, 30, 40, 100]
# returns 10
min(mylist)
# return max = 100
max(mylist)
