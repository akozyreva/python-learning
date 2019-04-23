def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


print(create_cubes(10))

for x in create_cubes(10):
    print(x)

# another way to do it with less of memory


def create_cubes(n):
    for x in range(n):
        yield x**3


# and result is the same
for x in create_cubes(10):
    print(x)
# or we can crate a list
print(list(create_cubes(10)))
# but  create_cubes(10) shows only, that it's generator


def gen_fibon(n):
    a, b = 1, 1
    for i in range(n):
        # yield a - the same as result.append(a) and returns result in the end of func
        yield a
        a, b = b, a+b


print(list(gen_fibon(10)))
