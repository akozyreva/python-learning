import random
# let's create generator for list sorting


def create_random_list(low, high):
    len = high - low
    for x in range(len):
        yield random.randint(low, high * low)


alist = list(create_random_list(2, 7))


def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        print("Begin of iteration")
        print("================")
        print("iteration, when sorts elements =", passnum + 1)
        for i in range(passnum):
            print("check values", alist[i], alist[i+1])
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                print("new values!", alist[i], alist[i + 1])
            print(alist)
        print("End of iteration")
        print("==========")



print('initial list', alist)
bubbleSort(alist)
print('final list', alist)
