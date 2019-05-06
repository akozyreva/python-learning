import timeit

a = "-".join(str(n) for n in range(100))
print(a)

# show the number, which is needed for execution
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
