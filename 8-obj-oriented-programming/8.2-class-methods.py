class Dog():

    # CLASS OBJ Attribute
    # Same for any instance of a class
    # Has no self keyword

    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # OPERATIONS/Actions ---> Methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))


myDog = Dog('lab', 'Sammy')
print(myDog.breed, myDog.name)
print(myDog.species)
myDog.bark(4)
