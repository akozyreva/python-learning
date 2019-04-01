print(7 // 4)
# output 1.75

print(7 % 4)
# output 3, beacause it shows reminder of division

print(7 // 4)
# output 1

print(2 ** 3)
# output 8, because 2*2*2

# =============================
# VARIABLES
my_dog = 2
my_dog = 'test'
print(my_dog, type(my_dog))
# show test and type = str
# =============================

# STRINGS
phrase = 'hello'
# in order to avoid mistakes with ' use double quotes instead
long_phrase = " I'm going on a run "

# for showing content on the next line
print('hello \nworld')
# see length of string
print(len(phrase))

# INDEX AND SLICING OF STRINGS
mystring = "Hello World"
print(mystring[0])
# we can use reverse order for indexing
print(mystring[-2])  # shows l from word World
print(mystring[-3])   # shows r from word World

# show all characters from 2 element to the end
print(mystring[2:])

# show all characters from very beginning to the 3 element (not included!)
print(mystring[:3])

# show 3 characters from 3 element
print(mystring[3:6]) #output was lo and space

# by default the step is 1.  but we can specify it - so, show all characters, go up by 2 characters, not by 1
print(mystring[::2])
print(mystring[::3])
print(mystring[::-1])  # go from back to the front
