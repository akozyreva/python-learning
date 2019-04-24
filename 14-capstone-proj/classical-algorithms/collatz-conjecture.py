# Collatz Conjecture - Start with a number n > 1. Find the number
# of steps it takes to reach 1 using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.


def collatzConjecture(n):
    step = 0
    print(step, n)
    while n != 1:
        if not(n % 2):
            print(f"{n} is even, {n}/2={n/2}")
            n = n/2
        else:
            print(f"{n} is odd, {n}*3+1={n*3+1}")
            n = n * 3 + 1
        step += 1
    return step


print(collatzConjecture(3))
