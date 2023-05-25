# we can also change the value
'''a = [8, 54, 874, 54, 64,]
a[0] = 56
a[2] = 36
a[4] = 63
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])'''

# we can also use this type of words 

'''a = [35, "rowdy", 32.32, True, None]
a[0] = 4243252345
a[2] = 4242345
a[4] = 4245
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])'''

# we can also slice into many pieces

'''a = [35, "rowdy", 32.32, True, None]
print(a[-3:-1])
print(a[1:3])'''

# sort, reverse, append, insert, pop, remove

'''name = [21, 98, 5, 1, 20]
name.sort()
print(name)

li = [90, 2, 234, 9, 34]
li.reverse()
print(li)

cast = [90, 2, 234, 9, 34]
cast.append(32)
print(cast)

cast = [90, 2, 234, 9, 34]
cast.insert(3, 0)
print(cast)

cast = [90, 2, 234, 9, 34]
cast.pop(3)
print(cast)

cast = [90, 2, 234, 9, 34]
cast.remove(90)
print(cast)'''

# we can also use string in its form

'''cast = ["sushant", "dinesh", "ishant", "ashiq", "khappad"]
cast.sort()
print(cast)'''

# now,tuples  it never be changed

'''t = (1, 2, 5, 10)
print(t)

t1 = (1,)
print(t1)'''

# tuple methods

'''t = (4, 43, 34, 6, 76, 46, 4)
print(t.count(4))
print(t.index(6))'''

# practice

'''f1 = input("enter the fruit f1:\n")
f2 = input("enter the fruit f2:\n")
f3 = input("enter the fruit f3:\n")
f4 = input("enter the fruit f4:\n")
f5 = input("enter the fruit f5:\n")

fname = [f1, f2, f3, f4, f5]
print(fname)'''

# next practice set

'''m1 = int(input("marks of student m1:\n"))
m2 = int(input("marks of student m2:\n"))
m3 = int(input("marks of student m3:\n"))
m4 = int(input("marks of student m4:\n"))
m5 = int(input("marks of student m5:\n"))

marks = [m1, m2, m3, m4, m5]
marks.sort()
print(marks)'''

# a = [3, 32, 345, 43]
# print(sum(a))

# t = [3, 0, 2, 0, 43, 0]
# print(t.count(0))