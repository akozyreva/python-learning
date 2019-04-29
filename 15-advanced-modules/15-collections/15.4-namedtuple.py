from collections import namedtuple

# it's the tuple, but with key-values pair
Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')
# and you can call value by index or by the name
print(sam.age, sam[0])
