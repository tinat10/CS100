"""
Tina Thai
CS100 2023 Section H11
HW 05, October 03, 2023
"""

# Problem 1
months = ['January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'November', 'December']
for month in months:
    if month[0] == 'J':
        print(month)

print()

# Problem 2
for num in range(0, 100):
    if (num%2==0 and num%5==0):
        print(num, end = " ")

print()

# Problem 3
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for let in horton:
    if (let in vowels):
        print(let, end = " ")



