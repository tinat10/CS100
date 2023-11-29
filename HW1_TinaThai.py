"""
Tina Thai
CS 100 2023 Section H11
HW 01, September 11, 2023
"""

# Exercise 5B
age = 18
height = 65
year = 2023

# Exercise 5C
price = 10.99
temperature = 98.6
weight = 114.8

# Exercise 5D
name = 'Tina Thai'
state = 'new jersey'
college = 'new jersey institute of technology'



# Exercise 1.1 Part 1
print("If you are missing a parenthesis, the computer immediately tells you that you are missing them. This is a syntax error.\n")

# Exercise 1.1 Part 2
print("If you leave out one quotation, you get a syntax error because of an unterminated string literal")
print("If you leave out both quotations, it throws an NameError because the machine is searching for a variable name that does not exist\n")

# Exercise 1.1 Part 3
print("The computer is able to print out 2++2 to equal 4. the arithmetic makes sense")
print(2++2)
print("")

# Exercise 1.1 Part 4
print("You aren't permitted to have leading zeroes in decimal integer literals. you get a syntax error if you use them\n")

# Exercise 1.1 Part 5
print("hi""friend")
print("in a print statement, the computer treats them as if they were one")
print("if they are two variables next to each other, the computer will believe that this is a new variable you are trying to call, so it will give you an error bc there is no variable with that name in their memory.\n")


# Exercise 1.2 Part 1
print(42*60 + 42, 'seconds')

# Exercise 1.2 Part 2
print(10/1.61, 'miles')

# Exercise 1.2 Part 3
print((42*60 + 42) / (10/1.61) / 60, 'minutes per mile')
print((42*60 + 42) / (10/1.61), 'seconds per mile')
print('average speed is', (10/1.61) / ((42*60 + 42)/3600), 'miles per hour')

# Exercise 2.1
print("42 = n is not legal. You get a syntax error")
x = y = 1
print("x = y = 1 is legal")
num = 18
print("you are able to put semi-colons at the end of statements. that's legal.")
print("you cannot put a period at the end of a statment. you get a syntax error.")
print("the computer thinks that xy is a new variable name, so it will not multiply them together. you get an error.")

# Exercise 2.2 Part 1
import math
print (4/3*(math.pi)*(5**3))

# Exercise 2.2 Part 2
price = 24.95 * 0.6
price*=60
price+=3
price+=(59*.75)
print('$',price)

# Exercise 2.2 Part 3
pace = (8.15 * 2) + (3*7.12)
if (pace%1 >= 0.6):
    pace+=0.4

pace/=100
time = 6.52
time+= pace

if (time%1 >= .60):
    time+=0.4
print("It is around", time)
print("It is", int(time), ":", int((time-int(time))*100))







