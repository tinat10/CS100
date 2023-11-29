# 4 different methods to read and print a file

fin = open('readingfile.py')
for line in fin:
    print(line, end = '')

fin.close()

print('____________________________________________________________________')

with open ('readingfile.py') as fin:
    print(fin.read())

print('____________________________________________________________________')

with open ('readingfile.py') as fin:
    lines = fin.readlines()

for line in lines:
    print(line, end = '')

print('____________________________________________________________________')

with open ('readingfile.py') as fin:
    while (line := fin.readline()) != '':
        print(line, end = '')
        
print('____________________________________________________________________')

# printing online txt file through web link

from urllib.request import urlopen

#with urlopen('https://www.gutenberg.org/cache/epub/41445/pg41445.txt') as fin:
    #for line in fin:
        #print(line.decode(), end='')
