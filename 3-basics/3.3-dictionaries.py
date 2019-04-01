my_dict = {
    'key1': 'value1',
    'key2': 'value2'
}
print(my_dict['key1'])

prices_lookup = {
    'apple': 2.99,
    'oranges': 1.99,
    'milk': 5.80
}

print(prices_lookup['apple'])

d = {
    'k1': 123,
    'k2': [0,1, 2],
    'k3': { 'insideKey': 100 }
}

# in order to recieve val from dict in dict
print(d['k3']['insideKey'])

# retrieve val from index
print(d['k2'][2])

d = {
    'key1': ['a', 'b', 'c']
}

# and after retriving I can use methods
print(d['key1'][2].upper())

# adding key-values to dict and editing
d = {
    'k1': 100,
    'k2': 200
}
d['k3'] = 300
d['k1'] = 'NEW VALUE'
print(d)

# show all keys
print(d.keys())

# show all values
print(d.values())

# show key-value pairs
print(d.items())
