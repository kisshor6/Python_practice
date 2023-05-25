'''class Books:
    def set_pic(self):
        print('i am reading boooks')

b1 = Books()
b1.set_pic()'''

# class attributes// it directly associated with class

'''class empl:
    company = 'microsoft'
kisshor = empl()    
asdf = empl()

print(kisshor.company)    
print(asdf.company)

empl.company = 'apple'

print(kisshor.company)    
print(asdf.company)'''

# isinstance attributes//given attribute get more priority

'''class salary:
    company = 'google'
    income = 40000
kissho = salary()
vivek = salary()

kissho.income = 90000

print(kissho.income)
print(vivek.income)'''

# another way to make program by self attributes

'''class lion:
    company = 'tata'
    def mysalary(self):
        print(f"the salary of employee working in {self.company}is{self.salary}")
        
kisshor = lion()
kisshor.salary = 89000
kisshor.mysalary()'''

# by using static method\\ it is not necessary to write (self)

'''class lion:
    company = 'tata'
    @staticmethod
    def mysalary():
        print("the salary of employee working in")
        
kisshor = lion()
kisshor.mysalary()'''

# __init__ (consructor)

'''class Worker:
    def __init__(self,name,salary,carname):
        self.name = name
        self.salary = salary
        self.carname = carname
        print('your biodata is passad')
    def show_details(self):
        print(f"the name of your worker is {self.name}")    
        print(f"the salary of your worker is {self.salary}")    
        print(f"the carname of your worker is {self.carname}")    

jkl = Worker('kisshor', 5000, 'lamourgini')
jkl.show_details()'''

# 01 practice set

'''class employee:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def show_details(self):
        print(f"the address of {self.name} is {self.address}")    

kissho = employee('arjit', 'washington dc')
kisshor = employee('radha', 'krukshetra')
kissho.show_details()
kisshor.show_details()'''

# 02 practice

'''class calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"the square of {self.num} is {self.num **2}")

    def cube(self):
        print(f"the cube of {self.num} is {self.num **3}")

    def squareroot(self):
        print(f"the squareroot of {self.num} is {self.num **0.5}")

cal = calculator(3)
cal.square()
cal.squareroot()
cal.cube()'''

# 04 practice

'''class sample:
    a  = "kissor"

obj = sample()
obj.a = "vivek"

print(sample.a)
print(obj.a)'''

# 05 practice

'''class monkey:
    @staticmethod
    def huss():
        print("hello! welcome to the our institute")
hatta = monkey()
hatta.huss()'''

# 06 practice

'''class train:
    def __init__(self,name, time, seat):
        self.name = name
        self.time = time
        self.seat = seat

    def show_details(self):
        print(f"the name of train is {self.name}")
        print(f"the time of train is {self.time}")
        print(f"the seats in train are {self.seat}")

    def book(self):
        if(self.seat>0):
            print(f"your ticket has been booked and your seat number is {self.seat}")
            self.seat = self.seat - 1
        else:
            print("sorry! all seats are full")        

data = train('mumbai express', '6:00 AM', 987)
data.show_details()
data.book()
data.show_details()'''

# 07 practice

'''class Gemo:
    def __init__(self,name):
        self.name = name
bag = Gemo('kisshor')
print(bag.name)'''           

