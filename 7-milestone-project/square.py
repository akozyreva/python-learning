import turtle

# to draw a square, or eventually a turtle, you need to do the things below

def draw_square():
    """ draw square for turtles """
    t = turtle.Turtle()
    for i in range(4): # for loop will run 4 times
      t.forward(100) #Forward turtle by 100 units
      t.left(90) #Turn turtle by 90 degree

    t2 = turtle.Turtle()
    for i in range(4): # for loop will run 4 times
      t2.backward(100) #Forward turtle by 100 units
      t2.right(90) #Turn turtle by 90 degree

    t3 = turtle.Turtle()
    for i in range(4): # for loop will run 4 times
        t3.backward(100) #Forward turtle by 100 units
        t3.left(90) #Turn turtle by 90 degree

    t4 = turtle.Turtle()
    for i in range(4): # for loop will run 4 times
        t4.forward(100) #Forward turtle by 100 units
        t4.right(90) #Turn turtle by 90 degree

    t5 = turtle.Turtle()
    t5.forward(200)
    t5.right(90)
    t5.forward(100)
    t5.right(90)
    t5.forward(100)
    t5.right(90)
    t5.forward(100)

    t6 = turtle.Turtle()
    t6.forward(200)
    t6.left(90)
    t6.forward(100)
    t6.left(90)
    t6.forward(100)
    t6.left(90)
    t6.forward(100)
window = turtle.Screen()


draw_square()

window.exitonclick()  # click the screen to close it
