import random
# Problem 1
# Create a generator that generates the squares of numbers up to some number N.


def genSquares(N):
    for i in range(N):
        yield i ** 2


for x in genSquares(10):
    print(x)

# Problem 2
# Create a generator that yields "n" random numbers between a low and
# high number (that are inputs).
# Note: Use the random library.


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


print(list(rand_num(1, 10, 12)))

# Problem 3
# Use the iter() function to convert the string below into an iterator:
s = 'python'
s_iter = iter(s)
print(next(s_iter))


# another way to create Generator
generator = (x**2 for x in range(1, 11))
print(generator)
for i in generator:
    print(i)
