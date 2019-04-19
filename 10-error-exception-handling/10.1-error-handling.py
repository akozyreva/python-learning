try:
    # open or create a new file and write to it
    f = open('testfile', 'r')
    f.write("Write a test line")
# except only if it's a type error!
except TypeError:
    print("There was a type error")
# type of errors can be find in documentation
except OSError:
    print("Oh, you have an Os Error")
# block, which is always executed
finally:
    print("I always run")
