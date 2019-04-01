name = "Sam"
# you can't change string direclty. It throws an error
# name[0] = 'P'
last_letters = name[1:]
print('P' + last_letters)

x = "Hello World"
print (x + " it's beautful outside")
# using mehtod upper, we make all strings in hello world bigger
print(x.upper())
print(x.lower())
# split mehtod allows to split words into the list - by default it splits by the whitespace
print(x.split())
# reverting string
print('test'[::-1])
x = 'Hi this is a string'
# spliting by the i letter - i was removed
print(x.split('i'))

# FORMATING STRINGS
# you can paste string in the place, where you put curly braces
print("this is a string {}".format('INSERTED'))
# insert values in the same order as you specify them in format function. Also you can change the order
print("The {2} {1} {0}".format('fox', 'brown', 'quick'))

print("The {q} {b} {f}".format(f = 'fox',b = 'brown', q = 'quick'))

result = 100/777
# if you want to reduce the size of precision
# 1 = it's the width of string before decimal ?? if it's 1 - it shows all numbers before decimal
print("{r:1.3}".format(r = result))

# new method in python 3.7 for formating strings - it's easier to write
name = "Jose"
print(f"Hello, his name is {name}")
