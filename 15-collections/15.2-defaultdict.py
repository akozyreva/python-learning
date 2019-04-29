from collections import defaultdict

dict = {'k1': 1}

d = defaultdict(object)
# it should be an object
print(d['one'])
# it created one key and has object as a value
print(d)

# we can programm in the way, when we have default values by default
d = defaultdict(lambda: 0)
# shows 0
print(d['one'])
