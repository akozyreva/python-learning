import random
# let's create generator for list sorting


def create_random_list(low, high):
    len = high - low
    for x in range(len):
        yield random.randint(low, high * low)


alist = list(create_random_list(2, 7))


def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


print(alist)
bubbleSort(alist)
print(alist)
