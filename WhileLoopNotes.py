while True:
    cmd = input('> ')
    if cmd == "":
        break
    print(cmd)

print()

print('while: ')
#in a while loop you need:
i = 0                    # initialization of variable
while i < 10:            # conditional
    print(i, end = " ")  # body
    i += 1               # incrementor

print()    
print("for: ")
for i in range(0,10):
    print(i, end = " ")

print()
print()
def getNegativeNumber():
    while True:
        num = input('give me negative number: ')
        if (int(num) < 0):
            return num
        
print('neg number:', getNegativeNumber())

def fibo(n):
    a, b = 0, 1
    while a <= n:
        a, b = b, a+b
    return a

print(fibo(10))
    
print('continue')
i = 0
while i<10:
    if i==5:
666666666        continue
    print(i)
    i+=1
