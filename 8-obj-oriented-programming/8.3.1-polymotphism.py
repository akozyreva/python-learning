class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"

class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

# polymorphism is a way to share methods between classes
for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

# in order not to repeat speak method, we create abstraction class
class Animal():

    def __init__(self, name):
        self.name = name

    # it's abstract class, which would inherit
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow"

fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())
