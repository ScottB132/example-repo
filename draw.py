
# Learning how to draw with turle 


import turtle

t = turtle.Turtle()

t.color("black", "yellow")

def draw_square(turtle_obj, size):  
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size)

turtle.getscreen().bgcolor("#ffff00")
for _ in range(5):
    t.forward(100)
    t.left(216)

turtle.done()

 