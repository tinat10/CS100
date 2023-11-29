"""
Tina Thai
CS100 2023 Section H11
HW 03, September 25, 2023
"""

import turtle
import math

# Problem 1
square = turtle.Turtle()
for i in range(4):
    square.fd(100)
    square.lt(90) # turns 90 degrees counter clockwise

square.clear()


tri = turtle.Turtle()
for i in range(3):
    tri.fd(100)
    tri.left(120) #same thing as lt()

tri.clear()

pent = turtle.Turtle()
for i in range(5):
    pent.fd(100)
    pent.rt(72) # 180-108 = 72


pent.clear()
turtle.Screen().clear() #clears entire screen

# Problem 2
c = turtle.Turtle()
c.penup()
c.goto(0,-100)
c.pendown()

c.circle(50)
c.penup()
c.goto(0,-150)
c.pendown()

c.circle(100)
c.penup()
c.goto(0,-200)
c.pendown()

c.circle(150)
c.penup()
c.goto(0,-250)
c.pendown()

c.circle(200)

c.clear()
turtle.Screen().clear()

# Problem 3
print("100! =", math.factorial(100))
print("log base 2 of 1000000 =", math.log(1000000, 2)) # if u want more accurate, use print(math.log2(1000000))
print("greatest common divisor of 63 & 49 =", math.gcd(63, 49))# gcd = gratest common divisor




