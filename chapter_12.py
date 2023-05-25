# method to protect program from being crash

'''while (True):
    print('print q to quit')
    a = input('enter the number\n')
    if a == 'q':
        break
    try:
        a = int(a)
        if a>6:
            print('the number that you entered is greater than 6')
    except Exception as e:
        print(f"your input resulted error: {e}")        
print('thanks for running code....')''' 

# adding multiple exceptions
'''try:
    a = int(input('enter the number'))
    c = 1/a
    print(c)

except ZeroDivisionError as e:
    print('make sure that you are not dividing by 0')
    print(e)

except ValueError as e:
    print('invalid syntex')
    print(e)

except TypeError as e:
    print('invalid type')
    print(e) '''   

print('this is the finishing point')

# raising Exceptions

'''def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError('the value will be invalid')    
a = increment(34)
print(a)'''

# try with else

'''try:
    a = int(input('enter the number'))
    c = 1/a
except Exception as e:
    print(e)
else:
    print('you are successful')'''

# try with finally (it works whether if program will fail or quit or any error occur)

'''try:
    a = int(input('enter the number'))
    c = 1/a
except Exception as e:
    print(e)
finally:
    print('almost done')'''

# introducing the file __name__== "__main__"    

'''def greet(name):
    print(f"good morning !! {name}")

if __name__ == "__main__":
    n = input("enter the name:\n")
    greet(n)'''

# global-local keywords

'''a = 45 #gloal variable
def fun1():
    global a
    print(f"print statement:1 {a}")
    a = 99 #local variable 
    print(f"print statement:2 {a}")
fun1()
print(f"print statement:3 {a}")'''

# enumerate function

'''list1 = [32, 53.34, 'kishor', True]
# x  = 0
# for item in list1:
#     print(x, item)
#     x += 1
for x, item in enumerate(list1):
    print(x, item)'''

# list comprehensions

'''a = [43, 5, 3, 6, 90, 12, 345, 67, 34]
# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)
# print(b)        
b = [i for i in a if i%2==0]
print(b)'''

# set comprehensions

'''a = [2, 1, 3, 9, 1, 3, 2]
s = {i for i in a}
print(s)'''

# 01 practice

'''def openfile(filename):
    try:
        with open(filename,'r')as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} is not found")


openfile("hat.txt")
openfile("hatti.txt")
openfile("maxim.txt")'''

# 02 practice

'''l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item,x in enumerate(l):
    if x == 2 or x == 4 or x == 8:
        print(x,item)'''

# 03 practice

'''num = int(input("enter your number:\n"))
table = [num*i for i in range(1,11)]
print(table)'''

# 04 practice

'''a = int(input("enter the number:\n"))
b = int(input("enter the number:\n"))
try:
     if a%b == 0:
         print("the program is execute")
except:
    print("make sure that the num is not divided by 0")'''    

# 05 practice

'''num = int(input("enter your number:\n"))
table = [num*i for i in range(1,11)]
print(table)
with open("tables.txt","a")as f:
    f.write(str(table))
    f.write('\n')'''
    

















