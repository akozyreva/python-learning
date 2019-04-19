try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except Exception:
    print("Ooops, problem with i")

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("It's impossible to divide on 0")
finally:
    print("All Done")


def ask():
    while True:
        try:
            number = int(input("Input an integer: "))
        except Exception:
            print("Seems, it's not an integer")
        else:
            print(f"Thank you, your number squared is:  {number ** 2}")
            break


ask()
