# 01-some input methods of dictionary

'''dict = {
    "computer" : "a smart machine",
    "home" : "a homestay of human being",
    'marks' : [3, 5, 6, 9.7],
    'another' : {'wood' : 'a furniture tool'}
}
print(dict["computer"])
print(dict['home'])
# dict['marks'] = [232, 42, 2, 0]
print(dict['marks'])
print(dict['another']['wood'])
print(type(dict))'''

# 02-methods of dictionary  1.type

'''oxford = {
    'asis' : 'smart',
    'sushant' : 'handsome',
    'hatta': 'nabin',
    32 : 989,
    'dins' : {'dabba': 'honest and good'}
}
print(oxford.keys()) #print the keys of oxford(dictionary)
print(oxford.values()) #print the values of oxford(dictionary)
print(oxford.items()) #print the items(values and items) of oxford(dictionary)'''

# to updae anything afer the code (up = down)code

'''print(oxford)
a = {
    'dasd' : 'movie',
    'jkl' : 'cinema',
    'asdf' : 'film',
    'asis' : 'great'  # it update if the value is same
}
oxford.update(a)
print(oxford)'''

# same (up = down)code
# it work as same if the content found

'''print(oxford.get('hatta2423'))   #it shows none on screen if value not found
print(oxford['hatta2423'])        #it shows error on screen if value not found'''

# sets in python

'''a = {3, 11, 456, 3433, 3} #it cannot repeat same element again
print(a)
print(type(a))'''

# creating an empty set

'''a = {} # it is not a empty set it is empty dictionary 
print(type(a))

b = set() # it is a empty set
print(type(b))'''

# adding the value and using len, pop,remove and clear on set

'''b = set()
print(type(b))

b.add(213) # adding value on set
b.add(32)
b.add(3)
b.add(23)
b.add((0, 3, 564, 4)) # it cannot support list or dictionary
print(b)

print(len(b))
b.remove(213)
print(b.pop())
print(b)
print(b.clear())'''

# practice

'''dict = {
    'cpu' : 'component of computer',
    'hdd' : 'memory of computer',
    'ssd' : 'modern way to store data',
    'fan' : 'cooling agent of cpu',
    'speaker' : 'output device which gives sound'
}
print('choose any one option',dict.keys())
a = input('enter your words\n')
print('the meaning of your words is',dict.get(a))'''

# 02 practice

'''num1 = int(input('enter your number\n'))
num2 = int(input('enter your number\n'))
num3 = int(input('enter your number\n'))
num4 = int(input('enter your number\n'))
num5 = int(input('enter your number\n'))
a = {num1, num2, num3, num4,num5}
print(a)'''

# 03 practice

'''s = {34, '34', 435.45, True, None}
print(s)'''

# 04 practice

'''a = set()
a.add(20)
a.add(20.0)
a.add('20')
print(a)
print(len(a))'''

# 05 practice

'''favdict = {}
a = input('enter your favourite language hatti\n')
b = input('enter your favourite language hatta\n')
c = input('enter your favourite language aaasdk\n')
d = input('enter your favourite language hari\n')
e = input('enter your favourite language chowk\n')

favdict['hatta'] = a
favdict['hatti'] = b
favdict['aaasdk'] = c
favdict['hari'] = d
favdict['chowk'] = e

print(favdict)'''