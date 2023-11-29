'''
Tina Thai
CS100 2023 Section H11
HW 10, November 14, 2023
'''

# Problem 1
def initialLetterCount(wordList):
    dic = {}
    for word in wordList:
        if word[0] in dic:
            dic[word[0]]+=1
        else:
            dic[word[0]] = 1
    return dic

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'sally']
print(initialLetterCount(horton))
# {'I': 4, 's': 2, 'w': 2, 'm': 2, 'a': 1]

print()

# Problem 2
def initialLetters(wordList):
    dic = {}
    for word in wordList:
        if word[0] not in dic:
            dic[word[0]] = [word]
        elif word not in dic[word[0]]:
            dic[word[0]].append(word)
    return dic

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'Sally', 'sally']
print(initialLetters(horton))
# {'I': ['I'], 's': ['say'], 'w': ['what'], 'm': ['mean'], 'a': ['and']}

print()
   
# Problem 3
def shareOneLetter(wordList):
    dic = {}
    for word in wordList:
        for let in word:
            for word2 in wordList:
                if let in word2 and word not in dic:
                    dic[word] = [word2]
                elif let in word2 and word2 not in dic[word]:
                    dic[word].append(word2)
                
    return dic

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say', 'see']
print(shareOneLetter(horton))
'''{'I': ['I'], 'say': ['say', 'what', 'mean', 'and'], 'what': ['say', 'what', 'mean', 'and'], 'mean': ['say', 'what', 'mean', 'and'],
# 'and': ['say', 'what', 'mean', 'and']}'''

