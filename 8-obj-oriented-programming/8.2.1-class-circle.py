class Circle():

    # Class obj attr
    pi = 3.14

    def __init__(self, radius=1):
         self.radius = radius
         self.area = radius * radius * self.pi

    # Methods
    def get_circumference(self):
        return self.radius * self.pi * 2

myCircle = Circle(30)
print(myCircle.area)
print(myCircle.get_circumference())
