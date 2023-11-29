'''
Tina Thai
CS100 2023 Section H11
HW 08, October 29, 2023
'''

# Problem 1
def twoWords(length, firstLetter):
    while True:
        word = input(f'Enter a {length} letter word please: ')
        if len(word) == length:
            break
    while True:
        word2 = input(f'Enter a word beginning with {firstLetter} please: ')
        if word2[0].lower() == firstLetter.lower():
            break;

    return [word, word2]

print(twoWords(4, 'c'))
print()

# Problem 2
def twoWordsV2(length, firstLetter):
    word = ''
    while len(word) != length:
        word = input(f'Enter a {length} letter word please: ')
    word2 = input(f'Enter a word beginning with {firstLetter} please: ')
    while word2[0].lower() != firstLetter.lower():
        word2 = input(f'Enter a word beginning with {firstLetter} please: ')

    return [word, word2]

print(twoWordsV2(4, 'c'))
print()

# Problem 3
def enterNewPassword():
    while True:
        password = input('Enter a password that has 8-15 characters w/ at least one digit: ')
        if password.isalpha():
            hasNumber = False
        else:
            hasNumber = True
        if len(password) > 16 or len(password)< 7:
            goodLength = False
        else:
            goodLength = True
        if hasNumber == False and goodLength == False:
            print('FAILED BOTH TESTS. PASSWORD MUST CONTAIN A # AND HAVE 8-15 CHARS')
        elif goodLength == False:
            print('FAIL! PASSWORD MUST BE 8-15 CHARACTERS')
        elif hasNumber == False:
            print('FAIL! PASSWORD MUST BE CONTAIN A NUMBER')
        else:
            print('Good password saved')
            break


enterNewPassword()
print()

# Problem 4
import random

print('I am thinking of a number in the range 0-50. You have five tries to guess it.')
rando = random.randint(0,50)
num, count = -1, 1
while rando!=num and count<6:
    num = int(input(f'Guess {count}?  '))
    if (num > rando):
        print(f'{num} is too high')
    elif (num < rando):
        print(f'{num} is too low')
    else:
        print(f'You are right! I was thinking of {num}')
    count+=1

if count > 5 and num!=rando:
    print('GAME OVER. The number was', rando)

