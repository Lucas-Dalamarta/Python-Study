#   PAINTING DIFFERENT SHAPES USING TURTLE
import turtle  
##### CREATING THE CURSORS #####
x           =   turtle.Turtle()
triangle    =   turtle.Turtle()
square      =   turtle.Turtle()
circle      =   turtle.Turtle()
##### SETTING COLORS ###########
x.pencolor("blue")
square.pencolor("pink")
triangle.pencolor("green")
circle.pencolor("red")
##### SETTING PENSIZES #########
x.pensize(3)
square.pensize(3)
triangle.pensize(3)
circle.pensize(3)
##### SETTING POS ##############
x.penup()
x.setpos(0,-60)
x.pendown()

square.penup()
square.setpos(-75,0)
square.pendown()

triangle.penup()
triangle.setpos(0,45)
triangle.pendown()

circle.penup()
circle.setpos(90,0)
circle.pendown()
################################


def draw():
    draw_circle()
    draw_x()    
    draw_triangle()
    draw_square()

def draw_circle():
    for i in range(120):
        circle.left(3.14)
        circle.forward(1.2)

def draw_x():    
    x.left(45)
    x.forward(50)
    x.right(180)
    x.forward(25)
    x.right(90)
    x.penup()
    x.forward(25)
    x.pendown()
    x.right(180)
    x.forward(50)

def draw_triangle():  
    for i in range(3):
        triangle.forward(50)
        triangle.left(120)

def draw_square():    
    for i in range(4):
        square.forward(40)
        square.left(90)

draw()

turtle.done()
