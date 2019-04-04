from random import shuffle, randint

mylist = [1,2,3,4,5,6,7,8,9,10]
# shuffle doesn't return anything, it simply changes existing list
shuffle(mylist)
# now the values have another, randomed positions
print(mylist)

# returns random integer
print(randint(0, 100))
