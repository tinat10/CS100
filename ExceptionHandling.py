#loop won't end till it can open a valid file
#just type in ExceptionHandling.py
while True:
    try:
        file = open(input('fileName: '))
        break
    except:
        print('Invalid file.')

file.close()

'''
try:
    <dangerous code>
except:
    <error alert statement>
'''

#if user inputs 0, there will be an error
while True:
    try:
        n = int(input("Num: "))
        print(1/n)
        break;
    #except (ValueError, ZeroDivisionError):
        #print("Invalid")
    except Exception as e:
        print(e)
    else:
        print('else')

# with open(input()) as fin, open(input(), 'w') as fount:

def process_file(filename):
    try:
        fin = open(filename)
    except:
        return
    finally:
        print('last')
    for lin in fin:
        pass
    fin.close()
    
    

