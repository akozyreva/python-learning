class Dog():

    #initalize method, which starts, when you assign class
    def __init__(self, breed, name, spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.my_attr = breed
        self.name = name

        # Expect boolean
        self.spots = spots

# create an instance of cla ss
myDog = Dog('lab', 'Sammy', False)
print(myDog.breed, myDog.name, myDog.spots)
