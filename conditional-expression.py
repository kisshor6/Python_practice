# if-elif-else ladder in python

'''a = 70.9
if(a<18):
    print('you cannot go ahead')
elif(a==80):
    print('you may processed')
elif(a == 18):
    print('you may processed') 
elif(a>80):
    print('you cannot go ahead')   
else:
    print('sorry!')'''  

    # in another hand

'''a = 9
if(a<18):
    print('you cannot go ahead')
if(a==80):
    print('you may processed')
if(a == 18):
    print('you may processed') 
if(a>80):
    print('you cannot go ahead')   #only this executive
else:
    print('sorry!')'''


# age = int(input('enter your age:\n'))
# if(age >= 18):
#     print('yes')
# else:
#     print('no')  

# logical operators like and, or, 

'''age = int(input('enter your age:\n'))
if(age>18 and age<45):
    print('welcome! you can work with us')
else:
    print('sorry! you are rejected')'''  


'''age = int(input('enter your age:\n'))
if(age==20 or age<20):
    print('welcome! you can work with us')
else:
    print('sorry! you are rejected')''' 

# a = [3, 234, 234, 54, 90]
# print(0 in a)

# asd = None
# if(asd is None):
#     print('true')
# else:
#     print('false') 


# practice 

'''num1 = int(input('enter the number1:\n'))
num2 = int(input('enter the number2:\n'))
num3 = int(input('enter the number3:\n'))
num4 = int(input('enter the number4:\n'))

if(num1>num2):
    f1 = num1
else:
    f1 = num2 

if(num3>num4):
    f2 = num3
else:
    f2= num4

if(f1>f2):
    print(str(f1) + 'is greatest number')
else:
    print(str(f2) + 'is greater number')'''

# 02 practice

'''sub1 = int(input('enter your first subject marks :\n'))                   
sub2 = int(input('enter your second subject marks :\n'))                   
sub3 = int(input('enter your third subject marks :\n'))                   
sub4 = int(input('enter your forth :\n subject marks :\n'))

if(sub1<33 or sub2<33 or sub3<33 or sub4<33):
    print('you are faled')
elif(sub1+sub2+sub3+sub4)/4 < 40:
    print('you have been failed')
else:
    print('congratulation! you have been passed')'''        

# 03 practice

'''comet = input('enter your text:\n')
if('hatti' in comet):
    chhichore = True

elif('kevim' in comet):
    chhichore = True

elif('sushant' in comet):
    chhichore = True

elif('dinesh' in comet):
    chhichore = True

else:
    chhichore = False

if(chhichore):
    print('he is absoutly chhichore') 
else:
    print('he is not chhochore')''' 

# 04 practice

'''names = ['sushant', 'hatti', 'dinesh', 'chaudari', 'kisshor']
name = input('enter your name\n')
if(name in names):
    print('your name is present')
else:
    print('your name isnot present')''' 

# 05 practice

'''marks = int(input('enter your marks'))
if(marks>=90):
    grade = "A+"
elif(marks>=80):
    grade = "A"         
elif(marks>=70):
    grade = "B+"
elif(marks>=60):
    grade = "B"
elif(marks>=50):
    grade = "C+"
else:
    grade = "failed"

print('your grade is' + grade)''' 

# 06 practice

'''namw = 'dineshpunmagar'

if(len(namw)) >= 10:
    print('true')
else:
    print('false')''' 

# 07 practice

'''name = ['harry','HARRY','HaRRy', 'haRRy','harrY']

if('harry' in name):
    print('yes')
else:
    print('no')'''

