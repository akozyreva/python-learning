myList = [1, 2, 3]

class Sample():
    pass

mySample = Sample

# and we unable to check the len of mySmaple - it's getting an error
# print(len(mySample))
# how can we use usual methods in class?

class Book():
    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # we programm methods ourself
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book has been deleted")

pythonBook = Book('Python3', 'Jose', 200)

# and if we try to print(pythonBook), we see only machine lang text
# we need to create inside __str__ method to see result

print(str(pythonBook))
print(len(pythonBook))

# in order to delete the instance you need to run
# but justify del method, we can insert print function in it
del pythonBook
