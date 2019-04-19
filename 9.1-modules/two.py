# two.py
import one

print("Top level in two.py")

one.func()

if __name__ == "__main__":
    print("Two.py is running directly")
else:
    print("Two.py hase been imported")
print("The end of execution")
