# dictionary = hashMap = hashes = sparse arrays

eng2sp = {'one': 'uno', 'red':'rojo', 'blue':'azul', 'yellow':'amarillo', 'cat':'gato'}
#{<key>:<value>}
# keys MUST BE of immutable data types (i.e. strings, tuples, floats)
# keys CANNOT BE mutable data types (i.e. dictionaries, lists, sets)

print('blue is', eng2sp['blue'])
for k in eng2sp:
    print(f'{k}:{eng2sp[k]}')

print()

while True:
    word = input('> ')
    if word == '':
        break
    elif word in eng2sp:
        print(f'the English word "{word}" is "{eng2sp[word]}" in Spanish.')
    else:
        eng2sp[word] = input(f'Enter the Spanish word for {word}: ')

print()

for k in eng2sp.keys():
    print(f'{k}: {eng2sp[k]}')

print()

for k, v in eng2sp.items():
    print(f'{k}: {v}')

numberDict = {}
for i in range(1,51):
    numberDict[i] = str(i)

for num in numberDict:
    print(num, numberDict[num])

print()

from timeit import timeit
print(timeit('''d[0]''', '''d = {i:i**2 for i in range(1000000)}'''))

print()

import string

with open('Frankenstein.txt', errors = 'ignore') as file:
    text = file.read()

text = text.translate(str.maketrans('', '', string.punctuation)).lower()
words = text.split()

d = {}
for word in words:
    if word in d:
        d[word]+=1
    else:
        d[word] = 1

""" ALTERNATE WAY:
def f(x):
    return x[1]

for word, count in sorted(d.items(), key=f):
    print(f'{word:20}:{count}')
"""

for word, count in sorted(d.items(), key=lambda x: x[1])[-20:]:
    print(f'{word:20}:{count}')
#lambda x => creating an inner function w/ no name
    #that takes in x that returns x[1]


print(timeit('''f(1)''', '''def f(x): return x''', number=10000000))
print(timeit('''f(1)''', '''f = lambda x: x''', number=10000000))









