#foreach loop
#for <var> in <sequence>:
#    <smth>

pets = {"cat", "dog", "bird", "fish", "hamster"}
for pet in pets:
    print(pet)

for ch in "abracadabra": # ch is char
    print(ch, end = " ")

print() # creates new line

for i in range(10): # obv starts from 0
    print(i, end = " ")

# print(pets, pets::-1)

days = ('m', 't', 'w', 'r', 'f', 's', 'u')
for day in days:
    print(day)
    
for num in range(11):
    print(num, end = " ")

print() # creates new line

for num in range(1, 10, 1):
    print(num, end = " ")

print() # creates new line

for num in range(0, 10, 2):
    print(num, end = " ")

print() # creates new line

for num in range(1, 10, 2):
    print(num, end = " ")

print() # creates new line

for num in range(10, 70, 10):
    print(num, end = " ")

print() # creates new line

names = ["tina", "alyssa", "katie", "angie"]
for name in names:
    if (name == "katie"):
        name = "katherine"

#doesn't change the list because this for loop is just a foreach loop in disguise

for name in names:
    print(name)

i = 0
while i < len(names):  # len is length
    if (names[i] == "katie"):
        print("hi katie")
        #names[i] = "katherine"
    print(i, names[i])
    i+=1

print(names)

while True:
    cmd = input('> ') #cmd == command
    if cmd == '':
        break
    print(cmd)
