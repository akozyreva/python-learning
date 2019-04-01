# tuples have immutability - it's main difference from the list
t = (1, 2, 3)
mylist = [1, 2, 3]
type(t)
# you can reassign tuple
t = ('one', 2)
print(t[0])

t = ('a', 'a', 'b')

# count reutrns, how may time a appears
print(t.count('a'))
# show index of 1 occurence
print(t.index('b'))

# we can't change values in tuple
# t[0]  = 'NEW'  it shows an error, it's incorrect
