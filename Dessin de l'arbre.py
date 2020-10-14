import turtle
import math
turtle.setheading(-90)
turtle.heading()
angle=30
proportion=0.8
turtle.setheading(90)
turtle.heading()
def arbre(grandeur,rep):
    if 0<rep:
        turtle.forward(grandeur)
        turtle.setheading(90-angle)
        turtle.heading()
        turtle.forward(proportion*grandeur)
        arbre(proportion*grandeur,rep-1)
        turtle.done()
    return
arbre(50,3)
