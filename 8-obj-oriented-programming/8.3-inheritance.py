class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


# dog inherits Animal class
class Dog(Animal):

    def __init__(self):
        # init and self calling parent class
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am dog")

    def bark(self):
        print("Woof!")

myDog = Dog()

# we rewrite method
myDog.who_am_i()
myDog.bark()
