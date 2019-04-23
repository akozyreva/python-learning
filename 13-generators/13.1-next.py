def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

# we assign the generator to a new variable g
g = simple_gen()
print(next(g))
# output is 0
print(next(g))
# output is 1
print(next(g))
# output is 2
