'''marks = [90, 56, 80, 85]
print(sum(marks)/4)

# or in another hand

marks = [22, 90, 89, 97]
percentage = sum(marks)/4
print('you perentage is ',percentage)'''

# its long way to execute th eprogram for only knowledge

'''def avg(marks):
    return((marks[0] + marks[1] + marks[2] + marks[3])/2)

marks1 = [34, 55, 45, 90]
print(avg(marks1)) 

marks2 = [45, 89, 98, 67]
print(avg(marks2))'''

# and

'''def avg(t):
    return((t[0] + t[1] + t[2] + t[3])/2)

t1 = [465, 45, 4, 4]
print(avg(t1))

t2 = [45, 42, 9, 67]
print(avg(t2))'''

# for example\\

'''def asdf(name):
    print('good mornong!,' + name)

asdf('kisshore')'''

# default parameter value

'''def nm(enter='string'):
    print('good mornong!' + enter)
nm('kisshor')    
nm() ''' 

# Recursion()

'''i = int(input('enter the number:\n'))
prop = 1
for r in range(i):
    prop = prop * (r+1)
print(prop)'''

# another way


'''def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
f = factorial(8)
print(f)''' 

# practice

'''def max(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3    
    else:
        if(num2>num3):
            return num2
        else:
            return num3

a = max(45, 67, 84)
print('the value if maximum number' + str(a))'''

# 02 practice

'''def far(cel):
    return (cel *(9/5)) + 32

cel = 37
f = far(cel) 
print('your f temprature is' + str(f))'''

# 03 practice

'''print('hello! ', end=" ")
print('how', end=" ")
print('are', end=" ")
print('you', end=" ")'''

# 04 practice

'''def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 4

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))'''

# 05 practice

'''n = 3
for i in range(n):
    print('*' * (n-i))'''

# 06 practice

'''def box(string,word):
    asd = string.replace(word,"")
    return asd.strip()
this = '     what my name was      ' 
n = box(this, 'what')
print(n)''' 

# 07 practice

'''x = int(input('enter the number:\n'))
for m in range(1,11):
    print(f"{x}x{m} = {x*m}")'''

# 08 practice of game

'''import random
def game(wwe, c):
    if wwe == c:
        return None
    if wwe == 'w':
        if c == 'g':
            return ('you lose the game')
        elif c == 's':
            return ('you win')

    if wwe == 'g':
        if c == 's':
            return ('you lose the game')
        elif c == 'w':
            return ('you win') 

    if wwe == 's':
        if c == 'w':
            return ('you lose the game')
        elif c == 'g':
            return ('you win')                


print("computer turn: snake(s), water(w) or gun(g)")
randno = random.randint(1, 3)

if (randno == 1):
    wwe = 'w'
elif(randno == 2):
    wwe = 'g'
elif(randno == 3):
    wwe = 's'        

c = input("player turn: snake(s), water(w) or gun(g)")

a = game(wwe, c)

print(f"computer chooes,{wwe}")
print(f"player chooes,{c}")

if a == None:
    print('the game is tie')
elif a:
       print('you win the game')
else:
       print('you lose')'''        
