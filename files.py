'''f = open('firefox,text') # by default the mode is automatically read, for write we use 'w'
print(f.read(20)) # it reads the the file according ti given number otherwise it read all characters 
f.close()'''

# another method to read the file


'''f = open('firefox,text')
# read first line
print(f.readline())
# read second line
print(f.readline())
#read thoed line and so on according to the line in file
print(f.readline())
f.close()'''

# writing the file

'''f = open("kisshor.txt", 'w')  # it creates the new file  
print(f.write('please go ahead you may processed'))
f.close()'''

# appending the file

'''f = open('firefox,text','a')
print(f.write('this is appinding text'))
f.close()'''

# opening file with (with) statement

'''with open('firefox,text', 'r') as f:
    print(f.read())''' # not nrcessary to close the file

# now practice set 

'''with open('firefox,text', 'r') as f:
    if 'twinkle' in f:
        print('yes,you are right')
    else:
        print('sorry , you are wrong')    

    print(f.read())'''

# 02 practice

''''def game():
    return 446
score = game()
with open('firefox,text') as f:
    highscore = int(f.read())
     

if highscore<score:
    with open('firefox,text', 'w')as f:
        f.write(str(score))'''

# 02 (ii) practice // when highscore is blank

'''def game():
    return 446
score = game()
with open('firefox,text') as f:
    highscore = f.read()

if highscore == '':
       with open('firefox,text', 'w')as f:
        f.write(str(score))   

elif int(highscore)<score :
    with open('firefox,text', 'w')as f:
        f.write(str(score))'''

# 03 practice 

'''with open('firefox,text') as f:
    content = f.read()
content = content.replace('donkey', '******')
with open('firefox,text','w') as f:
    content = f.write(content)''' 

# 04 practice

'''words = ['chuk', 'rangila', 'mota', 'hattti']
with open('firefox,text') as f:
    content = f.read()

for word in words:    
    content = content.replace(word, '******')
with open('firefox,text','w') as f:
    content = f.write(content)'''             

# 05 practice

'''with open('firefox,text','r')as f:
    content = f.read()

if 'Python' in content:
    print('yes! python is found in it')
else:
    print('sorry! it not found')''' 

# 06 practice// up code = down

'''content = True
i = 1
with open('firefox,text') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print('yes! it is found')
            print(i)
        i+= 1''' 

# 07 practice program to copy the content of file in another file

'''with open('firefox,text') as f:
    content = f.read()

with open('kissor.txt','w')as f:
    f.write(content)'''

# o8 practice

'''f1 = 'firefox,txt'
f2 = 'kissor.text'

with open('firefox,text')as f:
    f1 = f.read()

with open('kissor.txt')as f:
    f2 = f.read()

if f1 == f2:
    print('file found and matched')
else:
    print('sorrry error found')'''            

# 09 practice to wipe the file or clear

'''with open('kissor.txt', 'w')as f:
    f.write("")'''

# 10 practice to rename the file  

'''import os
with open('firefox,text')as f:
    son = f.read()
with open('kir.txt', 'w')as f:
    f.write(son) 
os.remove('firefox,text')'''         


'''important key terms'''

# 'rb' will open for read in binary mode
# 'r+' will open for read in text mode