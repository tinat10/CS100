"""
Tina Thai
CS100 2023 Section H11
HW 04, October 01, 2023
"""

import turtle
import math

# Problem 1

a = 3
b = 4
c = 5

if a < b:
    print("OK")
if c < b:
    print("OK")
if a + b == c:
    print("OK")
if ((a*a + b*b)  == c*c):
    print("OK")

# Problem 2

if a < b:
    print("OK")
else:
    print("NOT OK")
    
if c < b:
    print("OK")
else:
    print("NOT OK")
    
if a + b == c:
    print("OK")
else:
    print("NOT OK")
    
if ((a*a + b*b)  == c*c):
    print("OK")
else:
    print("NOT OK") 


""" I didn't know if you wanted it like this instead
if not a < b:
    print("NOT OK")
if not c < b:
    print("NOT OK")
if not a + b == c:
    print("NOT OK")
if not ((a*a + b*b)  == c*c):
    print("NOT OK")
"""

# Problem 3

color = input("what color? ")
lineWidth = input("what line width? ")
lineLength = int(input("what line length? "))
shape = input("line, triangle, or square? ")

drawing = turtle.Turtle()
drawing.color(color)
drawing.width(int(lineWidth))
if shape == "line":
    drawing.forward(lineLength)
elif shape == "triangle":
    drawing.forward(lineLength)
    drawing.right(120)
    drawing.forward(lineLength)
    drawing.right(120)
    drawing.forward(lineLength)
elif shape == "square":
    drawing.forward(lineLength)
    drawing.right(90)
    drawing.forward(lineLength)
    drawing.right(90)
    drawing.forward(lineLength)
    drawing.right(90)
    drawing.forward(lineLength)
    drawing.right(90)
    





