# while loop in python

'''i = 0
while i<=5:
    print('yes'+ str(i))
    i = i + 1'''

'''hh = 0
while hh<=50:
    print('checking' + str(hh))
    hh = hh + 5'''

'''name = ['sushant', 'dinesh', 'biswash', 'hatti', 'kisshor']
a = 0
while a<len(name):
    print(name[a])
    a = a + 1''' 

# for loops

'''obj = ['pluggin', 'house', 'fruit', 'water', 'machine']
for p in obj:
    print(p)'''

# range function in loop or python

'''for r in range(3 ,21): #we can also give starting num otherwise it starts from 0
    print(r) 

for r in range(3 ,21, 3): #we can also give step-size
    print(r)'''  

# for loop with else 

'''for g in range(1,5):
    print(g)
else:
    print('now! else statement is starting')'''

# breaking the loop   

'''for t in range(13):
    print(t)
    if (t == 5):
     break
else:                     #we can also use else 
    print('if there is break it will not occur')'''

# continuening the loop

'''for m in range(11):
    if(m == 9):
     continue
    print(m)'''

# pass statement(it does nothing)

'''w = 34
if w>34:
    pass
print('he is very intellectual',w)'''

# def yes(player):
#     pass

# reversing the number

'''w = int(input('enter your number :\n')) 
rev = 0
while w>0:
    rev = (rev*10) + w%10
    w = w//10
print('the reverse number is',rev)'''

# practice

'''num = int(input('enter the number'))
for w in range(1,11):
    print(f"{num}x{w}={num*w}")'''

    # both are same we use for better look only
'''print(str(num) + "x" + str(w) + '=' + str(w*num))
    print(str(w*num))'''

# 02 practice

'''names = ['hatta', 'hatti', 'hataru', 'motae', 'rangila']
for name in names:
    if name.startswith('ha'):
        print('hello! '+ name) '''

# 03 practice

'''num = int(input('enter the number:\n'))
prime = True
for s in range(2, num):
    if (num%s == 0):
        prime = False
        break

if prime:
    print('the given number is prime')
else:
    print('the given number is not prime')''' 

# 04 practice

'''num = int(input('enter the number:\n'))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"the factorial of {num} is {fact}")''' 

# 05 practice

'''n = 10
s = 0
m = 0
while n>s:
    s=s+1
    m=m+s
print("the sum of 10 natural number",m)'''

# 06 practice

'''n = 4
for i in range(4):
    print("*" * (i+1))''' 

# 07 practice

'''n = 0
for i in range(0,5,2):
    print("*" * (i+1))'''




