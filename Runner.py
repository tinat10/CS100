def myFunction(x):
    result = x**2
    return "result is: ", result, 5

print(myFunction(2))
#returns a tuple when more than one type of variable is returned

print('\\n has a length of', len('\n'))
def myFunction(aStr):
    return len(aStr)

s = 'my cat is catatonic\n\n'
print(myFunction(s))
# \n has a length of 1

ifile = open('HW9_Text1.txt', 'r')
print(ifile.read(5))
print(type(ifile.readline()))
print(type(ifile.readlines()))
ifile.close()
# readline() returns type string while readlines() returns a list of strings

def makeIndex(pageList):
    wordIndex = {}
    for item in pageList:
        word = item[0]
        page = item[1]
        if word not in wordIndex:
            wordIndex[word] = [page]
        else:
            wordIndex[word].append(page)
    return wordIndex

wordOccurences = [('rabbit', 1), ('alice', 1), ('rabbit', 4), ('alice', 7), ('alice', 10)]
print(makeIndex(wordOccurences))

