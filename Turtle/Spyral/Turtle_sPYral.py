#   Draws a random color spiral

import turtle
import random

jorel = turtle.Turtle()

def change_color() :
    R = random.random()
    G = random.random()
    B = random.random()

#   Returns Turtle new and shiny color !!
    return jorel.color(R,G,B)

for i in range (500) :    
    
    jorel.right(20)
    jorel.forward(2)

    change_color()

    if i % 2 == 0 :
        jorel.forward(i * 0.1)
        jorel.right(i * 0.01)
    
    if i /2 != 0 :
        jorel.forward(i * 0.2)
        jorel.right(i * 0.02) 
    
    jorel.speed(i * 2)

#   Gives TURTLE some deserved rest           
turtle.done()
