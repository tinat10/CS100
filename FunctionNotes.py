#def <functName>(<param>):
#    <body>

def twice(x):
    return 2 * x

def thrice(x):
    y = 3 * x
    return y

#<functName>(<args>)
print(twice(5))
print(thrice(5))

print()

a = (int)(input())
b = twice(a)
print("number:", a, "* 2 =", b)
print()


def empty(x):
    x = 2
print(empty(2)) #b/c it returns nothing (like a void method), it will print "None"

#^^ is similar to doing this
print(print("hiiii"))

print()

def docString():
    '''this is a doc string. tells us what this function does'''
    print('a docstring is typically in triple quotations')

def oddCount(nums):
    '''returns the number of odd numbers in the list'''
    count = 0
    for num in nums:
        if num%2: # in python, 1 is true and 0 is false → u can write as num%2==0 though
            count+=1
    return count

numbers = [2, 5, 2, 1, 4 ,6]
print(oddCount(numbers))

help(docString)
help(oddCount)

