'''
Tina Thai
CS100 2023 Section H11
HW 11, November 17, 2023
'''

# Problem 1, 2, 5
class Dog:

    species = 'Canis familiaris'
    
    '''This is the Dog object class'''
    def __init__(self, name, breed, tricks = []):
        self.name = name
        self.breed = breed
        self.tricks  = tricks

# Problem 3
    def teach(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
        print(f'{self.name} knows {trick}')

# Problem 4
    def knows(self, trick):
        if trick not in self.tricks:
            print(f'No, {self.name} does not know {trick}')
        else:
            print(f'Yes, {self.name} knows {trick}')
        return(trick in self.tricks)

