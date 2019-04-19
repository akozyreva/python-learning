# one.py


def func():
    print("Func in one.py")


print("Top level in one.py")

# check if it runs directly or has been imported
# directly means python3 one.py

if __name__ == "__main__":
    print("One.py is running directly")
else:
    print("One.py hase been imported")
