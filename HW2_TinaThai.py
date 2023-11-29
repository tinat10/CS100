"""
Tina Thai
CS 100 2023 Section H11
HW 02, September 15, 2023
"""

# Question 1
grades =  ['A', 'B', 'A', 'C', 'D', 'F', 'A', 'B', 'A', 'B']
frequency = [0, 0, 0, 0, 0];

for grade in grades:
    print(grade, end = " ")
    if grade == 'A':
        frequency[0]+=1
    elif grade == 'B':
        frequency[1]+=1
    elif grade == 'C':
        frequency[2]+=1
    elif grade == 'D':
        frequency[3]+=1
    elif grade == 'F':
        frequency[4]+=1
print()
for times in frequency:
    print(times, end = " ")
print()

# USING COUNT METHOD

frequency2 = [0, 0, 0, 0, 0];
frequency2[0] = grades.count('A')
frequency2[1] = grades.count('B')
frequency2[2] = grades.count('C')
frequency2[3] = grades.count('D')
frequency2[4] = grades.count('F')

for times in frequency2:
    print(times, end = " ")
print()


# Question 2A
dog_breeds = ['collie', 'sheepdog', 'chow', 'chihuahua']
print(dog_breeds)
print()

# Question 2B
herding_dogs = dog_breeds[0:2:1]
print(herding_dogs)
print()

# Question 2C
tiny_dogs = dog_breeds[-1]

for dog in tiny_dogs:
    print(dog, end = " ")
print()

# Question 2D
print("Is the dog breed 'persian' in the list:", 'persian' in dog_breeds)
print("Is the dog breed 'persian' in the list:", not dog_breeds.count('persian') == 0)

  





