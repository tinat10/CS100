import math

# is a perfect number (the sum of its divisors equal the number itself)

def perfect(n):
    total = 0;
    for i in range(1, int(n/2)+1): # use floor division n//2+1 to replace the int()
        if (n%i==0):
            total+=i
    return (total == n)
        
for i in range(1,10001):
    if perfect(i):
        print(i, end = " ")

print()

# find the sum of all primes less than 1,000

def prime(n):
    for i in range(2,n//2):
        if (n%i==0):
            return False;
    return True;

tot = 2
for i in range(3, 1001, 2):
    if prime(i):
        tot+=i
print(tot)

# largest palindrome number

biggest = 0;
for i in range(1, 1000): # to be faster you could start from 1000 and subtract 1
    for j in range(1, 1000):
        num = i*j
        if (str(num) == str(num)[::-1] and num > biggest):
            biggest = num
print(biggest)

# DID THIS INCORRECTLY! sum of numbers in fibonacci sequence up to 4,000,000

tot = 0
prevNum = 1
num = 1
while num <= 4000000:
    temp = prevNum + num
    tot+= temp
    prevNum = num
    num = temp

print(tot)

#










        

