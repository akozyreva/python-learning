# sets - it's unordered collection of the unique items you want
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
# it doesn't make sense, because we still have {1, 2}, so it will be ignored
mySet.add(2)

mylist = [1,1,1,1,1,2,2,2]
# shows only unique values!
print(set(mylist))

# it also works with strings
print(set('Mississippi'))
