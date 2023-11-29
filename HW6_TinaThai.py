"""
Tina Thai
CS100 2023 Section H11
HW 06, October 16, 2023
"""

# Problem 1A

def hasFinalLetter(strList, letters):
    strings = []
    for word in strList:
        if word[-1].lower() in letters.lower():
            strings.append(word)
    return strings

# Problem 1B

lst = ['cat', 'ice', 'bat', 'zerO', 'herO', 'idea']
lets = 'AeIoU'
print(hasFinalLetter(lst, lets))

lst = ['tina', 'lauren', 'audrey', 'lizzie', 'tramina', 'irina', 'sharon']
lets = 'aNmo'
print(hasFinalLetter(lst, lets))

lst = ['apple', 'banana', 'orange', 'pineapple', 'strawberry', 'watermelon']
lets = 'zQRfPl'
print(hasFinalLetter(lst, lets))

print()
# Problem 2A

def isDivisible(maxInt, twoInts):
    nums = []
    for i in range(1, maxInt):
        if i%twoInts[0]==0 and i%twoInts[1]==0:
            nums.append(i)
    return nums        

# Problem 2B
print(isDivisible(10, (2, 4)))
print(isDivisible(100, (5, 10)))
print(isDivisible(50, (35, 17)))











