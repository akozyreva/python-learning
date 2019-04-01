#  create file, if it doesnt't exist and write text into it
#  w+  read and write (overwrites existinf file or create a new file)
#  w   only write
#  r   only read
#  a   adding more lines to the end of file
f = open("test.txt","w+")
f.write("Hello this is a text file\n")
f.write("this is a second line\n")
f.write("this is a third line")
#  returns everything from a file as a big string
f.close()
f = open("/Users/akozyreva/projects/python-learning/test.txt")
print(f.read())
# in order to put cursor in the beginning of file after reading, run the following
f.seek(0)

content = f.read()
#  shows all content of file
print(content)
f.seek(0)

# return text as list, where every element is a line in file
print(f.readlines())

# with special key with, I don't need to close session with file every time
with open("test.txt") as my_new_file:
    content = my_new_file.read()
    print(content)

# example of append mode - when we add text in the end of file
with open("test.txt", "a") as my_new_file:
    my_new_file.write('\nfour line')

with open("test.txt", "r") as my_new_file:
    content = my_new_file.read()
    print(content)
