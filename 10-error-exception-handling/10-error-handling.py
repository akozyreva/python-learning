def add(n1, n2):
    print(n1 + n2)


number1 = 10
number2 = input("Please add a number ")

try:
    # wnat to attempt this code
    # may have an error
    # number 2 is the str by default, so this execution throws an error
    add(number1, number2)
except Exception:
    print("It looks, that you aren't adding correctly")
else:
    # will execute, if there was no exception
    print('Adding looks good')
