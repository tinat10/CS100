'''
Tina Thai
CS100 2023 Section H11
HW 09, November 02, 2023
'''

# Problem 1
def file_copy(in_file, out_file):
    original = open(in_file, 'r')
    clone = open(out_file, 'w')
    for line in original:
        clone.write(line)

    clone.close()
    original.close()

file_copy('HW9_Text1.txt', 'HW9_Text2.txt')
copy = open('HW9_Text2.txt')
print(copy.read())

print()

# Problem 2
def file_stats(in_file):
    words, chars = 0, 0
    file = open(in_file)
    lines = file.readlines()
    print(type(lines))
    for line in lines:
        chars+= len(line)
        words+=len(line.split())
    
    print('lines', len(lines), '\nwords', words, '\ncharacters', chars)

file_stats('HW9_Text2.txt')

print()

# Problem 3
import string

def repeat_words(in_file, out_file):
    oldFile = open(in_file)
    newFile = open(out_file, 'w')

    for line in oldFile.readlines():
        repeats = []
        line = line.translate(str.maketrans('','', string.punctuation)) 
        words = line.lower().split()
        for word in words:
            if words.count(word) > 1 and word not in repeats:
                repeats.append(word)

        for rep in repeats:
            newFile.write(rep + ' ')
        newFile.write('\n')

repeat_words('HW9_problem3.txt', 'newFile.txt')
file = open('newFile.txt')
print(file.read())

























