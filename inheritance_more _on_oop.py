#  INHERITANCE
# 01 single INHERITANCE

'''class worker:
    company = "microsoft"

    def show_details(self):
        print("you are an worker of microsoft")

class man(worker):
    brand = "boat"

    def getbrand(self):
        print(f"the language is {self.brand}")
    
    def show_details(self):
        print("you are an worker of boat")

w = worker()
w.show_details()
m = man()
m.show_details()'''

# 02 multiple inheritance

'''class Tires:
    company = "zomato"
    address = 'k gaun'

class Fastfood:
    company = "fastfood"
    gaun = 'guranspur'

    def box(self):
        print("the billiniore")

class quick(Tires,Fastfood):
    company = "daaraz"

q = quick()
print(q.company)
q.box()
print(q.gaun)'''

# 03 multi-level inheritance

'''class biodata:
    country = "india"

    def fox(self):
        print("the success of business is here")

class employee(biodata):
    company = "tata"

    def getsalary(self):
        print("your salary of the month is")
    def fox(self):
        print("I am, very happy today .......")

class program(employee):
    company = "reliance"

    def getsalary(self):
        print("no salary to the programmer")
     

b = biodata()
b.fox()
e = employee()
e.getsalary()
p = program()
p.getsalary()'''

# super inheritance method

'''class biodata:

    def __init__(self):
        print("your request is granted")

    country = "india"
    def getsalary(self):       
        print("i am a indian so i live in india")

    def fox(self):
        print("the success of business is here")

class employee(biodata):
    company = "tata"

    def __init__(self):
        super().__init__()
        print("you are in trouble ..........//")    

    def getsalary(self):
        super().getsalary()        
        print("your salary of the month is")
    def fox(self):
        print("I am, very happy today .......")

class program(employee):
    company = "reliance"

    def __init__(self):
        super().__init__()
        print("programming ..........//") 

    def getsalary(self):
        super().getsalary()
        print("no salary to the programmer")
     

b = biodata()
b.fox()

e = employee()
e.getsalary()

p = program()
p.getsalary()'''

# class inheritance

'''class rock:
    company = "infosis"
    location = "mumbai"
    salary = 90000

    @classmethod
    def change(self,salary):
        self.salary = salary

# another way to change the class attributes       

    def change(self,salary):
        self.__class__.salary = salary        

rj = rock()
rj.change(80999)
print(rj.salary)
print(rj.location)
print(rj.company)'''

# property decorator

'''class horse:
    company = "honda"
    salary = 80000
    bonus = 700

    @property 
    def totalsalary(self):
        return self.salary + self.bonus

    @totalsalary.setter
    def totalsalary(self, val):
        self.bonus = val - self.salary

fr = horse()
print(fr.totalsalary)
fr.totalsalary = 90000
print(fr.salary)
print(fr.bonus)'''

# operator overloading in python (it can be used by using __ method)
# important key terms


# p1 + p2 = __add__
# p1 - p2 = __sub__
# p1 * p2 = __mul__
# p1 / p2 = __truediv__
# p1 // p2 = __floordiv__

'''class number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print('i am busy today')
        return self.num + num2.num 

    def __mul__(self,num2):
        print('i am free today')
        return self.num * num2.num         

n1 = number(5)
n2 = number(7)

sum = n1 + n2
print(sum)

mul = n1 * n2
print(mul)'''

# using (__str__) and (__len__) in python

'''class number:
    def __init__(self,num):
        self.num = num

    def __str__(self):
        return f"the required number is {self.num}"
    def __len__(self):
        return 323               

n1 = number(5)
print(n1)
print(len(n1))'''

# practice

'''class c2dvector:
    def __init__(self, i, j):
        self.j = j
        self.i = i
    def __str__(self):
        return f"{self.i}i + {self.j}j"    

class c3dvector(c2dvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"            

v2d = c2dvector(1, 3)
v3d = c3dvector(4, 5, 6)
print(v2d)
print(v3d)'''

# 02 practice

'''class dog:
    def bark(self):
        print("BOW ! BOW!")

d = dog()
d.bark() '''

# 03 practice

'''class worker:
    salary = 9000
    tax = 25.6

    @property
    def final_salary(self):
        return self.salary*self.tax

    @final_salary.setter
    def final_salary(self,sai):
        self.tax = sai/self.salary

wr = worker()
print(wr.final_salary)

print(wr.tax)
wr.final_salary = 18000'''

# 04 practice

# (a+bi) (c+di) = (ac-bd) (ad+bc)

'''class uranium:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, c):
        return uranium (self.i + c.i , self.j + c.j)

    def __mul__(self, c):
        muli = self.i * c.i-self.j*c.j
        mulj = self.i * c.j+self.j*c.i
        return uranium (muli, mulj)

    def __str__(self):
        # if self.j<0:
        #     return f"{self.i} - {self.j}i"
        # else:
            return f"{self.i} + {self.j}i"


dog = uranium(3, 2)        
fog = uranium(1, 7)
print(dog + fog)
print(dog * fog)'''

# 05 practice

'''class vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)   

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum            

v1 = vector([1, 4]) 
v2 = vector([1, 6]) 
print(v1 + v2)               
print(v1 * v2)'''               

# 06 practice

'''class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"         

v1 = vector([1, 4, 6]) 
v2 = vector([1, 6, 9]) 
print(v1)               
print(v2)'''

# 07 practice
'''class vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)   

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)               

v1 = vector([1, 4, 8, 0]) 
v2 = vector([1, 6, 8]) 
print(len(v1))              
print(len(v2))'''


# project 002

'''import random
randnumber = random.randint(1, 10)
userguss = None
guesses = 0
while(userguss != randnumber):
    userguss = int(input("enter the guss number:"))
    guesses += 1

    if (userguss == randnumber):
        print("the number that you entered is actually right!")
    else:
        if(userguss>randnumber):
            print("the number that you entered is greater!, enter smaller one")
        else:
            print("the number is smaller so, please enter greater one")

print(f"you guessed the number in {guesses} guesses")'''

# with open("highscore.txt", "r")as f:
#     highscore = int(f.read())

# if (guesses<highscore):
#     print("you broke the record of highscore")
#     with open("highscore.txt", "w")as f:
#         f.write(str(guesses))    

















