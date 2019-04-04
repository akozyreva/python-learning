my_string = 'hello'
my_list = []

# in order to crate from string list, do the following
for letter in my_string:
    my_list.append(letter)
print(my_list)

# but we can write it in shortest way
my_list = [i for i in my_string]
# paste i, which is iterable in a string

# generate list with values from 1 to 10
my_list = [x for x in range(1, 11)]
print(my_list)

# generate list with sqaure values from 1 to 10
my_list = [x**2 for x in range(1, 11)]
print(my_list)

# generate list with sqaure values from 1 to 10, which are even
my_list = [x for x in range(0,11) if x%2 == 0]

# generate list with fahrenheit values
celcius = [0, 10, 20, 34.5]
fahrenheit = [( 9/5 * temp + 32 ) for temp in celcius]
print(fahrenheit)

# how use if-else in short variation - but it's not recommended
results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results)

#loop in loop
my_list = []
for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        my_list.append(x*y)
print(my_list)

# shortest way to do the same
my_list = [x*y for x in [2, 4, 6] for y in [100, 200, 300]]
print(my_list)
