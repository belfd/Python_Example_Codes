"""
Python Quick Reference - edited in GitHub

 In python , the source code is compiled to a much simpler form called bytecode .
 The bytecode instructions are similar to the CPU instructions but are executed by a virtual machine .

 Searching in a list can be considerably slow as compared to a dictionary.
 The effect is even more pronounced , when the size of elements to search increases .
 As a fact, using a dictionary is over 100,000x faster than using a list if the search is on 10 million items.
 The reason is simple , the list uses iterative method to search for an element while a dictionary uses a hash lookup.

 A Metaclass in Python is a class of a class that defines how a class behaves.
 A class is itself an instance of a metaclass.
 A class in Python defines how the instance of the class will behave.

 The Dataclass module was introduced as a utility tool to make structured classes specially for storing data.
 These classes hold certain properties and functions to deal specifically with the data
 and its representation. Two instances of a dataclass having the same content will be equal to each other ,
 while two instances of a normal class will be not equal to each other as the equality operator
 checks the address in this case.
"""

### CHECK PYTHON VERSION ### do verifications for customer version awareness
import sys

if sys.version_info < (3, 5):
    print(f"Dear customer you are running old python")
print(f"Python version is: {sys.version_info}")

### IMPORTS ####
print("IMPORTS")
# 'generic import' of math module
import math

math.sqrt(25)

# import a function
from math import sqrt

sqrt(25)  # no longer have to reference the module

# import multiple functions at once
from math import cos, floor

# import all functions in a module (generally discouraged)
from csv import *

# define an alias
import datetime as dt

print(dt.date.today())
# show all functions in math module
# print(dir(math))
# show help on math module
# help(math)

# define an alias to specific func from module
from math import sqrt as sq

print(f"sqrt(81) is {sq(81)}")


# PLACEHOLDER - a placeholder in a function that you haven’t implemented
def func():
    pass


def func1():
    ...


# INPUTS
print("================")
print("INPUTS")
print("Multiple User input")

# normal way
# a = input("Enter name: ")
# b = input("Enter age: ")
# Better way
# a, b = input("Enter name and age: ").split()


# VARIABLES
print("===============")
print("VARIABLES")

# all variables/functions/class instances etc - are objects!!!
# Variables are pointer to address in memory - they hold the address in memory not actually the value
# addresses of objects can be revealed by function id()
# Each assignment to a var changes the reference even if you do my_var = ny_var+5 it means my_var is now pointing to new
# address in memory
a = 10
print(hex(id(a)))  # HEX address where a points to: 0x7ffc9daab470
b = a
print(hex(id(b)))  # HEX address where a points to: 0x7ffc9daab470 the same address!!!
a = 5  # Now the a variable is pointing to other place
print(hex(id(a)))  # output: 0x7ffcaea1b3d0 meaning the assignment moved var a from pointing to place of 10
# to new place of 5
print(f"b is {b}")  # output: b is 10 because the assignment still to 10 in memory
b = b + 5  # b is now 15 meaning value changed - it means b is now pointing to other place
print(hex(id(b)))  # HEX address where a points to: 0x7ffcaea1b510 a different address.
### values of integer -5 till 256 will point always to same variables
k1 = 2
k2 = 2
print(f"k1 is k2: {k1 is k2} because k1 id is: {id(k1)} and it equal to id of: {id(k2)}")

### DATA TYPES ###
print("===============")
print("DATA TYPES")
# determine the type of an object
type(2)  # returns 'int'
type(2.0)  # returns 'float'
type('two')  # returns 'str'
type(True)  # returns 'bool'
type(None)  # returns 'NoneType'

# python is dynamic typed - var as pointer(reference) to address type is according to what is been pointed to
a = 10
print(f"type of a is: {type(a)} and its val is {a}")
a = "Hello"
print(f"type of a is: {type(a)}  and its val is {a}")

# check if an object is of a given type
isinstance(2.0, int)  # returns False
isinstance(2.0, (int, float))  # returns True

# convert an object to a given type
float(2)
int(2.9)
str(2.9)

# zero, None, and empty containers are converted to False
bool(0)
bool(None)
bool('')  # empty string
bool([])  # empty list
bool({})  # empty dictionary

# non-empty containers and non-zeros are converted to True
bool(2)
bool('two')
bool([2])

# Object that can be changed internally (its state = its data) is called mutable
# Object that can NOT be changed internally (its state = its data) is called immutable
# Numbers (int,float,Boolean),string,tuple,Frozen set,user defined classes are *immutables!*
# list,set,dictionary,user defined classes are *mutables!*

# Notice: t is tuple of list a and b it means it is immutable but a and b are mutable,
# you cannot add new element to t but you can change the element in a and b inside the t
a = [1, 2]
b = [5, 6]
t = (a, b)
# t = (a,b,1) #Error - t tuple is immutable
t[0].append(3)
t[1].append(7)
print(f"t now is : {t}")  # t now is : ([1, 2, 3], [5, 6, 7])


def func(inp):
    inp = inp + ' World!'
    print(f"inside func my_val is: {inp}")  # inp = "Hello World!
    return inp


my_val = "Hello"
func(my_val)
print(f"Outside val of my_val is {my_val}")  # my_val is: Hello   --> because string is immutable!

c = 7
print(f"address of c is {hex(id(c))}")  # output: 0x7ffcaea1b410
d = 7
print(f"address of d is {hex(id(d))}")  # output: 0x7ffcaea1b410 the same address - python is clever to point
# to the same address because integer is immutable - it will not change! But if values are large like 500 address are
# different
# when trying to do modification to integer it is actually pointing to new address with other value
a = [1, 2, 3]
print(f"address of a is {hex(id(a))}")  # output: 0x2484852fb88
b = [1, 2, 3]
print(f"address of b is {hex(id(b))}")  # output: 0x2484852fbc8 meaning -
# python memory for mutable types uses different address.
c = b
print(f"address of c is {hex(id(c))}")  # output: 0x2484852fbc8 meaning - in this case same address is shared
c.append(100)  # will cause c to add 100 to list and also b to add 100
print(f"b val is: {b}")  # output: b val is: [1, 2, 3, 100]

#### Mutable and Imutable Explained ####
print("Mutable and Imutable Explained")
print("==============================")
'''
the mutable objects can be changed after creation. The immutable objects cannot be changed after creation. 
Let’s check it out by two examples:
leaders = ["Elon Mask"]
print(leaders, id(leaders))
# ['Elon Mask'] 140700341254336
leaders.append("Dan Belfer")
print(leaders, id(leaders))  # Same id
# ['Elon Mask', 'Dan Belfer'] 140700341254336

if we changed the leaders list, its content will be changed but its identity won’t be changed. 
Because the list object in Python is mutable, we can do the in-place modifications on it.

Leader = "dan"
print(Leader, id(Leader))
# dan 139713044786288

Leader.capitalize()
print(Leader, id(Leader))  # the Leader itself wasn't changed
# dan 139713044786288

### since a string is an immutable object in Python, we can not change anything on it, 
### even just capitalize its first letter. 
### We must assign the result of Leader.capitalize() to a new string.
Cap_Leader = Leader.capitalize()
print(Cap_Leader, id(Cap_Leader))
# Dan 139713044502768

list/Dict/Set are mutable (can be modified after initialized) all rest(tuple,string,number...) cannot be modified.
The '=' will create new object and label will be attached to the new object.
**Everything in Python is an object and the assignment operation is just binding a name to an object**

leaders = ["Elon Mask"]
print(leaders, id(leaders))
# ['Elon Mask'] 140009549940864
leaders.append("Dan Belfer")
print(leaders, id(leaders))  # Same id
# ['Elon Mask', 'Dan Belfer'] 140009549940864
leaders = ["Mark Zuckerberg"]
print(leaders, id(leaders))  # the id changed!
# ['Mark Zuckerberg'] 140009549461184

## The ["Mark Zuckerberg"] is another list object, and the name leaders will be bound to this object 
## when we run leaders = ["Mark Zuckerberg"].
## Due to the name leaders has already represented another object, it’s id is different.

A = ["Elon", "Dan"]
B = A
print(B, A)            # ['Elon', 'Dan'] ['Elon', 'Dan']
print(id(B) == id(A))  # True



B.append("Mark")  # 'append' modifies the list itself 
print(B, A)             # ['Elon', 'Dan', 'Mark'] ['Elon', 'Dan', 'Mark']
print(id(B) == id(A))   # True

B = ["Mark"]   # the '=' attach name to new object
print(B, A)             # ['Mark'] ['Elon', 'Yang', 'Mark']
print(id(B) == id(A))   # False

## As the above example shown, when B and A are bound to the same object, 
## changing B will affect A as well. When B is bound to another object, changing B won’t affect A at all.

How Objects are Passed to Functions?? Python is neither call-by-value nor call-by-reference. 
** It is call-by-sharing (also known as “call-by-object” or “call-by-object-sharing”). **

Why immutable objects are not call-by-value?
def updateNumber(val):
    val += 10
    print(val)
    
b = 5
updateNumber(b)  # 15
print(b)         # 5

BUT:
def updateNumber(val):
    print(id(val)) # 10055680

b = 5
print(id(b))  # 10055680
updateNumber(b)  # 10055680

## the val is another name besides b which is bound to the integer object 5. 
## The two names have identical ids since they are bound to the same object. 
## If we change the integer, because of its immutability, 
## a new integer object will be created and the val will be bound to it.

Why mutable objects are not call-by-reference?

L = [1, 2, 3]

def func(vals):
    vals.append(4)
    print(vals)

func(L)  # [1, 2, 3, 4] 
print(L) # [1, 2, 3, 4]

## As demonstrated above, appending a new value to the val will affect the L as well. 
## It acts like call-by-reference.

BUT:
L = [1, 2, 3]

def func(vals):
    vals = [7, 8, 9]  ## the assignment '=' bind vals name to the list [7,8,9]
    print(vals)

func(L)  # [7, 8, 9] 
print(L) # [1, 2, 3]

## after the 'vals' = [7,8,9] was executed, the name 'vals' had been bound to another list object — [7,8,9]. 
## Since the 'vals' and 'L' were bound to different list objects, the modification of 'vals' would not affect 'L'.

Be Aware of the Mutability of Nested Objects
# we should know that the mutability of nested objects depends on each object itself. For instance:

tp = ([1, 2, 3], 4, 5)
tp[0].append(4)
print(tp)  # ([1, 2, 3, 4], 4, 5)

# The tp is a tuple which is immutable, but the first element of tp is a list that is mutable. 
# Therefore, we can modify the first element of tp even if it’s an immutable object.
'''


### F-STRING ###
print("===============")
print("F-STRING PRINTING")

import datetime

now = datetime.datetime.now()
val = 12.3
a = 300

print(f'{now:%Y-%m-%d %H:%M}')  # output: 2021-02-10 12:17
print(f'{val:.2f}')  # output: 12.30
print(f'{val:.5f}')  # output: 12.30000
for x in range(1, 11):
    print(f'{x:02} {x * x:3} {x * x * x:4}')  # first output: 01   1    1
# hexadecimal
print(f"{a:x}")  # output: 12c
# octal
print(f"{a:o}")  # output: 454
# scientific
print(f"{a:e}")  # output: 3.000000e+02

# To ease read of large numbers:
val = 10000000000000000
print(f"{val:_}")  # output: 10_000_000_000_000_000
print(f"{val:,}")  # output: 10,000,000,000,000,000

'''
f-strings can also be used to self-document code using the = character.
What this means in practice is that when you’re printing a variable’s value to the console, 
you no longer need to write f"variable_name = {variable_name}".
'''
some_variable = "HELLO!"
print(f"some_variable={some_variable}")  # output: some_variable=HELLO!

## Instead, you can simply write:
some_variable = "HELLO!"
print(f"{some_variable=}")  # output: some_variable=HELLO!

# Printing on the Same Line - if need several string on same line
print("Python ", end="")
print("Programming")
# output: Python Programming

### MATH ###
print("===============")
print("MATH")
# basic operations
10 + 4  # add (returns 14)
10 - 4  # subtract (returns 6)
10 * 4  # multiply (returns 40)
10 ** 4  # exponent (returns 10000)
5 % 4  # modulo (returns 1) - computes the remainder
10 / 4  # divide (returns 2 in Python 2, returns 2.5 in Python 3)
10 / float(4)  # divide (returns 2.5)

# force '/' in Python 2 to perform 'true division' (unnecessary in Python 3)
# from __future__ import division
10 / 4  # true division (returns 2.5)
10 // 4  # floor division (returns 2)

### COMPARISONS AND BOOLEAN OPERATIONS ###
print("===============")
print("COMPARISONS AND BOOLEAN OPERATIONS")
# assignment statement
x = 5

# comparisons (these return True)
x > 3
x >= 3
x != 3
x == 5

# boolean operations (these return True)
5 > 3 and 6 > 3
5 > 3 or 5 < 3
not False
False or not False and True  # evaluation order: not, and, or

a = 1;
b = 2;
c = 3
d = 5;
e = 5;
f = 3
print("a=1;b=2;c=3\nd=5;e=5;f=3\n")
print(f"a<b<c is {a < b < c}")
print(f"a==b==c is {a == b == c}")
print(f"a<d<=e is {a < d <= e}")
print(f"d==e != f is {d == e != f}")
print(f"d>f<e is {d > f < e}")

# Use 'is' or 'is not' to compare variable addresses (by their id)
# Use '==' ór '!=' to compare variable values

a = [1, 2, 3]
b = [1, 2, 3]
print(f"a value is: {a} and id is: {hex(id(a))}")
print(f"b value is: {b} and id is: {hex(id(b))}")
print(f"a is b : {a is b}")  # False - they do not have same id(address in memory)
print(f"a == b : {a == b}")  # True - there is value is the same

### CONDITIONAL STATEMENTS ###
print("===============")
print("CONDITIONAL STATEMENTS")

# if statement
if x > 0:
    print('positive')

# if/else statement
if x > 0:
    print('positive')
else:
    print('zero or negative')

# if/elif/else statement
if x > 0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')

# single-line if statement (sometimes discouraged)
if x > 0: print('positive')

# single-line if/else statement (sometimes discouraged)
# known as a 'ternary operator'
# value_if_true if condition else value_if_false
'positive' if x > 0 else 'zero or negative'

# simple if-statement coniditions:
n = 10
# instead of:
if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
    pass
# Type:
if n in [0, 1, 2, 3, 4, 5]:
    pass

### LISTS ###
## properties: ordered, iterable, mutable, can contain multiple data types
print("===============")
print("LISTS")

# create an empty list (two ways)
empty_list = []
empty_list = list()

# create a list
simpsons = ['homer', 'marge', 'bart']

# examine a list
simpsons[0]  # print element 0 ('homer')
len(simpsons)  # returns the length (3)

# modify a list (does not return the list)
simpsons.append('lisa')  # append element to end
simpsons.extend(['itchy', 'scratchy'])  # append multiple elements to end
simpsons.insert(0, 'maggie')  # insert element at index 0 (shifts everything right)
simpsons.remove('bart')  # search for first instance and remove it
simpsons.pop(0)  # remove element 0 and return it
del simpsons[0]  # remove element 0 (does not return it)
simpsons[0] = 'krusty'  # replace element 0

# concatenate lists (slower than 'extend' method)
neighbors = simpsons + ['ned', 'rod', 'todd']

# find elements in a list
simpsons.count('lisa')  # counts the number of instances
simpsons.index('itchy')  # returns index of first instance

# list slicing [start:end:step]
# Start, stop and step are optional. If you don’t fill them in, they will default to:
# 0 for start
# the end of the list for stop
# 1 for step
# start is the index of element, stop is always index-1
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(numbers[0])  # element 0
print(numbers[0:3])  # elements 0, 1, 2
print(numbers[:3])  # elements 0, 1, 2
print(numbers[3:])  # elements 3, 4, 5, 6, 7, 8, 9
print(numbers[-1])  # last element (element 9)
print(numbers[::2])  # every 2nd element [0, 2, 4, 6, 8]
print(numbers[::-1])  # backwards [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# alternative method for returning the list backwards
list(reversed(numbers))

# We can easily create a new list from
# the first two elements of a list:
first_two = [1, 2, 3, 4, 5][0:2]
print(first_two)  # output: [1, 2]

# And if we use a step value of 2,
# we can skip over every second number
# like this:
steps = [1, 2, 3, 4, 5][0:5:2]
print(steps)
# [1, 3, 5]

# This works on strings too. In Python,
# you can treat a string like a list of
# letters:
mystring = "abcdefdn nimt"[::2]
print(mystring)
# 'aced it'

# sort a list in place (modifies but does not return the list)
simpsons.sort()
simpsons.sort(reverse=True)  # sort in reverse
simpsons.sort(key=len)  # sort by a key

# return a sorted list (does not modify the original list)
sorted(simpsons)
sorted(simpsons, reverse=True)
sorted(simpsons, key=len)

# insert into an already sorted list, and keep it sorted
num = [10, 20, 40, 50]
from bisect import insort

insort(num, 30)

### Difference between sort() and sorted() ####
# sort() sorts the original list.
# sorted() returns a new sorted list.
groceries = ['milk', 'bread', 'tea']

new_groceries = sorted(groceries)
# new_groceries = ['bread', 'milk', 'tea']

# groceries = ['milk', 'bread', 'tea']
groceries.sort()
# groceries = ['bread', 'milk', 'tea']


# create a second reference to the same list
same_num = num
same_num[0] = 0  # modifies both 'num' and 'same_num'

# copy a list (two ways)
new_num = num[:]
new_num = list(num)

# examine objects
num is same_num  # returns True (checks whether they are the same object)
num is new_num  # returns False
num == same_num  # returns True (checks whether they have the same contents)
num == new_num  # returns True

### DEQUES ###
print("======================")
print("DEQUES")
'''
 deques are a double-ended sequence data structure, 
 it’s designed for operations involving adding items to or removing items
 from both ends. 
 Thus, we shouldn’t limit our data model selection to only lists or other common data types. 
 When specific business needs (e.g. FIFO) arise, we should consider alternative data models.
'''
import collections

# Create a deque
DoubleEnded = collections.deque(["Mon", "Tue", "Wed"])
print(DoubleEnded)

# Append to the right
print("Adding to the right: ")
DoubleEnded.append("Thu")
print(DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print(DoubleEnded)

# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print(DoubleEnded)

# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print(DoubleEnded)

# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print(DoubleEnded)

### TUPLES ###
## properties: ordered, iterable, immutable, can contain multiple data types
## like lists, but they don't change size
print("===============")
print("TUPLES")

# create a tuple
digits = (0, 1, 'two')  # create a tuple directly
digits = tuple([0, 1, 'two'])  # create a tuple from a list it means we cannot add other object to the tuple
# but the list itself can be changed
zero = (0,)  # trailing comma is required to indicate it's a tuple

# What defines tuples is not the () but the ,
# Therefor a,b,c is equivalent to (a,b,c) - thats why (a) is not tuple but (a,) is tuple
# () is tuple to define empty one - although there is no ',' in it
# can define empty tuple also with tuple()

# examine a tuple
digits[2]  # returns 'two'
len(digits)  # returns 3
digits.count(0)  # counts the number of instances of that value (1)
digits.index(1)  # returns the index of the first instance of that value (1)

# elements of a tuple cannot be modified
# digits[2] = 2       # throws an error

# concatenate tuples
digits = digits + (3, 4)

# create a single tuple with elements repeated (also works with lists)
(3, 4) * 2  # returns (3, 4, 3, 4)

# sort a list of tuples
tens = [(20, 60), (10, 40), (20, 30)]
sorted(tens)  # sorts by first element in tuple, then second element
#   returns [(10, 40), (20, 30), (20, 60)]

# tuple unpacking
bart = ('male', 10, 'simpson')  # create a tuple
(sex, age, surname) = bart  # assign three values at once

# Trick to append values to tuple because it is immutable (non changed)
tuple1 = (1, 2, 3)
lst = list(tuple1)
lst.append(4)
lst.append(5)
tuple1 = tuple(lst)
print(f"new tuple after appending: {tuple1}")  # (1, 2, 3, 4, 5)

### NAMED TUPLES ####
print("================")
print("NAMED TUPLES")

# namedtuple - a function which generates new class like class factory that inherites from tuple
# because tuple are immutable and has elements and only with index can be reached
# we need method to define the elements like in class so it is easy to work with
# example: pt = (10,20)  meaning pt[0] is x coordinates and pt[1] is y coordinates
# we can define class Point:
#                   def __init__(self,x,y)
#                       self.x=x
#                       self.y=y
# OR we can use namedtuple that arrives from module collections
# namedtuple is class factory and we need to fulfill certain rules:
# 1. class name we want to use ; 2. sequence of field names(strings) we want to assign in the order
# of the elements in the tuple - names can be any valid name except they cannot start with '_'
# the return value will be a class , we need to assign this class to a var name as instance
# Example: Point2D = namedtuple('Point2D',['x','y'])  #notice ,this is a class we created
# Now we can create instance: pt = Point2D(10,20)
# Sequence of attributes can be a list or tuple, order matters, if you supply string seperate
# the attributes with whitespace or comma
# namedtuple('Point2D',['x','y'])
# namedtuple('Point2D',('x','y'))
# namedtuple('Point2D','x,y')
# namedtuple('Point2D','x y')
# initialization:
# pt1 = Point2D(10,20) or pt2 = Point2D(x=10,y=20)
# to access attributes - use index,slice or iterate
# isinstance(pt1,tuple) ==>> True
# x,y = pt1
# x = pt1[0]
# for e in pt1:
#     print(e)
# Or py1.x and pt1.y
# Because namedtuple inherites from tuple - it is immutable! pt1.x = 100 -->> Error
# To learn what fields belong to the namedtuple - use: _fields, Point2D._fields --> ('x','y')
# Instance method _asdict() create dictionary of all named values in the tuple
# pt1._asdict()  --> {'x':10,'y':20}
# When working with modules and there is function to import that has attributes it will be easier to return
# namedtuple because it will appear with name of attributes when calling the function
from collections import namedtuple

### STRINGS ###
## properties: iterable, immutable
print("===============")
print("STRINGS")

# create a string
s = str(42)  # convert another data type into a string
s = 'I like you'

# examine a string
s[0]  # returns 'I'
len(s)  # returns 10

# string slicing is like list slicing
s[:6]  # returns 'I like'
s[7:]  # returns 'you'
s[-1]  # returns 'u'

# basic string methods (does not modify the original string)
s.lower()  # returns 'i like you'
s.upper()  # returns 'I LIKE YOU'
s.startswith('I')  # returns True
s.endswith('you')  # returns True
s.isdigit()  # returns False (returns True if every character in the string is a digit)
s.find('like')  # returns index of first occurrence (2), but doesn't support regex
s.find('hate')  # returns -1 since not found
s.replace('like', 'love')  # replaces all instances of 'like' with 'love'

# split a string into a list of substrings separated by a delimiter
print("split example")
print(s.split(' '))  # returns ['I', 'like', 'you']
s.split()  # equivalent (since space is the default delimiter)
s2 = 'a, an, the'
s2.split(',')  # returns ['a', ' an', ' the']

# similar to this is 'partition' - Only splits the string once/ tracka the delimiter/ Returns the same data structure.
print("partition example")
print(s.partition('like'))

# join a list of strings into one string using a delimiter
stooges = ['larry', 'curly', 'moe']
' '.join(stooges)  # returns 'larry curly moe'

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4  # returns 'The meaning of life is 42'

# professional concatenate with JOIN method - better than '+'
arr = ['H', 'e', 'l', 'l', 'o']
result = "".join(arr)  # output: Hello

# remove whitespace from start and end of a string
s5 = '  ham and cheese  '
s5.strip()  # returns 'ham and cheese'

# string substitutions: all of these return 'raining cats and dogs'
'raining %s and %s' % ('cats', 'dogs')  # old way
'raining {} and {}'.format('cats', 'dogs')  # new way
'raining {arg1} and {arg2}'.format(arg1='cats', arg2='dogs')  # named arguments

# string formatting
# more examples: https://mkaz.blog/code/python-string-format-cookbook/
'pi is {:.2f}'.format(3.14159)  # returns 'pi is 3.14'

# normal strings versus raw strings
print('first line\nsecond line')  # normal strings allow for escaped characters
print(r'first line\nfirst line')  # raw strings treat backslashes as literal characters

# Split string to characters
str_samp = "Hello World"

# print a character
print(str_samp[3])

# capitalize a sentence - First char is Capital rest are small
s = 'this is a sentence.'
# old way: s = s[0].upper() + s[1:]
# New way: use capitalize
print(f"capitlize is: {s.capitalize()}")  # output: This is a sentence

# capitalize every word in a sentence - first char of each word in sentence
s = 'this is a sentence.'
# old way
'''
words = s.split(' ')
words = [w[0].upper() + w[1:] for w in words]
s = ' '.join(words)
'''
print(f"title() is: {s.title()}")  # output: This Is A Sentence

id_list = [
    '123',
    '45',
    '4321',
    '51323'
]
fixed_len = 6
print(f"zfill is: {[id.zfill(fixed_len) for id in id_list]}")
# output: ['000123', '000045', '004321', '051323']

# Decide if string is made of chars or numbers
s = '1plus1'
# re-invent the wheel:
# import re
# bool(re.match(r'^[\dA-Za-z]+$', s))
s.isalnum()  # output: True

'''
    If you want to match a string with letters only, use isalpha()
    If you want to match a string with digits only, use isdigit()
    If you want to match a decimal number (not binary or hex), use isdecimal()
    If you consider the underscore “_” is valid in a string, use isidentifier()
'''

'''
Sometimes we receive string with '\n' or '\t' and we want to remove leading spaces or tailing spaces.
'''
s = ' \nDan Belfer\t  '
print(f"My name is {s.strip()}")  # output: My name is Dan Belfer

# split lines
'''
When we want to break down a large chunk of string into lines by the newlines, 
we can definitely use split()
'''
print("regular split:")
print("123 \n 456 \r 789 \r\n abc".split('\n'))  # output: ['123 ', ' 456 \r 789 \r', ' abc']

print("split lines:")
print([s.strip() for s in "123 \n 456 \r 789 \r\n abc".splitlines()])  # output: ['123', '456', '789', 'abc']

print("join example: ")
s = 'abcdef'
print(' '.join(s))  # output: 'a b c d e f'
print(','.join(s))  # output  'a,b,c,d,e,f'

str1 = "Reverse a String"  # the best way to reverse string
print(f"{str1} and now reversed: {str1[::-1]}")

# make list from the string
chars = list(str_samp)  # output: l
print(type(chars))  # output: <class 'list'>
print(chars[3])  # output: l

# remove new line from strings in list
data = ['alpha\n', 'beta\n', 'gamma\n']
print(data)  # output: ['alpha\n', 'beta\n', 'gamma\n']
data = [s.strip() for s in data]
print(data)  # output:['alpha', 'beta', 'gamma']

### namedtuple ####
# namedtuple is better when importing modules because inner attributes are seen in new context
from random import randint
from collections import namedtuple

Color = namedtuple('Color', 'red green blue')


def rand_colors():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return Color(red, green, blue)


color = rand_colors()
print(f"color is:{color}")

# Best way to find palindrom
w = "Rotator".lower()
palindrome = bool(w.find(w[:: -1]) + 1)
print(f"Is {w} is palindrom? {palindrome}")


# write a program to find the largest word in a text file?
def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


# print(longest_word('test.txt'))


### DICTIONARIES ###
## properties: unordered, iterable, mutable, can contain multiple data types
## made of key-value pairs
## keys must be unique, and can be strings, numbers, or tuples
## values can be any type
print("===============")
print("DICTIONARY")

# create an empty dictionary (two ways)
empty_dict = {}
empty_dict = dict()

# create a dictionary (two ways)
family = {'dad': 'homer', 'mom': 'marge', 'size': 6}
family = dict(dad='homer', mom='marge', size=6)

# convert a list of tuples into a dictionary
list_of_tuples = [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
family = dict(list_of_tuples)

# examine a dictionary
family['dad']  # returns 'homer'
len(family)  # returns 3
'mom' in family  # returns True
'marge' in family  # returns False (only checks keys)

# returns a list (Python 2) or an iterable view (Python 3)
family.keys()  # keys: ['dad', 'mom', 'size']
family.values()  # values: ['homer', 'marge', 6]
family.items()  # key-value pairs: [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]

# modify a dictionary (does not return the dictionary)
family['cat'] = 'snowball'  # add a new entry
family['cat'] = 'snowball ii'  # edit an existing entry
del family['cat']  # delete an entry
family['kids'] = ['bart', 'lisa']  # dictionary value can be a list
family.pop('dad')  # remove an entry and return the value ('homer')
family.update({'baby': 'maggie', 'grandpa': 'abe'})  # add multiple entries

# access values more safely with 'get'
family['mom']  # returns 'marge'
family.get('mom')  # equivalent
# family['grandma']                   # throws an error since the key does not exist
family.get('grandma')  # returns None instead
family.get('grandma', 'not found')  # returns 'not found' (the default)

# access a list element within a dictionary
family['kids'][0]  # returns 'bart'
family['kids'].remove('lisa')  # removes 'lisa'

# string substitution using a dictionary
'youngest child is %(baby)s' % family  # returns 'youngest child is maggie'

# simple iteration dictionary using 'in'
data = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome'
}

for country in data:
    print(f'The capital of {country} is {data[country]}')

# A safer way of reading values from dictionary - using get instead of [key]
data = {'France': 'Paris', 'Italy': 'Rome'}

# capital  = data,get('Germany') #ERROR
capital = data.get('Germany')
# but it retuns None
print(capital)  # output: None

capital = data.get('Germany', '??')
print(capital)  # output: ??

'''
The advantage of these functions is that these functions do not throw errors 
if the item with a specified key does not exist.
'''
print("get() and setdefault() functions for dictionary: ")
dict1 = {1: 'one', 2: 'two', 4: 'four'}
print(dict1.get(3))  # output: None
print(dict1.setdefault(3, 'Default Value'))  # output: Default Value

'''
Swap dictionary key & values:
'''
mydict= {1: 11, 2: 22, 3: 33}
mydict = {i: j for j, i in mydict.items()}
print(mydict) #output: {11: 1, 22: 2, 33: 3}

mydict= {'John': 'Tesla', 'Jane': 'BMW'}
mydict = {i:j for j,i in mydict.items()}
print(mydict) #output: {'Tesla': 'John', 'BMW': 'Jane'}

### SETS ###
## properties: unordered, iterable, mutable, can contain multiple data types
## made of unique elements (strings, numbers, or tuples)
## like dictionaries, but with keys only (no values)
print("===============")
print("SETS")

# create an empty set
empty_set = set()

# create a set
languages = {'python', 'r', 'java'}  # create a set directly
snakes = set(['cobra', 'viper', 'python'])  # create a set from a list

# examine a set
len(languages)  # returns 3
'python' in languages  # returns True

# set operations
languages & snakes  # returns intersection: {'python'}
languages | snakes  # returns union: {'cobra', 'r', 'java', 'viper', 'python'}
languages - snakes  # returns set difference: {'r', 'java'}
snakes - languages  # returns set difference: {'cobra', 'viper'}

# modify a set (does not return the set)
languages.add('sql')  # add a new element
languages.add('r')  # try to add an existing element (ignored, no error)
languages.remove('java')  # remove an element
# languages.remove('c')       # try to remove a non-existing element (throws an error)
languages.discard('c')  # remove an element if present, but ignored otherwise
languages.pop()  # remove and return an arbitrary element
languages.clear()  # remove all elements
languages.update(['go', 'spark'])  # add multiple elements (can also pass a set)
# Notice: set is not ordered so: s = {'p','y','t','h','o','n'}  when print it ,output: {'h', 'y', 't', 'n', 'p', 'o'}
# that is why we cannot do: s[0] = ... it is unordered

# get a sorted list of unique elements from a list
sorted(set([9, 0, 2, 1, 0]))  # returns [0, 1, 2, 9]

# remove a duplication in list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 1, 1, 2]
print(list(set(my_list)))  # output: [1, 2, 3, 4, 5]

### DEFINING FUNCTIONS ###
print("===============")
print("FUNCTIONS")


# define a function with no arguments and no return values
def print_text():
    print('this is text')


# call the function
print_text()


# define a function with one argument and no return values
def print_this(x):
    print(x)


# call the function
print_this(3)  # prints 3
n = print_this(3)  # prints 3, but doesn't assign 3 to n


#   because the function has no return statement

# define a function with one argument and one return value
def square_this(x):
    return x ** 2


# include an optional docstring to describe the effect of a function
def square_this(x):
    """Return the square of a number."""
    return x ** 2


# call the function
square_this(3)  # prints 9
var = square_this(3)  # assigns 9 to var, but does not print 9


# define a function with two 'positional arguments' (no default values) and
# one 'keyword argument' (has a default value)
def calc(a, b, op='add'):
    if op == 'add':
        return a + b
    elif op == 'sub':
        return a - b
    else:
        print('valid operations are add and sub')


# call the function
calc(10, 4, op='add')  # returns 14
calc(10, 4, 'add')  # also returns 14: unnamed arguments are inferred by position
calc(10, 4)  # also returns 14: default for 'op' is 'add'
calc(10, 4, 'sub')  # returns 6
calc(10, 4, 'div')  # prints 'valid operations are add and sub'


# Notice: Default parameter will be assigned to param and all rest of params after it also should have default value
def func(a, b=1, c=2):
    pass


func(100)  # meaning a receives 100 and b is 1 and c is 2
# Named argument can enable to choose which val go to which param even if not in same order
func(c=10, a=3)  # will give a=3,b=1,c10  --> b received 1 as default


# use 'pass' as a placeholder if you haven't written the function body
def stub():
    pass


# return two values from a single function
def min_max(nums):
    return min(nums), max(nums)


# return values can be assigned to a single variable as a tuple
nums = [1, 2, 3]
min_max_num = min_max(nums)  # min_max_num = (1, 3)

# return values can be assigned into multiple variables using *tuple unpacking*
min_num, max_num = min_max(nums)  # min_num = 1, max_num = 3


# Chained function call
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 5, 10

print(f"Chained Function calls: {(add if b > a else subtract)(a, b)}")  # output: Chained Function calls: 15

# Objects Can Behave Like Functions
'''
While all functions are objects in Python, the reverse isn’t true. Objects aren’t functions. But they can be made 
callable, which allows us to treat them like functions in many cases.
If an object is callable it means we can use the round parentheses function call syntax on it and even pass in function 
call arguments. This is all powered by the __call__ dunder method.
Here’s an example of class defining a callable object:
class Foo:
    def __init__(self):
        print("init")
    def __call__(self):
        print("call")
>>> obj = Foo()
init
>>> obj()
call
'''

### DOCSTRING FUNCTIONS ###
### Enable adding documentation to functions - can be activated by __doc__ ###
print("===============")
print("DOCSTRING FUNCTIONS")


def func_doc_string(something):
    '''This is doctring that expalins func_doc_string'''
    return something


func_doc_string('Hi')
print(func_doc_string.__doc__)

### *ARGS ###
### an operator we can pass to functions, can be called whatever we want, gather remaining arguments as tuple ###
print("===============")
print("*ARGS")

l = [1, 2, 3, 4, 5, 6]
a, b = l[0], l[1:]

print(f"a is: {a}")  # a is: 1
print(f"b is: {b}")  # b is: [2, 3, 4, 5, 6]

# Using *
c, *d = l

print("-----------")
print(f"c is: {c}")  # c is: 1
print(f"d is: {d}")  # d is: [2, 3, 4, 5, 6]
print(*d)  # output: 2 3 4 5 6
### Notice: *param inside of method will removes the list structure and give list of elements


l1 = [1, 2, 3, 4, 5, 6]
a1, b1, *c1, d1 = l1

print(f"a1 is: {a1}")  # a1 is: 1
print(f"b1 is: {b1}")  # b1 is: 2
print(f"c1 is: {c1}")  # c1 is: [3, 4, 5]
print(f"d1 is: {d1}")  # d1 is: 6

a, *b, (c, *d) = [1, 2, 3, 'python']
print(f"a is: {a}")  # a is: 1
print(f"b is: {b}")  # b is: [2, 3]
print(f"c is: {c}")  # c is: p
print(f"d is: {d}")  # d is: ['y', 't', 'h', 'o', 'n']


def sum_all_nums(*nums):
    total = 0
    for n in nums:
        total += n
    return total


print(f"sum of all nums is: {sum_all_nums(1, 2, 3, 4, 5, 6)}")  # 21


def avg(*args):
    count = len(args)
    total = sum(args)
    return count, total / count


print(avg(2, 2, 4, 4))  # output: (4,3.0)

### **KWARGS ###
### an operator we can pass to functions, gather remaining arguments as a dictionary ###
### **kwargs is used when we want to pass a dictionary as an argument to a function. ###
print("===============")
print("**KWARGS")


def func(**kargs):
    print(kargs)


func(a=1, b=2, c=3)  # output: {'a': 1, 'b': 2, 'c': 3}


def family_members(**people):
    for name, family_name in people.items():
        print(f"His name is {name} and family name is {family_name}")


family_members(ídan="Belfer", ron="Ram", noam="Belfer")


# His name is ídan and family name is Belfer
# His name is ron and family name is Ram
# His name is noam and family name is Belfer

def intro(**data):
    print("\nData type of argument:", type(data))
    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(name="alex", Age=22, Phone=1234567890)
intro(name="louis", Email="a@gmail.com", Country="Wakanda", Age=25)
'''
Data type of argument: <class 'dict'>
name is alex
Age is 22
Phone is 1234567890

Data type of argument: <class 'dict'>
name is louis
Email is a@gmail.com
Country is Wakanda
Age is 25
'''

### RETURN ###
print("===============")
print("RETURN")

'''
By Default function return None, even if nothing is returned
def func():
    tot = 1 +2
    
print(func()) #output: None

If the return statement is not reached in the function, it returns None.
def add(a,b):
    c=a+b
    if (c>10):
        return c
    
print(add(1,2)) #output: None

Return Multiple values from a function:
+ using commas  return a,b,c  -->> return type tuple
+ List          return [a,b,c] -->> return type list
+ Set           return {a,b,c} -->> return type set
+ Dictionary    return {'a':a,'B':b,'C':c} -->> return type dictionary
Examples: 

def add(a,b):
    result=a+b
    return a,b,result

print(add(1,2))  #output: (1,2,3)

def add(a,b):
    result=a+b
    return result,

print(add(1,2))  #output: (3,)

def calc(a,b):
    sum=a+b
    dif=a-b
    mul=a*b
    div=a/b
    return [sum,dif,mul,div]

print(calc(5,4)) #Output:[9, 1, 20, 1.25]

def calc(a,b):
    sum=a+b
    dif=a-b
    mul=a*b
    div=a/b
    return {"Addition":sum,"Subtraction":dif,"Multiplication":mul,"Division":div}

print(calc(5,4)) #Output:{'Addition': 9, 'Subtraction': 1, 'Multiplication': 20, 'Division': 1.25}

def calc(a,b):
    sum=a+b
    dif=a-b
    mul=a*b
    div=a/b
    return {sum,dif,mul,div}

print(calc(5,4)) #Output:{9, 20, 1, 1.25}

The return statement having a single expression without a trailing comma doesn’t create a tuple; 
it returns the value of that expression.

def add(a,b):
   result=a+b
   return result

print(add(1,2)) #Output:3

print(add("Hello ","Python"))  #Output:Hello Python

print(add([1,2],[3,4])) #Output:[1, 2, 3, 4]

print(add((1,2),(3,4))) #Output:(1, 2, 3, 4)

Multiple ‘return’ statements in a single function:
The function call is terminated when one of the return statements is reached.

def num(a):
    if a%2==0:
        return "Even Number"
    else:
        return "Odd Number"

print(num(5))#Output:Odd Number
print(num(30))#Output:Even Number

‘return’ vs. ‘print’ statements inside a function
The return statement will terminate the function call and return the value to the caller.
The print statement will just print the value. We can’t assign that result to another variable or pass 
the result to another function.

def add(a,b):
    r1=a+b
    print (r1)

add(3,4) #Output:7

#We can't assign the return value to a variable
r3=add(3,4) 
print(r3)  #Output:None

‘return’ statement terminates the function call
The return statement terminates the current function call with the expression list (or None) as the return value. 
The statements after the return statement inside the function are not executed.

def add(a,b):
    result=a+b
    return result
    print("After return statement")

print(add(3,4)) #Output:7

’return’ statement in ‘try’ block
“When return passes control out of a try statement with a finally clause, 
that finally clause is executed before really leaving the function.”

Example: In the below example, the function call will return after executing the finally clause:

def add(a,b):
    try:
        result=a+b
        return result

    except Exception as e:
        return e
    finally:
        print("Finally done")

print(add(3,4))

#Output:
#Finally done
#7

If an exception is raised, the function call will return after executing the finally clause.

def add(a,b):
    try:
        result=a+b
        return result
    except Exception as e:
        return e
    finally:
        print("Finally done")

print(add({'a':1},{'b':2}))

Output:
Finally done
unsupported operand type(s) for +: 'dict' and 'dict'
 
'''


### PARAMETER ORDERING - only when you use all types of follwing###
### 1. params 2.*args 3.default params 4.**kwargs ###
def display_info(a, b, *args, first_name='Dan', **kwargs):
    return [a, b, args, first_name, kwargs]


print(display_info(1, 2, 3, last_name="Belfer", jov="Programmer"))
# output: [1, 2, (3,), 'Dan', {'last_name': 'Belfer', 'jov': 'Programmer'}]

# *** NOTICE: if you pick arg nth place to receive default ,from it and till last - all rest args should have defaults
# func(a, b=10,c='wow') is correct!! func(a,b=10,c) is WRONG!!!

### output: [1, 2, (3,), 'Colt', {'last_name': 'Belfer', 'jov': 'Programmer'}] ###

### TUPLE UNPACKING ### -- enable return of multiple vars from functions!
### Use * before arguments to convert to tuple when passing them to functions
print("===============")
print("TUPLE UNPACKING")


def count_sevens(*args):
    return args.count(7)


nums = [90, 1, 35, 7, 67, 89, 20, 3, 1, 2, 3, 4, 5, 6, 9, 34, ]
print(f"count_sevens() is {count_sevens(*nums)}")  # output: count_sevens() is 1

### Dictionary Unpacking ###
### Use ** before arguments as params to functions to convert to disctionary
print("===============")
print("DICTIONARY UNPACKING")


def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Ram", "second": "Anat"}
display_names(**names)  # output: Ram says hello to Anat

### ANNOTATIONS ####
# Function annotations give us additional way to document our functions
# used with __annotations__ dunder
print("===============")
print("ANNOTATIONS")


# def my_func(a:<expression>,b:<expression>)-><expression>:
#     pass

def func(a: str, b: int) -> str:
    return a * b


# In case of using default values
def func(a: str = 'xyz', b: int = 5) -> str:
    return a * b


func()  # output: xyzxyzxyzxyzxyz
print(func("Dan", 4))  # output: DanDanDanDan

from typing import List


def func(l: List[int]) -> list[int]:
    return [e ** 2 for e in lst]


lst = [1, 2, 3, 4]
print(func(lst))

### ANONYMOUS (LAMBDA) FUNCTIONS ###
## primarily used to temporarily define a function for use by another function - like inline functions
## This is a real function with anonymous name , structure: lambda [param list] : expression
## The expression returns function object when it is called, param list is optional can be empty
## Lambda expression MUST be assigned to variable OR passed as argument to function
print("===============")
print("LAMBDA FUNCTIONS")

my_func = lambda x: x ** 2
# my_func(3) ->9
my_func = lambda x, y: x + y
# my_func(3,5) ->8
my_func = lambda: 'hello'
print(my_func())  # output: hello


# define a function the "usual" way
def squared(x):
    return x ** 2


# define an identical function using lambda
squared = lambda x: x ** 2


# print(squared(5)) #output: 25

## lambda as argument to function
def apply_func(x, fn):
    return fn(x)


print(apply_func(3, lambda x: x ** 2))  # output: 9
print(apply_func(2, lambda x: x + 2))  # output: 4

f = lambda x, y=10: x + y
print(f(1, 2))  # output:3
print(f(1))  # output:11
f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(f(1, 'a', 'b', y=100, a=10, b=20))  # output: (1, ('a', 'b'), 100, {'a': 10, 'b': 20})

l = ['C', 'B', 'a', 'd']
print(sorted(l))  # output: ['B', 'C', 'a', 'd']  this sort is only by ord(x) value
# Need to do sorting by same type of letter for example all are upper()
print(sorted(l, key=lambda s: s.upper()))  # output: ['a', 'B', 'C', 'd'] as expected

d = {'abc': 200, 'def': 300, 'ghi': 100}
print(sorted(d))  # output:['abc', 'def', 'ghi']
# we want to sort by the value not the key
print(sorted(d, key=lambda e: d[e]))  # output: ['ghi', 'abc', 'def']  as we want by value

# sort a list of strings by the last letter (without using lambda)
simpsons = ['homer', 'marge', 'bart']


def last_letter(word):
    return word[-1]


sorted(simpsons, key=last_letter)

# sort a list of strings by the last letter (using lambda)
sorted(simpsons, key=lambda word: word[-1])

import random

# randomize sorting of 10 numbers
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted(l, key=lambda x: random.random()))

'''
sorted() method can be used to sort any iterable in Python
We have passed a lambda function as a key to sort the dictionary by age
'''

data = [{'name': 'John', 'age': 21},
        {'name': 'Max', 'age': 19},
        {'name': 'Lisa', 'age': 22}
        ]
sorted_data = sorted(data, key=lambda x: x['age'])
print("Using sorted on dictionary by age:")
print(sorted_data)  # [{'name': 'Max', 'age': 19}, {'name': 'John', 'age': 21}, {'name': 'Lisa', 'age': 22}]

### FUNCTION ATTRIBUTES ####
print("=================")
print("FUNCTION ATTRIBUTES")
import inspect


def my_func(a: "first",
            b: "optional" = 1,
            c=2,
            *args: "args here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "extra kw ") -> "do nothing":
    """This is a function for explanation"""
    i = 10
    j = 20


print(my_func.__doc__)  # output: This is a function for explanations
print(my_func.__annotations__)
# output: {'a': 'first', 'b': 'optional', 'args': 'args here', 'kwargs': 'extra kw ', 'return': 'do nothing'}
my_func.short_description = "added attribute to the function"
## all attributes of function can be seen with dir(func) method
print(my_func.__name__)  # output: my_func
print(my_func.__defaults__)  # output: (1,2) --> match to b=1,c=2
print(my_func.__kwdefaults__)  # output: {'kw2': 100, 'kw3': 200}
# function has attribute named: __code__ which is object that we can do dir(my_func.__code__)
print(my_func.__code__.co_name)  # output: my_func
print(my_func.__code__.co_argcount)  # output: 3 for a,b,c - show only positional arguments
print(my_func.__code__.co_varnames)  # output: ('a', 'b', 'c', 'kw1', 'kw2', 'kw3', 'args', 'kwargs', 'i', 'j')
print(inspect.getdoc(my_func))  # output: This is a function for explanation
# print(inspect.signature(my_func).parameters) # output will be all parameters
# for k,v in inspect.signature(my_func).parameters.items():
#    print(f"{k} : {v} ") #output: all the params with values


### FOR LOOPS AND WHILE LOOPS // ENUM ###
print("===============")
print("FOR WHILE LOOPS // ENUM")

# range returns a list of integers (Python 2) or a sequence (Python 3)
range(0, 3)  # returns [0, 1, 2]: includes start value but excludes stop value
range(3)  # equivalent: default start value is 0
range(0, 5, 2)  # returns [0, 2, 4]: third argument is the step value

# for loop (not the recommended style)
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i].upper())

# for loop (recommended style)
for fruit in fruits:
    print(fruit.upper())

# iterate through two things at once (using tuple unpacking)
family = {'dad': 'homer', 'mom': 'marge', 'size': 6}
for key, value in family.items():
    print(key, value)

# use enumerate if you need to access the index value within the loop
for index, fruit in enumerate(fruits):
    print(index, fruit)

# for/else loop - #else will happen if for loop finishes completely and not stopped by break
for fruit in fruits:
    if fruit == 'banana':
        print('Found the banana!')
        break  # exit the loop and skip the 'else' block
else:
    # this block executes ONLY if the for loop completes without hitting 'break'
    print("Can't find the banana")

# while loop
count = 0
while count < 5:
    print('This will print 5 times')
    count += 1  # equivalent to 'count = count + 1'

# 'else' command after while will be execute after while finishes
# else will happen if while loop finishes completely and not stopped by break
x = 5
while x > 0:
    print(x)
    if x < 0:
        break
    x -= 1
else:
    print('Done')

### ENUMERATION ###
print("===============")
print("ENUMERATIONS")


class Direction:
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


def move(direction):
    if direction == Direction.NORTH:
        print("Moving North")
    elif direction == Direction.EAST:
        print("Moving East")
    elif direction == Direction.SOUTH:
        print("Moving South")
    elif direction == Direction.WEST:
        print("Moving West")


# ENUMERATE SAMPLE with Start argument
print("Example of Enum with Start value:")
mylist = ['a', 'b', 'd', 'c', 'g', 'e']
print("Regular Enum:")
for i, item in enumerate(mylist):
    print(i, item)  # output: 0 a 1 b 2 d 3 c 4 g 5 e

# but, you can add a start for enumeration:
print("Enum start with index from 16...")
for i, item in enumerate(mylist, 16):
    print(i, item)  # output: 16 a 17 b 18 d 19 c 20 g 21 e
print("\n")

### COMPREHENSIONS ###
print("===============")
print("COMPREHENSIONS")

# for loop to create a list of cubes
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
    cubes.append(num ** 3)

# equivalent list comprehension
cubes = [num ** 3 for num in nums]  # [1, 8, 27, 64, 125]

# for loop to create a list of cubes of even numbers
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num ** 3)

# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]
cubes_of_even = [num ** 3 for num in nums if num % 2 == 0]  # [8, 64]

# for loop to cube even numbers and square odd numbers
cubes_and_squares = []
for num in nums:
    if num % 2 == 0:
        cubes_and_squares.append(num ** 3)
    else:
        cubes_and_squares.append(num ** 2)

# equivalent list comprehension (using a ternary expression)
# syntax: [true_condition if condition else false_condition for variable in iterable]
cubes_and_squares = [num ** 3 if num % 2 == 0 else num ** 2 for num in nums]  # [1, 8, 9, 64, 25]

# for loop to flatten a 2d-matrix
matrix = [[1, 2], [3, 4]]
items = []
for row in matrix:
    for item in row:
        items.append(item)

# equivalent list comprehension
items = [item for row in matrix for item in row]  # [1, 2, 3, 4]

# set comprehension
fruits = ['apple', 'banana', 'cherry']
unique_lengths = {len(fruit) for fruit in fruits}  # {5, 6}

# dictionary comprehension
fruit_lengths = {fruit: len(fruit) for fruit in fruits}  # {'apple': 5, 'banana': 6, 'cherry': 6}
fruit_indices = {fruit: index for index, fruit in enumerate(fruits)}  # {'apple': 0, 'banana': 1, 'cherry': 2}

new_list = [x for x in range(10)]  # list comprehension
new_dict = {x: x + 1 for x in range(10)}  # dictionary comprehension
new_set = {x for x in range(10)}  # set comprehension
new_gen = (x for x in range(10))  # generator comprehension

### MAP AND FILTER REDUCE ALL AND ANY ###
print("===============")
print("MAP AND FILTER REDUCE ALL AND ANY ")

# 'map' applies a function to every element of a sequence
# ...and returns an iterator
# function that accepts at least 2 args, a function and íterable
# iterable = something that can be iterated over(list,string,dictionary,set,tuple)
# runs lambda for each value in the iterable and returns
# a map object which can be converted into other data structure
'''
+ If you already have a list of values and you want to do the exact same operation on each of the elements in the array 
  and return the same amount of items in the list, in these type of situations it is better to use the map method.

+ If you already have list of values but you only want to have items in the array that match certain criteria, 
  in these type of situations it is better to use the filter method.

+ If you already have list of values, but you want to use the values in that list to create something completely new, 
  in these type of situations it is better to use the reduce method.
'''


# map example
def square(n): return n * n


map_inputs = (1, 2, 3, 4)
map_ret = map(square, map_inputs)
print(map_ret)  # output: <map object at 0x0000019F8B6CC910>
list_square = list(map_ret)
print(list_square)  # output: [1, 4, 9, 16]

# map usually uses lambda function
map_inputs = (1, 2, 3, 4)
map_ret = map(lambda n: n ** 2, map_inputs)
print(map_ret)  # output: <map object at 0x0000019F8B6CC700>
list_square = list(map_ret)
print(list_square)  # output: [1, 4, 9, 16]

# map most short version
map_inputs = (1, 2, 3, 4)
print(list(map(lambda n: n ** 2, map_inputs)))  # output: [1, 4, 9, 16]

# filter example
in_list = [98, 99, 100, 101, 102]
out_list = filter(lambda x: x > 100, in_list)
print(list(out_list))  # output: [101, 102]

# reduce example
result = 1
in_num = [1, 2, 3, 4, 5]
for num in in_num:
    result = result * num
print(result)  # output: 120

simpsons = ['homer', 'marge', 'bart']
map(len, simpsons)  # returns [5, 5, 4]
map(lambda word: word[-1], simpsons)  # returns ['r', 'e', 't']

l = [1, 2, 3, 4]
doubles = list(map(lambda x: x * 2, l))  # output: evens [2,4,6,8]
# equivalent list comprehensions
[len(word) for word in simpsons]
[word[-1] for word in simpsons]
[x * 2 for x in l]

# 'filter' returns iterator containing
# ...the elements from a sequence for which a condition is True
nums = range(5)
filter(lambda x: x % 2 == 0, nums)  # returns [0, 2, 4]

# equivalent list comprehension
[num for num in nums if num % 2 == 0]

# Combining map and filter
l = range(10)
print("map & filter:")
print(list(filter(lambda y: y < 25, map(lambda x: x ** 2, l))))  # output: [0, 1, 4, 9, 16]
# easy to use list comprehension
print("list comprehension:")
print([x ** 2 for x in range(10) if x ** 2 < 25])  # output: [0, 1, 4, 9, 16]
# Another list comprehention but with conditions:
Genius = ["Jerry", "Jack", "tom", "Dan"]
print("List Cmprehnsion with conditions:")
L1 = [name if name.startswith('D') else 'Not Genius' for name in Genius]
print(L1)  # ['Not Genius', 'Not Genius', 'Not Genius', 'Dan']

print("Same example without List Comprehension:")
L2 = []
for name in Genius:
    if name.startswith('D'):
        L2.append(name)
    else:
        L2.append('Not Genius')

print(L2)  # ['Not Genius', 'Not Genius', 'Not Genius', 'Dan']

# Use Nested For-Loops to Handle Nested Iterables
Genius = ["Jerry", "Jack", "tom", "Dan"]
L1 = []
for name in Genius:
    for char in name:
        L1.append(char)
print(L1)  # output: ['J', 'e', 'r', 'r', 'y', 'J', 'a', 'c', 'k', 't', 'o', 'm', 'D', 'a', 'n']

# The short way using list comprehention
Genius = ["Jerry", "Jack", "tom", "Dan"]
L1 = [char for name in Genius for char in name]
print(L1)  # output: ['J', 'e', 'r', 'r', 'y', 'J', 'a', 'c', 'k', 't', 'o', 'm', 'D', 'a', 'n']

# 'all' return True if all elements of iterable are true (or iterable empty)
# 'all' behaves like a series of AND conditions
all([0, 1, 2, 3])  # False
all([char for char in 'eio' if char in 'aeiou'])
all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])  # True
# 'any' return True if any element of iterable is true. If iterable is empty ,returns False
# 'any' behaves like a series of OR conditions
any([0, 1, 2, 3])  # True
any([val for val in [1, 2, 3] if val > 2])  # True
any([val for val in [1, 2, 3] if val > 5])  # False

'''
When you need many conditions to be fulfilled in your code, 
then you can use Conditional List and All to check all the conditions. 
We can write all the conditions in the list and apply All to check if all the conditions are true.
Instead of using the if statement and writing all the conditions separated by and operator, 
we can write all the conditions in the list and apply All.
'''
physics = 49
chemistry = 51
mathematics = 57

list_condition = [physics > 50, chemistry > 50, mathematics > 50]
("Pass" if all(list_condition) else "Fail")  # output: Fail

'''
We can use a Conditional List and Any together when we want to check even if one of the many conditions is True.
Instead of using if statement and checking conditions separated by or operator, 
we can write all the conditions in the list and pass it to Any.
'''

physics = 49
chemistry = 51
mathematics = 47

list_condition = [physics > 50, chemistry > 50, mathematics > 50]
("Pass" if any(list_condition) else "Fail")  # output: Pass

'''
Python has some higher order functions such as map() , filter() and so on. 
It’s a good habit to always use the list comprehension instead of higher order functions. 
Because it makes our programs more readable for others.
'''

# The map() method can always be replaced:
# L = map(func, iterable)
#### can be replaced to:
# L = [func(a) for a in iterable]

# The filter() method can be converted as well:
###L = filter(condition_func, iterable)
# can be converted to
###L = [a for a in iterable if condition]

Genius = ["Jerry", "Jack", "tom", "Daniel"]
L1 = filter(lambda a: len(a) < 4, Genius)
print(list(L1))
# ['tom']
# Better way
L2 = [a for a in Genius if len(a) < 4]
print(L2)
# ['tom']

### ZIP ###
print("===============")
print("ZIP")

# make an iterator that aggregates elements from each of the iterables, only works with iterators
# for iterating over two data types at the same time, where needed the indexes to be equal
list1 = [102, 306, 918, 2754]
list2 = [1, 3, 9, 27]

averages = []
for idx1, el1 in enumerate(list1):  # first for-loop
    for idx2, el2 in enumerate(list2):  # second for-loop
        if idx1 == idx2:  # check whether the indexes of first * second for-loop match
            y_intercept = el1 / el2
            averages.append(y_intercept)

print(averages)  # output: [102.0, 102.0, 102.0, 102.0]
## Now with zip...
averages = []
for el1, el2 in zip(list1, list2):  # loop through both list using zip
    y_intercept = el1 / el2
    averages.append(y_intercept)
print(averages)  # output: [102.0, 102.0, 102.0, 102.0]

'''
You can do this with any data type or generator. 
For instance, you could create dictionaries without looping over the separate lists, as such:
'''
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))  # Best way to convert list to dictionary
print(dictionary)  # output: {'a': 1, 'b': 2, 'c': 3}

# Returns an iterator of tuples ,where the i-th tuple contains the i-th element
# from each of the argument sequences or iterables
# The iterator stops when the shortest input iterable is exhausted
num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
print(list(zip(num1, num2)))  # output: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(dict(zip(num1, num2)))  # output: {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}
l1 = [1, 2, 3]
l2 = [a, b, c, d]
print(list(zip(l1, l2)))

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd']
print(list(zip(l1, l2)))  # output: [(1, 'a'), (2, 'b'), (3, 'c')]

l1 = [1, 2, 3]
l2 = [10, 20, 30]
print([x + y for x, y in zip(l1, l2)])  # output: [11,22,33]

print("Example of transpose of 2D data:")
m = [(1, 2, 3), (4, 5, 6)]
print(f"We have matrix: m = {m}")

print(f"Use *m to load the args - these 2 tuples to transpose the lists: list(zip(*m)) :{list(zip(*m))}")

# simplest zip example
idx = [1, 2, 3, 4]
record = zip(idx)
print(list(record))  # output: [(1,), (2,), (3,), (4,)]

# deal with unequal lists:
idx = [1, 2]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
record = zip(idx, leaders)

print(list(record))  # output:  [(1, 'Elon Mask'), (2, 'Tim Cook')]

# Unzip operation - uses trick using *param
record = [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]
idx, leaders = zip(*record)
print(idx)  # (1, 2, 3, 4)
print(leaders)  # ('Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou')

# Create and Update Dictionaries by the Zip Function
# With the help of the zip function, creating or updating a dict based on some separated lists is very simple.
# There are two one-line solutions:
# Using dict comprehension and zip
# Using dict function and zip

idx = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']

# create dict by dict comprehension
leader_dict = {i: name for i, name in zip(idx, leaders)}
print(leader_dict)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# create dict by dict function
leader_dict_2 = dict(zip(idx, leaders))
print(leader_dict_2)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# update
other_id = [5, 6]
other_leaders = ['Larry Page', 'Sergey Brin']
leader_dict.update(zip(other_id, other_leaders))
print(leader_dict)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou', 5: 'Larry Page', 6: 'Sergey Brin'}

# Use Zip function in For-Loops:
products = ["cherry", "strawberry", "banana"]
price = [2.5, 3, 5]
cost = [1, 1.5, 2]
for prod, p, c in zip(products, price, cost):
    print(f'The profit of a box of {prod} is £{p - c}!')


# The profit of a box of cherry is £1.5!
# The profit of a box of strawberry is £1.5!
# The profit of a box of banana is £3!

### 5 Uses of Asterisks in Python ###
# 1. Mathematics
# Single * for the multiplication operation.
# Double ** for the exponentiation operation.

# 2.To Receive an Unlimited Number of Arguments
def print_genius(*names):
    print(type(names))
    for n in names:
        print(n)


print_genius('Elon Mask', 'Mark Zuckerberg ', 'Larry Page')


# output:
# <class 'tuple'>
# Elon Mask
# Mark Zuckerberg
# Larry Page

def top_genius(**names):
    print(type(names))
    for k, v in names.items():
        print(k, v)


top_genius(Top1="Elon Mask", Top2="Mark Zuckerberg", Top3="Larry Page")


# output:
# <class 'dict'>
# Top1 Elon Mask
# Top2 Mark Zuckerberg
# Top3 Larry Page

# 3. Restrict to Keyword-Only Arguments
# A really cool usage of asterisks is to make a function can only receive keyword arguments
# just one * can restrict all following arguments must be passed as keyword arguments

def genius(*, first_name, last_name):
    print(first_name, last_name)


# genius('Yang','Zhou')
# TypeError: genius() takes 0 positional arguments but 2 were given
genius(first_name='Larry', last_name='Page')


# Larry Page

#  if we just would like to restrict a few arguments to be keyword-only and remain some positional arguments.
#  We can just put the positional arguments before the asterisk.

def genius(age, *, first_name, last_name):
    print(first_name, last_name, 'is', age)


genius(28, first_name='Larry', last_name='Page')
# Larry Page is 28

# 4. Iterables Unpacking
# We can use asterisks to unpack iterables, which will make our programs clear and elegant.
# For example, if we gonna combine different iterables, such as one list, one tuple and one set, into a new list
A = [1, 2, 3]
B = (4, 5, 6)
C = {7, 8, 9}
L = [a for a in A] + [b for b in B] + [c for c in C]
print(L)
# [1, 2, 3, 4, 5, 6, 8, 9, 7]

## Better is using *
A = [1, 2, 3]
B = (4, 5, 6)
C = {7, 8, 9}
L = [*A, *B, *C]
print(L)
# [1, 2, 3, 4, 5, 6, 8, 9, 7]

# 5.  Extended Iterable Unpacking
L = [1, 2, 3, 4, 5, 6, 7, 8]
a, *b = L
print(a)
# 1
print(b)
# [2, 3, 4, 5, 6, 7, 8]

# unpacking an iterable
[x for x in range(100)] == [*range(100)]  # True

# Example for using * to receive the middle elements
_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]
print(elements_in_the_middle)  # [2, 3, 4, 5, 6, 7]

# unpkacing dict keys
d = {'key1': 'A'}
list(d.keys()) == [*d]  # True

# unpacking whole dict
d == {**d}  # True

### REDUCE FUNCTIONS ###
print("===============")
print("REDUCE FUNCTIONS")

# Functions that recombine iterable recursively ending up with a single return value
# also called accumulator,aggregators or folding functions
# Example: find maximum of all the list of values - will use result = max(result,ai) where a is i-th element
# If list is: a0,a1,a2...an
# Each iteration is:
# result = a0
# result = max(result,a0)
# result = max(result,a1)
# ... till last element when result will be the max element in the list
from functools import reduce

l = [5, 2, 8, 6, 4, 9, 2, 1, 4]
min_result = reduce(lambda a, b: a if a < b else b, l)
print(f"Min Value in list is {min_result}")
max_result = reduce(lambda a, b: a if a > b else b, l)
print(f"Max Value in list is {max_result}")

### GLOBAL LOCAL SCOPES ####
print("===============")
print("GLOBAL LOCAL SCOPES")
# Python is familiar with scopes. The highest is Builtin scope (where defined True,list,print etc...)
# Next there is Global scope - all space that is outside of main() or any function
# Local scope is inside the function we work with
# When python encounter a function at complie-time it will scan for any variables that have values assigned to them
# It will search them anywhere in the function, if the variable has not been specified as global,then it is local
# If the variable is not found - only at run-time python will start looking higher in hierarchy to find the vars.
# You cannot change the value of a global variable just by mentioning it inside a function, you need to use 'global'


a = 10


def func1():
    print("Inside func1")
    print(f"a: {a}")  # there is no assignment or definition locally so it will print a: 10


def func2():
    print("Inside func2")
    a = 100  # Here python identifies a locally and the val is 100
    print(f"a: {a}")  # output: a:100


def func3():
    global a
    a = 200  # Here the assignment with global means we refer to a from globla scope so assignment of a = 200


def func4():
    # print(a)  #This will cause run-time error - because a is defined in the local scope but not yet, there is no
    # need to bring value from global scope where it exists, it is only run-time error ,at compile time it works
    print("Inside func4")
    a = 100
    print(f"a: {a}")  # output a:100  --> local


print(f"a: {a}")
func1()
func2()
func3()
print("after func3")
print(f"a: {a}")
func4()
print("after func4")
print(f"a: {a}")

print("## NONLOCAL EXAMPLE ##")


# When working with nested functions - nonlocal means we are working on variable that is not defined locally but one
# level scope above. ''nonlocal'' is not ''global''
def outer():
    x = 'hello'

    def inner1():
        x = 'python'

        def inner2():
            nonlocal x  # this means it is closure - x inside inner2 refers to x in inner1
            x = 'monty'

        print(f"inner before {x}")  # output: inner before python --> here x is still python
        inner2()
        print(f"inner after {x}")  # outpt: inner after monty --> inside inner2() the globla to inner2 is x from inner1

    inner1()
    print(f"outer {x}")  # output: outer hello -->The x of most global is not modified
    # - nonlocal of inner2 only relates to inner1


outer()
print("========================")
print("## ANOTHER NONLOCAL EXAMPLE ##")


def outer():
    x = 'hello'

    def inner1():
        nonlocal x
        x = 'python'

        def inner2():
            nonlocal x
            x = 'monty'

        print(f"inner before {x}")  # output: inner before python --> here x python and it changed x with 'hello'
        inner2()
        print(f"inner after {x}")  # outpt: inner after monty --> inside inner2() the globla to inner2 is x from inner1

    inner1()
    print(
        f"outer {x}")  # output: outer monty -->The x of most global was modified because of nonlocal defined in inner1


outer()
print("========================")
print("## THIRD NONLOCAL EXAMPLE ##")

x = 100


def outer():
    x = 'python'

    def inner1():
        nonlocal x
        x = 'monty'

        def inner2():
            global x
            x = 'hello'

        print(f"inner before {x}")  # output: inner before monty --> here x python and it changed x to monthy
        inner2()
        print(f"inner after {x}")  # outpt: inner after monty --> inside inner2() the global x 100 became hello

    inner1()
    print(f"outer {x}")  # output: outer monty -->The x is still monty


outer()
print(f"After outer call x is {x}")  # output: After outer call x is hello

### Difference between copy() and deepcopy() ###
print("========================")
print("## Difference between copy() and deepcopy() ##")
'''
A shallow copy constructs a new compound object and then (to the extent possible) 
inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, 
inserts copies into it of the objects found in the original.

A shallow copy means constructing a new collection object and then populating it with references 
to the child objects found in the original. In essence, a shallow copy is only one level deep. 
The copying process does not recurse and therefore won’t create copies of the child objects themselves.
A deep copy makes the copying process recursive. It means first constructing a new collection object and 
then recursively populating it with copies of the child objects found in the original. 
Copying an object this way walks the whole object tree to create a fully independent clone of the 
original object and all of its children.
'''
# example of shallow copy
first_list = [[1, 2, 3], ['a', 'b', 'c']]

second_list = first_list.copy()
print(f"id of first_list: {id(first_list)}, id of second_list: {id(second_list)}")
first_list[0][2] = 831

print(f"content of first_list: {first_list}")  # [[1, 2, 831], ['a', 'b', 'c']]
print(f"content of second_list: {second_list}")  # [[1, 2, 831], ['a', 'b', 'c']]

# example for the deepcopy() case
import copy

first_list = [[1, 2, 3], ['a', 'b', 'c']]

second_list = copy.deepcopy(first_list)
print(f"id of first_list: {id(first_list)}, id of second_list: {id(second_list)}")
first_list[0][2] = 831

print(f"content of first_list: {first_list}")  # [[1, 2, 831], ['a', 'b', 'c']]
print(f"content of second_list: {second_list}")  # [[1, 2, 3], ['a', 'b', 'c']]

# example of diff the copy() and deepcopy() or assignment
print("diff between copy() and deepcopy() or assinment")
import copy

x = 1
s = {7}

# create a list
l = [x, 5, s, {3}]

# copy!!!!!
m = l
n = l[:]
o = list(l)
p = copy.copy(l)
r = copy.deepcopy(l)

# shake things up
x += 1
l[1] += 1
s.add(8)
l[3].add(4)
l.append(2)

print(f"l is: {l}")  # l is: [1, 6, {8, 7}, {3, 4}, 2]
print(f"m is: {m}")  # m is: [1, 6, {8, 7}, {3, 4}, 2]
print(f"p is: {p}")  # p is: [1, 5, {8, 7}, {3, 4}]
print(f"r is: {r}")  # r is: [1, 5, {7}, {3}]

'''
Assignment m = l does not create a copy, it merely gives our list another name. 
All the modifications of l will be visible in m as well as they refer to the same object.
The following methods of copying lists are equivalent: n = l[:], o = list(l) and p = copy.copy(l). 
Altering mutable elements of the original list l will affect these shallow copies as well. 
(You can find more information about mutable and immutable variables here)
The only truly independent copy is r = copy.deepcopy(l). Altering the elements (mutable or immutable) 
in the original list l will not affect this copy.
'''

### CLOSURE ####
print("========================")
print("## CLOSURE ##")


class Averager:  # class example
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count


def averager():  # closure with functions example
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total / count

    return add


avg_func = averager()  # each add will calcultate total/count
print(avg_func(10))  # output: 10   --> 10/1
print(avg_func(20))  # output: 15   --> (10+20)/2

avg_instance = Averager()  # using instance of class
print(avg_instance.add(10))  # output: 10
print(avg_instance.add(20))  # output: 15

### DECORATORS ###
# Use this design pattern when 2 or more functions rely on another function
# Use this design pattern when a function has multiple responsibilities
# Use this design pattern when a function behavior needs to be extended
'''
@awesome_decorator
def my_function(agr1, agr2):
    return arg1 + arg2

is same as:
def my_function(arg1, arg2):
    # logic
my_function = awesome_decorator(my_function)

A decorator in Python can also be a class. 
In order to achieve that, we will pass the function to be decorated in __init__ and we will also
have to implement a special method, __call__. 
The call special method allows us to call the object of the class as we would call a function. 
Let’s refactor what we have above:

class awesome_decorator_class():
    def __init__(self, func):
        self.function = func

    def __call__(self, *arg, **kwargs):
        for arg in args:
            if arg < 0:
                raise Exception("Invalid Number!")
        return self.function(*args, **kwargs)


@awesome_decorator_class
def complicated_function(x, y, z):
    return x ** 2 + 10 * y - z

print(f"Complicated Computation: {complicated_function(-1, 15, 7)}")

'''

#
print("===============")
print("DECORATORS")


# Definition of general decorator
def dec(fn):
    print("Running Decorator")

    def inner(*args, **kwargs):
        print("Running Inner")
        return fn(*args, **kwargs)

    return inner


@dec
def my_func():
    print("Running myfunc")


my_func()
print("*********")


def dec_factory():
    print("Running dec_factory")

    def dec(fn):
        print("Running Decorator")

        def inner(*args, **kwargs):
            print("Running Inner")
            return fn(*args, **kwargs)

        return inner

    return dec


@dec_factory()  # is the same as:  my_func = dec_factory()(my_func)
def my_func():
    print("Running myfunc")


my_func()
print("*********")


def dec_factory(a, b):  # decorator factory with params - to create decorator that passes params
    print("Running dec_factory")

    def dec(fn):
        print("Running Decorator")

        def inner(*args, **kwargs):
            print("Running Inner")
            print(f"a={a},b={b}")
            return fn(*args, **kwargs)

        return inner

    return dec


@dec_factory(100, 200)
def my_func():
    print("Running myfunc")


my_func()

print("====+++====")
print("Using Class as decorator:")


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        print("Calling __call__")

        def inner(*args, **kwargs):
            print("Inside Inner")
            print(f"decorated call function called: a={self.a}, b={self.b}")
            return fn(*args, **kwargs)

        return inner


@MyClass(10, 20)
def my_func(s):
    print("Inside my_func")
    print(f"Hello {s}!")


# This is the same as creating instance: obj=MyClass(10,20)
# and then:  my_func = obj(my_func)

my_func('World')
print("====+++====")

## Decorating a class ##
from datetime import datetime, timezone


def info(self):
    results = []
    today = datetime.today()
    results.append(f"time: {today:%d/%m/%y}")
    results.append(f"Class: {self.__class__.__name__}")
    results.append(f"id: {hex(id(self))}")
    for k, v in vars(self).items():
        results.append(f"{k}:{v}")
    return results


def debug_info(cls):
    cls.debug = info  # this is attribute added to the class dynamically
    return cls


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi(self):
        return 'Hello There!'


p = Person('Dan', 1972)
print(p.debug())  # output: ['time: 10/02/21', 'Class: Person', 'id: 0x284cdfadfd0', 'name:Dan', 'birth_year:1972']


def timed(fn):  # decorator for measure time
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k}={v}" for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print((f"{fn.__name__}({args_str}) took {elapsed:.6f}s to run"))
        print(result)

        return result

    return inner


# fibonachi calculation with list comprehension for example 10 first occurances
fibo = [0, 1]
[fibo.append(fibo[-2] + fibo[-1]) for i in range(8)]


# fibonachi_recorsion
def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n - 1) + calc_recursive_fib(n - 2)


@timed
def fib_recursive(n):
    return calc_recursive_fib(n)


# fibonachi_loop
@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


# fibonachi_func_with_cache
def memorize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@memorize
def fib(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]


fib_recursive(30)  # output: fib_recursive(30) took 0.145620s to run
fib_loop(30)  # output: fib_loop(30) took 0.000010s to run

from time import perf_counter

start = perf_counter()
fib_instance = Fib()
end = perf_counter()
print((f"fib_instance took {end - start:.6f}s to run"))  # output: fib_instance took 0.000004s to run
print(fib_instance.fib(30))

print(f"Fibonatch with cache: {fib(30)}")  # output: Fibonatch with cache: 832040

## simple time measure decorator example ###
import time


def time_measure(f):
    t0 = time.time()
    f()
    t = time.time()
    return t - t0


@time_measure
def slow_code():
    time.sleep(2)


print(slow_code)  # output: 2.011594533920288
print("=========&&&&&&&*********&&&&&&&&=======")


## Another simple decorator example ###
def print_argument(func):
    def wrapper(the_number):
        print("Decorator added explanation: Argument for", func.__name__, "is", the_number)
        return func(the_number)

    return wrapper


@print_argument
def add_one(x):
    return x + 1


print(f"The result is: {add_one(1)}")
#######################################

### SINGLE DISPATCH GENERIC FUNCTION ####
print("=====================")
print("SINGLE DISPATCH")


# In python ,because it is dynamic typed - there is no function overloading
# the types of params and their number cannot differentiate between functions
# Sometimes we need different functions according to arguments(their types or num of arguments)

# The first way to do it is by creating dictionary where key=type,value=function reference

def pr_string(inp):
    print(f"This is a string: {inp}")


def pr_int(inp):
    print(f"This is an int: {inp}")


def pr_float(inp):
    print(f"This is float: {inp:.4f}")


def pr_none(inp):
    print(f"There is nothing to print")


def func_inp(inp):
    registry = {
        object: pr_none,
        int: pr_int,
        float: pr_float,
        str: pr_string
    }
    fn = registry.get(type(inp))
    return fn(inp)


func_inp(4)  # output: This is an int: 4
func_inp(1.1)  # output: This is float: 1.1000
func_inp("dan")  # output: This is a string: dan

print("++ Now for Single Dispatch inner implementation ++")


def singledispatch(fn):
    registry = {}

    def decorated(arg):
        return registry.get(type(arg))(arg)

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn

        return inner

    decorated.register = register
    return decorated


@singledispatch
def func_arg(inp):
    return inp


@func_arg.register(int)  # the operation here is: pr_int = func_arg.register(int)(pr_int)
def pr_int(inp):
    print(f"This is the new int: {inp}")
    return


@func_arg.register(float)
def pr_float(inp):
    print(f"This is new float: {inp:.4f}")


func_arg(4)
func_arg(4.1)

print("++ Using singledispatch from functools ++")
from functools import singledispatch
from decimal import Decimal


@singledispatch
def fun(s):
    print(s.upper())


@fun.register(int)
def _1(s):
    print(s * 2)


@fun.register(list)
def _2(s):
    for i, e in enumerate(s): print(i, e)


fun('Oklahoma')  # output: OKLAHOMA
fun(10)  # output: 20
fun(['g', 'e', 'e', 'k', 's'])


@fun.register(float)
@fun.register(Decimal)
def _3(s):
    print(round(s, 2))


fun(2.3456789)  # output: 2.35
fun(Decimal(4.897))  # output: 4.90

# dispatch() – To check which implementation will the generic function choose for a given type.
print(fun.dispatch(dict))  # output: <function fun at 0x0000021BEDFCD3A0>
print(fun.dispatch(list))  # output: <function _2 at 0x0000021BEDFF89D0>

# registry() – read-only attribute to access all registered implementations.
print(fun.registry.keys())  # output: dict_keys([<class 'object'>, <class 'int'>, <class 'list'>...
print(fun.registry[int])  # output: <function _1 at 0x000002C4468F8940>
print(fun.registry[object])  # output: <function fun at 0x000002C4468CD3A0>

### EXCEPTION RAISE ERROR ###
print("===============")
print("EXCEPTION RAISE ERRORS")


def colorize(text, color):
    colors = ["RED", "GREEN", "BLUE"]
    if type(color) is not str:
        raise TypeError("color must be string")
    if type(text) is not str:
        raise TypeError("text must be string")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")


# colorize(1,"blue") #TypeError: text must be string
# colorize("dan",10) #TypeError: color must be string
# colorize("dan","blue") #ValueError: color is invalid color

### TRY/EXCEPT Blocks ###
print("===============")
print("TRY_EXCEPT Blocks")


def divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong!")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")
    finally:
        print("==Will be printed anyway==")


print(divide(1, 2))
print(divide(1, 'a'))  # unsupported operand type(s) for /: 'int' and 'str'
print(divide(1, 0))  # division by zero


# How to create your own exception
class ExceptionA(Exception):
    pass


class ExceptionB(Exception):
    pass


for i in range(4):
    try:
        if i % 2 == 0:
            raise ExceptionA
        else:
            raise ExceptionB
    except ExceptionA:
        print('ExceptionA caught')
    except ExceptionB:
        print('ExceptionB caught')

### OPERATOR OVERLOADING ###
print("===============")
print("OPERATOR OVERLOADING")


# Example for implemet print(__str__ or __repr__) and +

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(4, 5)
print(p2)  # (4,5)
p3 = p1 + p2
print(p3)  # (5,7)

### CLASS ###
print("===============")
print("CLASS")


# regular class
class ClassSample:
    class_attribute = 0  # this attribute is known to any instance of the class

    # class attribute is a variable which belongs to a class rather than a particular instance.
    # All instances of this class can access it and it is defined outside the constructor function.

    def __init__(self, attr1, attr2=0):
        self.instance_attr1 = attr1
        self.instance_attr2 = attr2
        # An instance attribute inside the constructor function is a variable belonging
        # to a particular instance of a class. This variable is only accessible in this
        # instance rather than the class. If we call a instance attribute by the class,
        # there will be a AttributeError.
        self._private = "This is like private but can be accessed directly in main"
        self.__hidden = "This really can't be accessed in main\n \
        only by _ClassSample__hidden if need to access from main"
        self.__dunder__ = "Not recommended to use such function - only for python"
        ClassSample.class_attribute += 1  # counter of number of instances

    # A class method is a method which first parameter is the class itself[cls] to represent this mandatory parameter.
    # a class method can be called by class directly or by an instance but an instance method can only be called
    # by an instance.
    @classmethod
    def func_handle_class_attribute(cls, inp):
        print(f"This is method related to class attribute: {cls.class_attribute} and can use {inp}")

    # Static method is a method within a class that doesn’t have parameters of the class or instance. 
    @staticmethod
    def func_as_utility_not_related_to_cls():
        print(f"This is utility and {ClassSample.class_attribute} is not related to it")

    def instance_method(self, inp):  # instance methods, which first parameter is self.
        # The 'self' represents the current instance itself.
        print(f"This is instance_method with value {self._private} that receives {inp}")

    def logged_out(self):  # instance_method
        ClassSample.class_attribute -= 1  # decrease number when logged out

    def print(self):  # instance_method
        print(f"We have {self.instance_attr1} & {self.instance_attr2} also have {self._private} and {self.__hidden} ")
        print(f"And our count is {ClassSample.class_attribute}")

    def __repr__(self):
        rep = "This method pretty the print of the instance ,i.e.: print(instance) is shown in __repr__"
        return rep

    # function dir(instance) can show all methods and attributes of the class

    # Getters:- These are the methods used in Object-Oriented Programming (OOPS)
    # which helps to access the private attributes from a class.
    # Setters:- These are the methods used in OOPS feature
    # which helps to set the value to private attributes in a class.

    # @property replace getter and setter
    @property
    def priv(self):
        return self._private

    @priv.setter
    def priv(self, new_val):
        # value_if_true if condition else value_if_false
        self._private = new_val if new_val > 0 and new_val % 2 == 0 else 2


cs = ClassSample(123)
cs1 = ClassSample(321)
cs.print()
cs.priv = 445
print(f"The value of _private in cs instance is {cs.priv}")

'''
Instance method has a mandatory first attribute self which represent the instance itself. 
Instance method must be called by a instantiated instance.
Class method has a mandatory first attribute cls which represent the class itself. 
Class method can be called by an instance or by the class directly. 
Its most common using scenario is to define a factory method.
Static method doesn’t have any attributes of instances or the class. 
It also can be called by an instance or by the class directly. 
Its most common using scenario is to define some helper or utility functions which are closely relative to the class.

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def get_from_string(cls, name_string: str):
        first_name, last_name = name_string.split()
        if Student.validate_name(first_name) and Student.validate_name(last_name):
            return cls(first_name, last_name)
        else:
            print('Invalid Names')

    @staticmethod
    def validate_name(name):
        return len(name) <= 10


Yang = Student.get_from_string('yang zhou')
print(Yang.first_name) # yang
print(Yang.last_name) # zhou
'''
### STATIC VAR AND METHOD IN CLASS ###
print("===============")
print("STATIC VAR AND METHOD IN CLASS")


class Employee:  # create Employee class name
    dept = 'Information technology'  # define class variable == static variable

    def __init__(self, name, id):
        self.name = name  # instance variable
        self.id = id  # instance variable


# Define the objects of Employee class
emp1 = Employee('John', 'E101')
emp2 = Employee('Marcus', 'E105')

print(emp1.dept)  # Information technology
print(emp2.dept)  # Information technology
print(emp1.name)  # John
print(emp2.name)  # Marcus
print(emp1.id)  # E101
print(emp2.id)  # E105

# Access class variable using the class name
print(Employee.dept)  # Information technology   # print the department

# change the department of particular instance
emp1.dept = 'Networking'
print(emp1.dept)  # Networking
print(emp2.dept)  # Information technology

# change the department for all instances of the class
Employee.dept = 'Database Administration'
print(emp1.dept)  # Networking
print(emp2.dept)  # Database Administration

# Python has a static method that belongs to the class.
# It is just like a static variable that bounds to the class rather than the class's object.
# A static method can be called without creating an object for the class.
# It means we can directly call the static method with the reference of the class name.
# Furthermore, a static method is constrained with a class; hence it cannot change the state of an object.
# A static method in Python related to the class.
# It can be called directly from the class by reference to a class name.
# It cannot access the class attributes in the Python program.
# It is bound only to the class. So it cannot modify the state of the object
# It is also used to divide the utility methods for the class.
# It can only be defined inside a class but not to the objects of the class.
# All the objects of the class share only one copy of the static method.
# Define static method: Using the @staticmethod Decorator

# STATIC METHODS
print("                     ")
print("=== STATIC METHOD ===")


class Marks:
    @staticmethod
    def Math_num(a, b):  # define the static Math_num() function
        return a + b

    @staticmethod
    def Sci_num(a, b):  # define the static Sci_num() function
        return a + b

    @staticmethod
    def Eng_num(a, b):  # define the static Eng_num() function
        return a + b

    # print the total marks in Maths


print(" Total Marks in Maths", Marks.Math_num(64, 28))  # Total Marks in Maths 92

# print the total marks in Science
print(" Total Marks in Science", Marks.Sci_num(70, 25))  # Total Marks in Science 95

# print the total marks in English
print(" Total Marks in English", Marks.Eng_num(65, 30))  # Total Marks in English 95

print("                     ")

### Creating Custom Ctor and Custome Dtor ###
print("===============")
print("Creating Custom Ctor and Custome Dtor")


# Creating Custom Ctor and Custome Dtor
class C:
    def __init__(self):
        print("Contructor")

    def pr(self):
        print("Hello!!")

    def __del__(self):
        print("Destructor")


c = C()
c.pr()


# output: Constructor\nHello!!\nDestructor

# Demonstrating the work of __enter__ and __exit__ methods
class C:
    def some_work(self):
        print("Some work being Done!")

    def __enter__(self):
        print("ENTER")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT")


obj = C()
with obj:
    # as soon as you have 'with' you work with __enter__ & __exit__
    obj.some_work()
####output:
# ENTER
# Some work being Done!
# EXIT
######


### INHERITANCE ###
print("===============")
print("INHERITANCE")


# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def __repr__(self):
        return f"My name is {self.firstname} {self.lastname}"

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, school_name):
        super().__init__(fname, lname)
        self.uninversity = school_name

    def __repr__(self):
        return f"The student {self.firstname} {self.lastname} is studing in {self.uninversity} university"


st = Student("Mike", "Pence", "UCLA")
print(st)  # The student Mike Pence is studing in UCLA university


# You can call the parent class’s initializer using super() or parent class’s name
## using super()
class Parent:
    def __init__(self, city, address):
        self.city = city
        self.address = address


class Child(Parent):
    def __init__(self, city, address, university):
        super().__init__(city, address)
        self.university = university


child = Child('Zürich', 'Rämistrasse 101', 'ETH Zürich')
print(child.university)  # ETH Zürich


## using parent's class name
class Parent:
    def __init__(self, city, address):
        self.city = city
        self.address = address


class Child(Parent):
    def __init__(self, city, address, university):
        Parent.__init__(self, city, address)
        self.university = university


child = Child('Zürich', 'Rämistrasse 101', 'ETH Zürich')
print(child.university)  # ETH Zürich


##  Note that calls to parent initializers using __init__() and super()
## can only be used inside the child class’s initializer.

##### private & protected used #####
class Base(object):
    def __private(self):
        print("private value in Base")

    def _protected(self):
        print("protected value in Base")

    def public(self):
        print("public value in Base")
        self.__private()
        self._protected()


class Derived(Base):
    def __private(self):
        print("derived private")

    def _protected(self):
        print("derived protected")


d = Derived()
d.public()
'''
Output:
public value in Base
private value in Base
derived protected

Explain:
derived is not implementing public so public is Base
Because __private is a private method, only the object itself could use it, 
there is no naming conflict for a private method. Calling d.__prvate() will cause an Error
derive protected related to self of derived is chosen
'''

####################
### POLYMORPHISM ###
print("===============")
print("POLYMORPHISM")


# In OOP object can take many forms
# 1. same class method works in similar way for different classes
# parent.speak(), child1.speak() ,child2.speak() - child1 & child 2 inherites same parent
# 2. The same operation works for different kinds of objects
# len method works similar on list ,tuple or string
# The 1 section is deployed usually as parent class that has class method and child override the method to fit them

class Parent():
    def __init__(self, name):
        self.name = name
        print(f"This is init of parent named {self.name}")

    def mtd(self):
        print(f"Parent method named {self.name}")


class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"This is init of Child1 named {self.name}")

    def mtd(self):
        super().mtd()
        print(f"Child1 method with age {self.age} and named {self.name}")


class Child2(Parent):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id
        print(f"This is init of Child2 named {self.name}")

    def mtd(self):
        super().mtd()
        print(f"Child2 method with id {self.id} and named {self.name}")


c1 = Child1("c1", 11)
c2 = Child2("c2", 1234)
c1.mtd()
c2.mtd()
c3 = Child1("c3", 22)
c4 = Child2("c4", 4321)
c5 = Child1("c5", 33)
c6 = Child2("c6", 5678)

lst = [c1, c2, c3, c4, c5, c6]
for i in lst:
    i.mtd()  # this is actually polymorphism

### ABSTRACTION ###
print("===============")
print("ABSTRACTION")

'''
Abstraction is used to hide the internal functionality of the function from the users. 
By applying abstraction, each object is only exposed to a high-level mechanism for using it. 
A method that only has a declaration and not a definition is called an abstract method. 
An abstract method doesn’t have anything inside the body. 
A class that has an abstract method is called an abstract class.
Python by default does not support abstract classes, but there is a module named abc that 
allows Python to create abstract methods and classes.
'''

from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


# com = Computer()
# com.process()
# ---------------------------------
# TypeError: Can't instantiate abstract class Computer with abstract method process

'''
You can’t create objects for abstract classes. 
To access the abstract class and its methods, you need to use inheritance.
'''

import abc


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y):
        self.l = x
        self.b = y

    def area(self):
        return self.l * self.b


r = Rectangle(10, 20)
print('area: ', r.area())
'''
Some Things To Remember on Classes on general:
A method inside the class without self can only use class attributes.
Class and instance attributes are both accessible using the object of the class.
You don't need to call the constructor __init__. It is automatically called at the time of object creation.
A child class can access all the attributes of the parent class, but it does not happen vice versa.
To access a protected member, we need to use _ at the time of accessing it through an object or class member.
You can’t create objects for abstract classes
'''

# ITERATORS VS ITERABLES
print("====================")
print("ITERATORS VS ITERABLES")

# Iterator = Object that returns data each time next() is called on it. Like pointer it = iter(var) == it is iterator.
# var is the iterable, we can do next() on iterator ,i.e.: next(it) bring next char in string
# Iterable = Object that returns an iterator when iter() is called on it.Data strcuture we can loop upon like list,str..
# next(string) will not work, next(iterator_to_string) will work.
# To make a class an Iterable we need to define __iter__() method
# To loop on the class - we need to define __next__() method

'''
Difference between iterables and iterators?
Ans: iterable: An iterable is an object, which one can iterate over. 
In the case of iterable whole data is stored in the memory at a time.
iterators: an iterator is an object used to iterate over an object. 
it is only being initialized or stored in the memory when it is called. 
iterators has next using which elements are fetched out from the object.

### List is an iterable
lst = [1,2,3,4,5]
for i in lst:
    print(i)
### iterator
lst1 = iter(lst)   
next(lst1)
>1
next(lst1)
>2
for i in lst1:
    print(i)
>3,4,5      
'''


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
            func(thing)
        except StopIteration:
            break


ls = [1, 2, 3]
name = "Dan"
my_for(ls, print)
my_for(name, print)

print("Counter iterable example:")


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for x in Counter(10, 15):
    print(x)


# Another basic example of custome iterator
class C:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n += 1
        return self.n


c = C()
i = iter(c)  # get an iterator

for _ in range(5):
    # use the iterator
    print(next(i))  # output: 1 2 3 4 5

# GENERATORS
print("====================")
print("GENERATORS")

# Generators are iterators
# Can be created with generator functions
# use yield keyword
# Can be created with generator expressions

'''
We can create our own generators by writing functions that use the yield keyword instead of return. 
Return will fetch something, give it back to us and exit the function. 
With yield we can create a sequence and then we iterate over it when we need to. 
Yield does not stop the execution of the function, we can have logic after it too and it ‘remembers’ its previous value. 
Let’s take a look by implementing our own range, that will give us squares of the numbers we pass as arguments:
def squares(a, b):
    i = a
    while i < b:
        yield i**2
        i += 1
        
Of course, we can use for to iterate, just like any other sequence we have seen before, 
or we can use the next() function to access the next element in our sequence, after we bind it to a variable. 
This is similar to the .next() special iterator method we have in Java. Try running the following snippets:
for num in squares(5, 10):
    print(num)
sequene = squares(5, 10
print(next(sequene))
print(next(sequene))`*        

Difference between list comprehension(return) and generator comprehention: 
my_nums = [x*x for x in [1, 2, 3, 4, 5]] #list comprehension
my_nums1 = (x*x for x in [1, 2, 3, 4, 5]) #generator comprehension
print(my_nums)  #output:  [1,4,9,16,25]
print(my_nums1) #output:  <generator object <genexpr> at 0x000001C727BFDF20>

for num in my_nums:
  print(num)  # [1, 4, 9, 16, 25]

for num in my_nums1:
  print(num)  # 1 4 9 16 25
        
'''


# Generator functions are functions but do not use 'return' they use 'yield'
# Generator functions are not return once like regular functions but can yield multiple times
# Generator functions when invoked returns generator , regular functions return value

def gen(max):
    count = 1
    while count <= max:
        yield count
        count += 1


def week():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in days:
        yield day


for i in gen(5):
    print(i)

for day in week():
    print(day)

# Different generators working independently
print("Different Generators:")


def f():
    for i in range(10):
        yield i  # not 'return'


g1 = f()  # first generator object
g2 = f()  # second generator object

print(next(g1))  # val from generator 1 #output: 0
print(next(g2))  # val from generator 2 #output: 0
print(next(g1))  # val from generator 1 #output: 1
print(next(g2))  # val from generator 2 #output: 1
print(next(g1))  # val from generator 1 #output: 2
print(next(g2))  # val from generator 2 #output: 2

## Another Example
'''
Consider an example where we want to generate a sequence of numbers (up to 100 Million) in our program 
(like auto-incremented ids). We can solve this problem easily with the generator.'''


def generate_ids(limit):
    for id in range(1, limit + 1):
        yield id


ids = generate_ids(10000000)
print("Generate example")
print(next(ids))  # 1
print(next(ids))  # 2
print(next(ids))  # 3

'''
Using Generator Comprehensions, we can save our memory. 
It works the same as List Comprehension, but instead of creating a list and keeping the whole sequence in memory, 
the generator generates the next item in demand.
'''
print("Compare list comprehension and generator comprehension: ")
# list comprehension
my_list = [i for i in range(1000)]
print(f"summary of list: is {sum(my_list)}")
print(f"sizeof memory is: {sys.getsizeof(my_list)} bytes")  # 8856 bytes

# generator comprehension
my_gene = (i for i in range(1000))
print(f"summary of generator: is {sum(my_gene)}")
print(f"sizeof memory is: {sys.getsizeof(my_gene)} bytes")  # 112 bytes

# Generator Comprehension = reduces the speed of creation and optimizes memory allocation
my_list = [1, 2, 3, 4, 5]
my_gen_expr = (x * 2 for x in my_list)

print(f"next(my_gen_expr): {next(my_gen_expr)}")  # output: next(my_gen_expr): 2
print(f"next(my_gen_expr): {next(my_gen_expr)}")  # output: next(my_gen_expr): 4
print("---- Notice Generator is statefull - saves the last value so we continue from 6 not from 2 as before ---")
for x in my_gen_expr:
    print(f"x = {x}")  # output: x = 6  x = 8 x = 10

# Generator Comprehension example:
print("=== Generator Comprehension Example: ====")


# Regular Generator
def generate_up_to(n):
    for i in range(n):
        print("Generated number ", i)
        yield i


generator = generate_up_to(5)

next(generator)
next(generator)
next(generator)
next(generator)
next(generator)
print("===~~~~~~~~~~===")
# Generator comprehension phrase
n = 5
generator = (print("Generated number ", i) for i in range(n))

next(generator)
next(generator)
next(generator)
next(generator)
next(generator)

# PICKLE
print("====================")
print("PICKLE")
'''
Pickling is the process in which a python object hierarch is converted into a byte stream 
Unpickling is the inverse process in which a byte stream is converted into an object
'''

# We can serialize simple objects on files - it is called pickle

import json
import pickle


class SomeClass:
    def __init__(self, name="", family="", age=0):
        self.name = name
        self.family = family
        self.age = age

    def __repr__(self):
        return f"This is {self.name} {self.family} aged {self.age}"


man = SomeClass("Dan", "Belfer", 48)
print(man)  # output: This is Dan Belfer aged 48

json_structure = json.dumps(man.__dict__)  # saved in json like a dictionary
print(json_structure)  # output: {"name": "Dan", "family": "Belfer", "age": 48}

# To pickle an object: Serialize it
with open("people.pickle", "wb") as file:
    pickle.dump(man, file)

# To unpickle something:
with open("people.pickle", "rb") as file:
    new_man = pickle.load(file)
    print(new_man)  # output: This is Dan Belfer aged 48

### CLEAN CODE SAMPLES ###
print("====================")
print("CLEAN CODE SAMPLES")


# How to ease with nested if else conditions?
class Check():
    def __init__(self):
        pass

    def has_logged_in(self):
        pass

    def has_role(self):
        pass

    def has_funds(self):
        pass

    def is_root(self):
        pass


check = Check()


# This is the complicated nested checks
def nested_check():
    print("This is a nested check..")
    if check.has_logged_in():
        if check.has_role():
            print("You have access")
            if check.has_funds():
                print("You can buy it")
            else:
                print("Please add more funds")
        elif check.is_root():
            print("You have access")
        else:
            print("You do not have access to this area")
    else:
        print("You must be logged in")


# This is the clean easy to understand same solution like nested one - it is better!
def flat_check():
    print("This is a flat check..")
    if check.is_root():
        print("You have access")
        return
    if not check.has_logged_in():
        print("You must be logged in")
        return
    if not check.has_role():
        print("You must have the correct role")
        return
    if not check.has_funds():
        print("Please add more funds..")
        return
    print("You have access")


# How to improve work with dictionary?
name = {'first_name': 'Dan', 'last_name': 'Belfer'}
job = {'company': 'Argus', 'role': 'QA Engineer'}
contact = {'email': 'blabla', 'twiter': 'stam'}
"""We want to merge the 3 dictionaries to one dictionary"""
""""Example 1 : Very complicated way"""
items = [name, job, contact]
profile1 = {}

for i in items:
    for s in i:
        profile1[s] = i[s]

print("Example1: Multiple for loops")
print(profile1)

""""Example 2 : Pythonic update dictionary"""
profile2 = {}
profile2.update(name)
profile2.update(job)
profile2.update(contact)

print("Example 2: merge 2 dictionaries")
print(profile2)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}

print("Example 3: Pythonic ** a dictionary")
print(merged)
# {'a': 1, 'b': 3, 'c': 4}

# Since Python 3.9 merging - with |

# Python >= 3.9 only
merged3_9 = dict1 | dict2
print("Example 4: Since Python 3.9 | a dictionary")
print(merged3_9)
# {'a': 1, 'b': 3, 'c': 4}

# Find the Most Frequent Element of a List
nums = [2, 2, 6, 2, 2, 3, 4, 2, 113, 2, 1]
print(f"Most frequent element in list: {max(set(nums), key=nums.count)}")  # 2

# How to work with multiple if else conditions?
print("Working with Multiple if else conditions:")
from enum import IntEnum


class StatusE(IntEnum):
    OPEN = 1
    IN_PROGRESS = 2
    CLOSED = 3


def handle_open_status():
    print('Handling open status')


def handle_in_progress_status():
    print('Handling in progress status')


def handle_closed_status():
    print('Handling closed status')


handlers = {
    StatusE.OPEN.value: handle_open_status,
    StatusE.IN_PROGRESS.value: handle_in_progress_status,
    StatusE.CLOSED.value: handle_closed_status
}


def handle_status_change(status):
    if status not in handlers:
        raise Exception(f'No handler found for status: {status}')
    handler = handlers[status]
    handler()


handle_status_change(StatusE.OPEN.value)  # Handling open status
handle_status_change(StatusE.IN_PROGRESS.value)  # Handling in progress status
handle_status_change(StatusE.CLOSED.value)  # Handling closed status
# handle_status_change(4)  # Will raise the exception

## Multiple conditions at a single if-statement
math_points = 51
biology_points = 78
physics_points = 56
history_points = 72

my_conditions = [math_points > 50, biology_points > 50,
                 physics_points > 50, history_points > 50]

if all(my_conditions):
    print("Congratulations! You have passed all of the exams.")  # Congratulations! You have passed all of the exams.
else:
    print("I am sorry, but it seems that you have to repeat at least one exam.")

## At least one condition is met out of many in a single if-statement
math_points = 51
biology_points = 78
physics_points = 56
history_points = 72

my_conditions = [math_points > 50, biology_points > 50,
                 physics_points > 50, history_points > 50]

if any(my_conditions):
    print("Congratulations! You have passed all of the exams.")  # Congratulations! You have passed all of the exams.
else:
    print("I am sorry, but it seems that you have to repeat at least one exam.")

## Using * and ** for Function Argument Unpacking ##
print("=====================")
print("Using * and ** for Function Argument Unpacking")


# You can unpack a dictionary for use with named keywords by using the ** prefix:
def f(a, b):
    print(a, b)


args = {"a": 1, "b": 2}
f(**args)  # output: 1 2


#  we can use single * to unpack an array and feed its content as positional arguments to a function:
def f(a, b, c):
    print(a, b, c)


l = [1, 2, 3]
f(*l)  # output: 1 2 3

## FIND SUBSTRING ##
print("=====================")
print("FIND SUBSTRING")

# Find substring in long string
# Useful when you are finding substring in a string, in 2 ways:

programmers = ["I'm an expert Python Programmer",
               "I'm an expert Javascript Programmer",
               "I'm a professional Python Programmer",
               "I'm a beginner C++ Programmer"]
# method 1
for p in programmers:
    if p.find("Python") != -1:
        print(p)

print("~~~~~~~~~~~~~~~~~~~~")

# method 2
for p in programmers:
    if "Python" in p:
        print(p)

# Use pathlib to read files without using a with context manager
'''
The pathlib module offers a number of conveniences for working with file system paths and files on your file system
One particular convenience offered by pathlib is the pathlib.Path.read_text method. 
pathlib.Path.read_text lets you read the contents of a file without explicitly using a context manager:

from pathlib import Path

contents = Path("example-file.txt").read_text()
print(contents)

In the above example, you instantiate a Path object with the path you are interested in opening: example-file.txt. 
Calling the read_text method of the new Path object returns the text contained in the underlying file. 
The value of contents is the same as the value of contents in the first example.
In case you are concerned about files being closed properly, note that Path.read_text uses 
a with context manager under the hood to ensure that the underlying file is closed appropriately. 
The with context manager is still in play to ensure the file is closed for you, just abstracted away.
Path also offers three related additional methods beyond read_text. Namely: read_bytes, write_text, and write_bytes. 
With these four methods, you can cover the majority of your file reading/writing needs without 
repeatedly writing with open(...) context managers.
As you start working more withPath objects, you’ll also find that Path objects can augment 
and improve on functions you’re used to importing from the os module.
'''

#### CONTEXT MANAGER ####
print("=====================")
print("CONTEXT MANAGERS")
## this is a class defined to solve the example of writing to file many times - use class to handle open/close file
print("class solution to handle file")


class FileHandler:

    def __init__(self, filename, mode):
        print("----")
        print("Loading " + filename)
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening the file")
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print("Closing the file")
        self.open_file.close()


for _ in range(5):
    with FileHandler('temp.txt', 'w') as f:
        f.write('Hello World - From good example')

print("context manager solution to open/close file")
from contextlib import contextmanager


@contextmanager
def file_handler(path, mode):
    print("----")
    print("Opening the file")
    resource = open(path, mode)
    yield resource
    print("Closing the file")
    resource.close()


for _ in range(5):
    with file_handler('temp.txt', 'w') as f:
        f.write('Hello World - From better example')

#### ASSERT ####
print("=====================")
print("ASSERT")

x = "hello"
# if condition returns True, then nothing happens:
assert x == "hello"


# if condition returns False, AssertionError is raised:
# assert x == "goodbye"

# if condition returns False, AssertionError is raised:
# assert x == "goodbye", "x should be 'hello'"

# using assert to break the program if your data is wrong
def divide(x, y):
    assert y != 0
    return x / y


a = divide(100, 10)  # OK
print(f"Val of division is: {a}")

# a = divide(100,0) #ERROR
# print(f"Val of division is: {a}") #will not be printed


#### MEMORY USAGE ####
print("=====================")
print("MEMORY USAGE")

import sys

mylist = range(0, 10000)
print(f"Memory Usage of Mylist is {sys.getsizeof(mylist)}")  # output: 48

#  why is this huge list only 48 bytes?
'''It’s because the range function returns a class that only behaves like a list. 
A range is a lot more memory efficient than using an actual list of numbers.
You can see for yourself by using a list comprehension to create an actual list of numbers from the same range:'''
import sys

myreallist = [x for x in range(0, 10000)]
print(f"Memory Usage of My real list is {sys.getsizeof(myreallist)}")

#### PPRINT BETTER OUTPUT ####
print("=====================")
print("PPRINT BETTER OUTPUT")

import requests
from pprint import pprint

url = 'https://api.github.com/users/belfd'
user = requests.get(url).json()
print("+++  Ugly  +++")
print(user)
print("+++  Beutiful  +++")
pprint(user)

#### TIMEIT ####
print("=====================")
print("TIMEIT = to calculate the runtime of our code")

import timeit

code = '''
def fun():
    sum=0
    for i in range(1000000):
        sum+=i
    return sum
'''
print(f'timeit 1st example, measured {timeit.timeit(stmt=code)}')


def f(x):
    return x ** 2


def g(x):
    return x ** 4


def h(x):
    return x ** 8


print("timeit 2nd example, measured: ".strip())
print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))

### REPLACEMENT to SWITCH CASE ######
print("=====================")
print("REPLACEMENT to SWITCH CASE")

'''
{'option1': function1,
 'option2': function2,
 'option3': function3,
 'option4': function4}[value]()
'''


def first_case():
    print("first")


def second_case():
    print("second")


def third_case():
    print("third")


mycase = {
    'first': first_case,  # do not use ()
    'second': second_case,  # do not use ()
    'third': third_case  # do not use ()
}
myfunc = mycase['first']
myfunc()  # output: first


## if only working with values
def f(x):
    return {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }.get(x, 9)  # 9 is default if x not found


print(f('c'))  # output: 3

### MUTABLE DEFAULT PROBLEM!!! ######
print("=====================")
print("MUTABLE DEFAULT PROBLEM!!!")
'''
This is a nifty little trick that has more benefits than it appears.
BUT SHOULD be handled Carefully! 
Every call will create new list and append 1.. or that is what intended..

def something(x=[]):
    x.append(1)
    print (x)

output:
>>> something()
[1]>>> something()
[1, 1]>>> something()
[1, 1, 1]

The list gets appended every time you use this function. BOOM!!!
Default argument that receives list,dicts (any mutable) is changed after assignment 
Instead, you should use a default value denoting "not indicated" 
and replace with the mutable you'd like as default:
'''


# def something(x= None):
#     if x is None:
#         x= []
#     x.append(1)
#     print (x)


def something(x=[]):
    x = x if x else []
    x.append(1)
    print(x)


something()  # output: [1]
something()  # output: [1]

### COUNTING OCCURENCES IN LIST ###
print("===========================")
print("COUNTING OCCURRENCES IN LIST")

from collections import Counter

mylist = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
c = Counter(mylist)
print(f"Original list: {mylist}")
print(f"Counted times: {c}")
# Counter({1: 2, 2: 1, 3: 1, 4: 1, 5: 3, 6: 2})

# And it works on strings too:
strt = "aaaaabbbbbccccc"
print(f"String is: {strt}")
print(f"Count of Chars: {Counter(strt)}")
# Counter({'a': 5, 'b': 5, 'c': 5})

### UNDERSCORES & DUNDERS ###
print("===========================")
print("UNDERSCORES & DUNDERS")

'''
1. Single Leading Underscore:_var
Python doesn’t have a strong distinction between “private” and “public” variables like Java does. 
So, to indicate that a variable is meant for internal use, a single leading underscore (prefix) 
is used before the variable name.
'''


class Pubber:
    def __init__(self):
        self.name = 'Bond, James'
        self._age = 33  # private variable, shhh...

        def _menu_tonight():  # private function
            pass


p = Pubber()
p._age = 11  # not recommended - like private

'''
Single Trailing Underscore: var_
What if you need to use a keyword for a name?
Append a single trailing underscore (postfix) after variable, function, or Class names, and you’re good to go! It avoids naming conflicts with Python keywords.
class class: #SyntaxError: "invalid syntax"
'''


class class_:  # No problem
    pass


'''
Leading Dunders: __var
‘Dunders’ means double underscores.
A double underscore prefix can be used in Python to avoid naming conflicts in subclasses.
'''


class Pubber:
    def __init__(self):
        self.name = 'Bond, James'
        self._age = 33
        self.__address = 'Mars'  # double underscore prefix


class SubPubber(Pubber):
    def __init__(self):
        self.name = 'Bond, James'
        self._age = 33
        self.__address = 'Mars'  # double underscore prefix


p1 = Pubber()
sp1 = SubPubber()
# p1.__address='aaa' #output: AttributeError: object has no __address
# sp1.__address='bbb' #output: AttributeError: object has no __address

print(dir(p1))  # we can see it was converted to '_Pubber__address'
print(dir(sp1))  # we can see it was converted to '_SubPubber__address'

'''
Leading and Trailing Dunders: __var__ there are almost 100 built-in Dunders in Python
'''

'''
Single Underscore: _ 
 use a single stand-alone underscore as a name to indicate that a variable is temporary or insignificant.
'''
beer = ('light', 'bitter', 70, 153)
color, _, _, calories = beer
print(f"color is {color} and caloris are {calories}")  # output: color is light and caloris are 153

### FUNCTOOLS LIBRARY ###
print("===========================")
print("FUNCTOOLS LIBRARY")

'''
Using Partial function, you can fix any argument value the number of arguments of a function thus removing
the necessity of creating another one. What you get as a result is an elegant and easy to read code.
If you have a function with several arguments but you need to set only 1 or 2 each time. Use partial.
'''
print("functools.partial")
from functools import partial


def logger(log_level, id, message):
    print(f'[{log_level}]: {id} - {message}')


# The regular way
logger('DEBUG', 1111, 'message_one')  # [DEBUG]: 2222 - message_one
logger('DEBUG', 1111, 'message_two')  # [DEBUG]: 2222 - message_two
logger('DEBUG', 1111, 'message_three')  # [DEBUG]: 2222 - message_three

# Using partial, log_level should be debug and id 2222 always
debug_logger = partial(logger, 'DEBUG', 2222)
debug_logger('message_one')  # [DEBUG]: 2222 - message_one
debug_logger('message_two')  # [DEBUG]: 2222 - message_two
debug_logger('message_three')  # [DEBUG]: 2222 - message_three

'''
LRU stands for Least Recently Used, it saves the result of last executed function in memory and 
when it have to again execute the function, first it will check in cache, 
if found it will return the result otherwise it will go on to execute the function.
“lru_cache” can save us a lot of time when we need to perform computationally expensive or I/O bound 
operations through a function.
'''

print("functools.lru_cache")
from functools import lru_cache, singledispatch
from time import time


@lru_cache(maxsize=128)
def fibo_lru(n):
    if n <= 1:
        return n
    else:
        return (fibo_lru(n - 1) + fibo_lru(n - 2))


def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n - 1) + fibo(n - 2))


def sum_of_fibo(nterms, fun):
    start = time()
    result = 0
    for i in range(nterms):
        result += fun(i)
    print(f'Total Sum {result} , Total time taken {(time() - start):.2f} sec')


sum_of_fibo(30, fibo_lru)
sum_of_fibo(30, fibo)

'''
“singledispatch” implementation lets you achieve function overloading. 
It converts your function into a generic function which can have different behavior depending 
on the type of first argument.
Use “singledispatch” decorator over the default implementation and then simply add
 “@<functionname>.register(<type>)” over the functions that you need to overload.
'''

print("functools.singledispatch")
from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


add(1, 2)  # output: 3
add('Python', 'Programming')  # output: PythonProgramming
add([1, 2, 3], [5, 6, 7])  # output: [1, 2, 3, 5, 6, 7]

'''
functools.reduce
Reduce is again a higher order function which is primarily used to accumulate data while 
iterating over a passed sequence → reduce(function, sequence, start)
Working of reduce function →
1. In first iteration, the function provided is applied to the first element of a sequence and the start value, 
and the result is then returned to next iteration.
2. In second iteration, the same function is applied on the previously calculated result and the next element of 
the sequence, the result is then updated with the newly calculated value.
3. In all subsequent iterations, Step 2 is executed repeatedly until the sequence is exhausted, 
and the final result is then returned.
Reduce always returns a single value.
'''

print("functools.reduce")
from functools import reduce

l = [10, 20, 5, 100, 30]

# Sum of list with start value = 0
print(reduce(lambda x, y: x + y, l))  # output: 165

# Sum of list with start value = 100
print(reduce(lambda x, y: x + y, l, 100))  # output: 265

print(reduce(lambda a, b: a if a > b else b, l))  # output: 100
print(reduce(min, l))  # output: 5

### STACK Class implementation ###
print("===============================")
print("Stack Class implementation")


class Stack():
    def __init__(self):
        self.items = []  ## Empty list intilize

    def push(self, item):
        self.items.append(item)  ## simple appending to list

    def pop(self):
        return self.items.pop()  ## Removing top element of the stack

    def is_empty(self):
        return self.items == []  ### Checking whether the stack is empty or not

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  ## returnign top element using [-1]=last element

    def show_stack(self):
        return self.items  ## Printing all the items


obj = Stack()  ## Creating obj for class stack

print("push 10")
obj.push(10)
print("push 20")
obj.push(20)
print("push 30")
obj.push(30)
print("Show stack:")
print(obj.show_stack())
print("pop")
print(obj.pop())
print("peek top element")
print(obj.peek())
print("Show stack:")
print(obj.show_stack())

### Linked List Implementation ###
print("======================================")
print("Linked List Implementation")


# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    #############################################
    ############ INSERT NODES ###################
    #############################################

    ######### AT THE END (APPEND) ###############
    def append(self, data):
        newNode = Node(data)  ## Taking the data in the as a newNode
        if (self.head):  ## if self.head is not None then     means :=>> Linked list is not empty
            current = self.head  ## define current node as head node
            while (current.next):  ## While current node is not None
                current = current.next  # increase the current node by one node
            current.next = newNode  ## current node next is equal to newNode
        else:
            self.head = newNode  ## linked list is empty then simply add the new node

    ######### AT THE START (PREPAND) #############
    def prepand(self, data):
        newNode = Node(data)  ## Create a node
        newNode.next = self.head  ## Ponit the next of the new node to the head
        self.head = newNode  ## paas the head to the new node

    ######### AFTER A NODE  #######################
    def add(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        else:
            newNode = Node(data)
            newNode.next = prev_node.next
            prev_node.next = newNode

    ######### PRINTING ALL THE ELEMENTS  ##############
    def printLL(self):
        current = self.head  ## current node as head
        while (current):  ## While current node is  not None
            print(current.data)  ## Print the data part of the node   |data|next|
            current = current.next  ## Increase the current node with one node

    ##################################################
    ############ DELETE NODES ########################
    ##################################################

    def delete_node(self, key):
        current = self.head

        ######### AT THE START ##########################
        if current and current.data == key:
            self.head = current.next
            current = None
            return
            ######### IN THE MIDDLE AND THE END  ############
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        else:
            prev.next = current.next
            current = None
        ##################################################
        ######## DELETE NODE AT A GIVEN POSITION   #######
        ##################################################

    def delete_node_at_pos(self, pos):
        current = self.head

        if pos == 0:
            self.head = current.next
            current = None

        count = 1
        prev = None
        while current and count != pos:
            prev = current
            current = current.next
            count += 1
        if current is None:
            return
        else:
            prev.next = current.next
            current = None
        ##################################################
        ###### CALCULATE THE LENGTH OF THE LINKED LIST ###
        ##################################################

    def length(self):
        current = self.head
        length = 0
        while (current):
            length += 1
            current = current.next
        return length


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.prepand("E")
LL.append("A")
LL.add(LL.head.next, "F")
LL.append("B")
LL.append("C")
LL.printLL()
print("\n")

LL.delete_node("B")
LL.printLL()
print("\n")
LL.delete_node_at_pos(0)
LL.printLL()
print("\n")
print(LL.length())

### Search Algorithms Implemented ###
print("======================================")
print("Search Algorithms Implemented")

## LINEAR SEASRCH ###
print("Linear Search:")
lst = [2, 5, 3, 1, 7]
num = 1
for index, value in enumerate(lst):
    if num == value:
        print(f"{value} found at position {index + 1}")
print("################")
## BINARY SEARCH ###
print("Binary Search:")
lst = [1, 3, 2, 4, 5, 6, 9, 8, 7, 10]
lst.sort()
first = 0
last = len(lst) - 1
mid = (first + last) // 2
item = 7
found = False
while (first <= last and not found):
    mid = (first + last) // 2
    if lst[mid] == item:
        print(f"found at location {mid + 1}")
        found = True
    else:
        if item < lst[mid]:
            last = mid - 1
        else:
            first = mid + 1
if found == False:
    print("Number not found")

print("################")

## Calculate Prime Numbers ##
print("===========================")
print("Calculate Prime Numbers: till 13")
print(list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, 13))))  # output: [2,3,5,7,11]

# Write a one-liner in python to fetch out all the even and odd numbers from a given list?
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd, even = [el for el in a if el % 2 == 1], [el for el in a if el % 2 == 0]
# output: ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

# Write a program to check whether a number is Armstrong or not?
# Armstrong - sum of cubes of digits equal to value of the number - example:
# (1*1*1) + (5*5*5) + (3*3*3) == 153
num = 371
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    pass
# print(num,"is an Armstrong number")
else:
    pass
# print(num,"is not an Armstrong number")

## Checking Anagram ##
'''
An anagram is a word that is formed by rearranging the letters of a different word, 
using all the original letters exactly once. Like: LISTEN & SILENT
'''
print("Check Anagram:")
from collections import Counter


def check_anagram1(first_word, second_word):
    return sorted(first_word) == sorted(second_word)


def check_anagram2(first_word, second_word):
    return Counter(first_word) == Counter(second_word)


print(check_anagram1("silent", "listen"))  # True
print(check_anagram2("Fried", "Fired"))  # True

## Merging Two Dictionaries ##
print("===========================")
print("Merging Two Dictionaries:")
'''
3 examples to merge dictionaries
'''

basic_information = {"name": ['karl', 'Lary'], "mobile": ["0134567894", "0123456789"]}
academic_information = {"grade": ["A", "B"]}
details = dict()  ## Combines Dict

## Dictionary Comprehension Method
details = {key: value for data in (basic_information, academic_information) for key, value in data.items()}
print(details)

## Dictionary unpacking
details = {**basic_information, **academic_information}
print(details)

## Copy and Update Method
details = basic_information.copy()
details.update(academic_information)
print(details)

## Find the index of an element in a tuple
books = ('Atomic habits', 'Ego is the enemy', 'Outliers', 'Mastery')
print(books.index('Mastery'))  # 3

## FizzBuzz example ##
print("===========================")
print("MFizzBuzz example")
print(['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in
       range(1, 20)])

## Find Duplicates in List ##
print("===========================")
print("Find Duplicates in List")


def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

print(f"x has duplicates: {has_duplicates(x)}")  # True
print(f"y has duplicates: {has_duplicates(y)}")  # False

## Remove Duplicates From a List ##
print("===========================")
print("Remove Duplicates From a List")
list1 = [1, 2, 3, 3, 4, 'John', 'Ana', 'Mark', 'John']


# Method 1
def remove_duplicate(list_value):
    return list(set(list_value))


print(remove_duplicate(list1))

# Method 2
result = []
[result.append(x) for x in list1 if x not in result]
print(result)

## dataclasses ##
print("===========================")
print("dataclasses")
'''
There are several advantages over regular classes or other alternatives like returning multiple values or dictionaries:
a data class requires a minimal amount of code
you can compare data classes because __eq__ is implemented for you
you can easily print a data class for debugging because __repr__ is implemented as well
data classes require type hints, reduced the chances of bugs
'''

from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str


card = Card("Q", "hearts")
print(card == card)  # output: True
print(card.rank)  # output: 'Q'
print(card)  # output: Card(rank='Q', suit='hearts')


# Chunk
# How to chunk a list and divide it into smaller parts

def chunk(my_list, size):
    return [my_list[i:i + size] for i in range(0, len(my_list), size)]


my_list = [1, 2, 3, 4, 5, 6]
print(chunk(my_list, 2))  # [[1, 2], [3, 4], [5, 6]]
print(chunk(my_list, 3))  # [[1, 2, 3], [4, 5, 6]]
print(chunk(my_list, 4))  # [[1, 2, 3, 4], [5, 6]]

# Find the most frequently occurring value - To find the most frequently occurring value in a list or string:
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key=test.count))  # output: 4


#### Avoid the pitfalls of mutable default arguments ####
def add_item_to_cart(new_item, shopper_name, existing_items=[]):
    existing_items.append(new_item)
    print(f"{shopper_name}'s cart has {existing_items}")
    return existing_items


shopping_list_wife = add_item_to_cart("Dress", "Jennifer")  # Jennifer's cart has ['Dress']
shopping_list_husband = add_item_to_cart("Soccer", "David")  # David's cart has ['Dress', 'Soccer']

'''
As shown above, although we intended to create two distinct shopping lists, the second function call still accessed 
the same underlying object, which resulted in the Soccer item added to the same list object. To solve the problem, 
we should use the following implementation. 
Specifically, you should use None as the default value for a mutable argument:
'''


def add_item_to_cart(new_item, shopper_name, existing_items=None):
    if existing_items is None:
        existing_items = list()
    existing_items.append(new_item)
    print(f"{shopper_name}'s cart has {existing_items}")
    return existing_items


shopping_list_wife = add_item_to_cart("Dress", "Jennifer")  # Jennifer's cart has ['Dress']
shopping_list_husband = add_item_to_cart("Soccer", "David")  # David's cart has ['Soccer']


#####################################################################

# Check type before running the code in a function - example:
def add_numbers(a, b):
    if not (isinstance(a, (float, int)) and isinstance(b, (float, int))):
        raise TypeError("Numbers are required.")
    return a + b


# built in functions in Python good to know
class Circle():
    def __init__(self):
        self.radius = None


## isinstance = Return True if the object argument is an instance of the classinfo argument,
# or of a (direct, indirect or virtual) subclass thereof.
circle = Circle()
if isinstance(circle, Circle):
    print('isinstance use!')

## hasattr = hasattr() simply returns True if an object contains specified attribute, and False otherwise.
if hasattr(circle, 'radius'):
    print('hasattr returns the attribute of class')

## exec - dynamic executing of statement in python as string
statement = '''a = 10; print(a + 5); print("Exec example") '''
exec(statement)


# example of using toggle switch
class switch():
    def toggle_switch(self):
        if self.toggled == False:
            self.toggled = True
        else:
            self.toggled = False

    def better_toggle_switch(self):
        self.toggled = not self.toggled


### LEGB (Local, Enclosing, Global and Built-in) ###
'''
The LEGB rule refers to the variable look-up order in Python. 
Specifically, Python has four layers of scopes when the interpreter tries to resolve the variable 
— understand what values are bound to the variables. It’ll first start with the local scope, 
which can be a function or a class. If the interpreter finds the corresponding bound value for the variable, 
it’ll stop looking up and use the variable with that particular value.
Otherwise, it’ll look it up at a higher level — the enclosing scope. The enclosing scope only exists in 
a nested structure of functions. Specifically, when a function is declared within another function, 
we call the inside function the inner function and the outside function the outer function. 
When the interpreter tries to resolve the variable used within the scope of the inner function, 
if it can’t resolve in the local scope, it’ll go to the enclosing scope, 
which is the local scope of the outer function.
If it still can’t resolve the variable in the enclosing scope, it’ll go to the global scope. 
The global scope usually is the module level, which typically is a standalone Python file. Notably, 
when you import packages into the current file, the functions and classes from the import will 
also become part of the global scope. The built-in scope is the functions, classes, and other 
modules that are loaded when an interpreter is launched to make these most basic objects always available for use 
(e.g., the print and other built-in functions).
'''

#### MRO (Method Resolution Order) ####
'''
The Method Resolution Order denotes how Python or a programming language in general resolves a method or attribute. 
Unlike the LEGB rule discussed above, which is concerned about resolving a variable, 
the MRO is concerned about an object and how its calling of a method or retrieving a particular attribute is resolved. 
The MRO is mostly discussed in the context of multi-inheritance — classes (i.e., subclasses) inheriting 
from multiple classes (i.e., superclasses) and/or multi-layers of inheritance. Because both subclasses and 
superclasses share some common methods with possibly varied implementations, Python interpreter needs 
to have a mechanism to determine which method or attribute should be used in a particular call, and this is what the 
MRO takes the responsibility. A schematic example is shown in the code snippet below.

>>> class X:
...     def bin(self):
...         print(f"bin called in X")
... 
... class Y(X):
...     def go(self):
...         print(f"go called Y")
... 
... class Z(X):
...     def go(self):
...         print(f"go called Z")
... 
... class W(Y, Z):
...     def bin(self):
...         super().bin()
...         print(f"bin called W")
... 
...     def bingo(self):
...         self.bin()
...         self.go()
... 
... w = W()
... w.bingo()
... 
bin called in X
bin called W
go called Y
'''

### Dynamically Calling Functions ###
print("### Dynamically Calling Functions ###")


class MyClass():
    def example_func(self):
        print("example_func was called")


def call_func(name):
    klass = MyClass()
    return getattr(klass, name)()


call_func('example_func')  # output: example_func was called

'''
If you encounter sections of code where you won’t necessarily know the name of a function you wish to invoke until later, 
this is the answer. By using the built-in Python function getattr, you can call a function by name using a string. 
This is great for reducing tightly coupled code and improving extensibility. If you reduce hard-coded function names 
and allow more flexibility, then there is a strong chance your code will break less.
Using this simple method also reduces the overhead for other developers to add functionality to existing code. 
If all you have to do is add a new function to a class and it becomes immediately usable, that reduces complexity and 
makes code easier work with.
'''


# Another getattr example:
class Person:
    age = 23
    name = "Adam"


person = Person()
print('The age is:', getattr(person, "age"))  # output: The age is: 23
print('The age is:', person.age)  # output: The age is: 23


# getattr() when named attribute is not found
class Person:
    age = 23
    name = "Adam"


person = Person()

# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))  # output: The sex is: Male

# ==== SINGLETON ===
print("===========================")
print("=== Singleton ===")

## The __new__() method creates a new instance.
## The __init__() method initialises that instance.
'''
The __new__() is a static method (special-cased so we need not declare it as such) of a class to create instances. 
The first parameter is always the cls representing the class itself. 
Remaining parameters are those needed for the constructor. The return value should be a instance of this class.
'''


class Singleton_Student(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        print("Running __new__() method.")
        if not Singleton_Student._instance:
            Singleton_Student._instance = object.__new__(cls)
        return Singleton_Student._instance

    def __init__(self, first_name, last_name):
        print("Running __init__() method.")
        self.first_name = first_name
        self.last_name = last_name


s1 = Singleton_Student("Yang", "Zhou")  # Running __new__() method.
# Running __init__() method.
s2 = Singleton_Student("Elon", "Musk")  # Running __new__() method.
# Running __init__() method.

print(s1)  # <__main__.Singleton_Student object at 0x7ff1e5a53198>
print(s2)  # <__main__.Singleton_Student object at 0x7ff1e5a53198>
print(s1 == s2)  # True
print(s1.last_name)  # Musk
print(s2.last_name)  # Musk

## REMEMBER ##
'''
__init__() method must return None , otherwise a TypeError will be raised.
If the parent class has defined __init__() method, we should using super().__init__() to explicitly 
call it in subclasses’ __init__() method to ensure correct initialization.
If __new__() method does not return an instance of the class, then the __init__()method will not be invoked.
'''


class Student(object):

    def __new__(cls, *args, **kwargs):
        print("Running __new__() method.")
        instance = object.__new__(cls)
        return instance

    def __init__(self, first_name, last_name):
        print("Running __init__() method.")
        self.first_name = first_name
        self.last_name = last_name


s1 = Student("Dan", "Belfer")  # Running __new__() method.
# Running __init__() method.

print(s1.last_name)  # Belfer

### ABSTRACT CLASS ###
print("========================")
print("### ABSTRACT CLASS ###")

'''
An abstract class has some features, as follows:
An abstract class doesn’t contain all of the method implementations required to work completely, 
which means it contains one or more abstract methods. 
An abstract method is a method that just has a declaration but does not have a detail implementation.
An abstract class cannot be instantiated. It just provides an interface for subclasses to avoid code duplication. 
It makes no sense to instantiate an abstract class.
A derived subclass must implement the abstract methods to create a concrete class that fits 
the interface defined by the abstract class. 
Therefore it cannot be instantiated unless all of its abstract methods are overridden.
In a nutshell, an abstract class defines a common interface for a set of subclasses. 
It provides common attributes and methods for all subclasses to reduce code duplication. 
It also enforces subclasses to implement abstract methods to avoid odd inconsistencies.

Python comes with a module called abc which provides useful stuff for abstract class.
We can define a class as an abstract class by abc.ABC and define a method as an abstract method by abc.abstractmethod. 
ABC is the abbreviation of abstract base class.
Note: A class is not real abstract if it has abstract methods but not inherit from abc.ABC, 
which means it can be instantiated. For example:
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        print('Animal moves')


class Cat(Animal):
    def move(self):
        super().move()
        print('Cat moves')


c = Cat()
c.move()  # Animal moves
# Cat moves


### PROPERTY DECORATORS ###
print("=============================")
print("### PROPERTY DECORATORS ###")

'''
In object-oriented programming, each attribute of a class may have three basic methods:
A getter method to get its value
A setter method to set its value
A deleter method to delete it

Common property template:
class C(object):

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

### if you want to have Read only on property - do not apply setter on it ###
'''


class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError('The score must be between 0 ~ 100!')

    @score.deleter
    def score(self):
        del self._score


Yang = Student()
Yang.score = 55
print(f"The student score is: {Yang.score}")

###########################################
### 6 Alternatives to Classes in Python ###
print("==============================================")
print("###  6 Alternatives to Classes in Python  ####")
### Plain class ###

from typing import Optional


class Position:
    MIN_LATITUDE = -90
    MAX_LATITUDE = 90
    MIN_LONGITUDE = -180
    MAX_LONGITUDE = 180

    def __init__(
            self, longitude: float, latitude: float, address: Optional[str] = None
    ):
        self.longitude = longitude
        self.latitude = latitude
        self.address = address

    @property
    def latitude(self) -> float:
        """Getter for latitude."""
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        """Setter for latitude."""
        if not (Position.MIN_LATITUDE <= latitude <= Position.MAX_LATITUDE):
            raise ValueError(f"latitude was {latitude}, but has to be in [-90, 90]")
        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Getter for longitude."""
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        """Setter for longitude."""
        if not (Position.MIN_LONGITUDE <= longitude <= Position.MAX_LONGITUDE):
            raise ValueError(f"longitude was {longitude}, but has to be in [-180, 180]")
        self._longitude = longitude


pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
pos2 = Position(42.1238762, 9.1649964)


def get_distance(p1: Position, p2: Position) -> float:
    pass


### tuples ###
from typing import Tuple, Optional

pos1 = (49.0127913, 8.4231381, "Parkstraße 17")
pos2 = (42.1238762, 9.1649964, None)


def get_distance(p1: Tuple[float, float, Optional[str]],
                 p2: Tuple[float, float, Optional[str]]) -> float:
    pass


### Dictionaries ###
from typing import Any, Dict

pos1 = {"longitude": 49.0127913,
        "latitude": 8.4231381,
        "address": "Parkstraße 17"}
pos2 = {"longitude": 42.1238762,
        "latitude": 9.1649964,
        "address": None}


def get_distance(p1: Dict[str, Any],
                 p2: Dict[str, Any]) -> float:
    pass


### NamedTuples ###
from typing import NamedTuple


class Position(NamedTuple):
    longitude: int
    latitude: int
    address: int = None


# Both are used in the same way
pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
pos2 = Position(42.1238762, 9.1649964)


def get_distance(p1: Position, p2: Position) -> float:
    pass


### attrs ###
from typing import Optional
import attr


@attr.s
class Position:
    longitude: float = attr.ib()
    latitude: float = attr.ib()
    address: Optional[str] = attr.ib(default=None)

    @longitude.validator
    def check_long(self, attribute, v):
        if not (-180 <= v <= 180):
            raise ValueError(f"Longitude was {v}, but must be in [-180, +180]")

    @latitude.validator
    def check_lat(self, attribute, v):
        if not (-90 <= v <= 90):
            raise ValueError(f"Latitude was {v}, but must be in [-90, +90]")


pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
pos2 = Position(42.1238762, 9.1649964)


def get_distance(p1: Position, p2: Position) -> float:
    pass


### dataclasses ###
from typing import Optional
from dataclasses import dataclass


@dataclass
class Position:
    longitude: float
    latitude: float
    address: Optional[str] = None


@property
def latitude(self) -> float:
    """Getter for latitude."""
    return self._latitude


@latitude.setter
def latitude(self, latitude: float) -> None:
    """Setter for latitude."""
    if not (-90 <= latitude <= 90):
        raise ValueError(f"latitude was {latitude}, but has to be in [-90, 90]")
    self._latitude = latitude


@property
def longitude(self) -> float:
    """Getter for longitude."""
    return self._longitude


@longitude.setter
def longitude(self, longitude: float) -> None:
    """Setter for longitude."""
    if not (-180 <= longitude <= 180):
        raise ValueError(f"longitude was {longitude}, but has to be in [-180, 180]")
    self._longitude = longitude


pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
pos2 = Position(42.1238762, 9.1649964, None)


def get_distance(p1: Position, p2: Position) -> float:
    pass


#### 3 Ways to Explore a Python Object #####
print("===========================")
print("#### 3 Ways to Explore a Python Object #####")
#  First of all, when we get an object, we can check which type it belongs to by type() method.

a = 'Dan'
b = 100


class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name


Author = Person("Dan", "Blfer")

print(type(a))  # output: <class 'str'>
print(type(b))  # output: <class 'int'>
print(type(Author))  # output: <class '__main__.Person'>

# We can compare types:
a = 'dan'
b = 100
print(f"type(a)==type('developer'): {type(a)} == {type('developer')} : {type(a) == type('developer')}")  # output: True
print(f"type(b)==type(a): {type(b)} == {type(a)} : {type(b) == type(a)} ")  # output: False
print(f"type(b)==int: {type(b)} == int : {type(b) == int}")  # output: True
print(f"type(int) is {type(int)}")  # output: type(int) is <class 'type'>

# with import types we can check more complex types
import types


def func():
    return "Dan"


print(type(func) == types.FunctionType)  # output: True
print(type(lambda x: x) == types.LambdaType)  # output: True


# For inherited classes, using the isinstance() method is a very convenient way to check their inheritance relationship.

class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name


class Developer(Person):
    pass


class TopDeveloper(Developer):
    pass


one_guy = Developer()
Dan = TopDeveloper(first_name="Dan", last_name="Belfer")

print(f"isinstance(Dan,Person): {isinstance(Dan, Person)}")  # output: True
print(f"isinstance(one_guy,TopDeveloper): {isinstance(one_guy, TopDeveloper)}")  # output: False
print(f"isinstance(one_guy,Developer): {isinstance(one_guy, Developer)}")  # output: True

# The second parameter of isinstance() method can be a tuple to help us judge whether an object is one of certain types
print(f"isinstance('123',(str,int)): {isinstance('123', (str, int))}")  # output: True
print(f"isinstance([1,2,3],(list,tuple)): {isinstance([1, 2, 3], (list, tuple))}")  # output: True


# Type’s method mro() can give us the whole chain of class inheritance relations
class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name


class Developer(Person):
    pass


class TopDeveloper(Developer):
    pass


Dan = TopDeveloper(first_name="Dan", last_name="Belfer")
print(f"type(Dan).mro(): {type(Dan).mro()}")


# output: [<class '__main__.TopDeveloper'>, <class '__main__.Developer'>, <class '__main__.Person'>, <class 'object'>]

# The dir() method, which returns a list containing strings,
# can help us get all names of attributes and methods within an object.
class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name


print(dir(Person()))


# With the help of these three methods: getattr(), setattr() and hasattr(),
# we are able to get, set and check attributes or methods of an object.

class Person:
    def __init__(self, first_name="", last_name=""):
        self.first_name = first_name
        self.last_name = last_name


Dan = Person("Dan")
# Check an attribute is existed or not
print(f"hasattr(Dan,'first_name'): {hasattr(Dan, 'first_name')}")  # True
print(f"hasattr(Dan,'age'): {hasattr(Dan, 'age')}")  # False

# Set a new attribute to an object
setattr(Dan, 'sex', 'male')
print(f"getattr(Dan,'sex'): {getattr(Dan, 'sex')}")  # male

####### META-PROGRAMMING ######
print("===========================")
print("##### META-PROGRAMMING #####")
# Meta-programming is an act of writing code that manipulates code
# Meta-programming is an act of building functions and classes that can manipulate code by modifying,
# wrapping existing code, or generating code

# Meta-programming in Python can be achieved with:

# 1. Decorators - Decorators are higher-order functions that take a function as an argument and returns another function

# 2. Meta-classes - Meta-classes are special types of classes, rather than ordinary classes in Python.
# Where an ordinary class defines behavior of its own instance,
# a meta-class defines the behavior of an ordinary class and its instance.

# A meta-class can add or subtract a method or field to an ordinary class.
# Python has one special class, the type class, which is by default a meta-class.
# All custom type classes must inherit from the type class.

'''
For instance, if we have class Calc, with three class methods, 
and we want to provide debug functionality to all the methods in one class then we can use a meta-class for this.
'''


class Calc():
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y


# First, we need to create a meta-class MetaClassDebug, with debug functionality,
# and make the Calc class inherit from MetaClassDebug.
# And, when we call any method from the Calc class, it will get invoked with our debug_function.

def debug_function(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__qualname__} is called with parameter {args[1:]}")
        return func(*args, **kwargs)

    return wrapper


def debug_all_methods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug_function(val))
    return cls


class MetaClassDebug(type):

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debug_all_methods(obj)
        return obj


class Calc(metaclass=MetaClassDebug):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y


calc = Calc()
print(calc.add(2, 3))  # output: Calc.add is called with parameter (2, 3)  5
print(calc.sub(2, 3))  # output: Calc.sub is called with parameter (2, 3) -1
print(calc.mul(2, 3))  # output: Calc.mul is called with parameter (2, 3)  6

### attrs ###
print("===========================")
print("######    attrs    ########")

import attr


@attr.s
class Person(object):
    name = attr.ib(default='John')
    surname = attr.ib(default='Doe')
    age = attr.ib(init=False)


p = Person()
print(p)
p = Person('Bill', 'Gates')
p.age = 60
print(p)
#
# # Output:
# #   Person(name='John', surname='Doe', age=NOTHING)
# #   Person(name='Bill', surname='Gates', age=60)

############ JSON ##########
print("#### JSON ####")

'''
JavaScript Object Notation (JSON) is a lightweight data-interchange format based on the syntax of JavaScript objects. 
It is a text-based, human-readable, language-independent format for representing structured object data 
for easy transmission or saving. JSON objects can also be stored in files
 — typically a text file with a .json extension and a application/json MIME type. 
 Commonly, JSON is used for two way data transmission between a web-server and a client in a REST API.

JSON exists as a string — a sequence (or series) of bytes. To convert a complex object (say a dictionary) 
in to a JSON representation, the object needs to be encoded as a “series of bytes”, 
for easy transmission or streaming == a process known as serialization.
Deserialization is the reverse of serialization. It involves decoding data received in JSON format as native data types,
that can be manipulated further.

Compared to its predecessor in server-client communication, XML, JSON is much smaller, 
translating into faster data transfers, and better experiences.
JSON exists as a “sequence of bytes” which is very useful in the case we need to transmit (stream) data over a network.
JSON is also extremely human-friendly since it is textual, and simultaneously machine-friendly.
JSON has expressive syntax for representing arrays, objects, numbers and booleans.

Generally, the json module encodes Python objects as JSON strings implemented by the json.JSONEncoder class, 
and decodes JSON strings into Python objects using the json.JSONDecoder class.

By default, the JSON encoder only understands native Python data types (str, int, float, bool, list, tuple, and dict). 
The json module provides two very handy methods for serialization based on the conversion table below:
Python dict --> JSON object
Python list,tuple --> JSON array
Python str --> JSON string
Python int,float --> JSON number
Python True --> JSON true
Python False --> JSON false
Python None --> JSON null

dumps() — to serialize an object to a JSON formatted string.
dump()  — to serialize an object to a JSON formatted stream ( which supports writing to a file).

code:
import json
json.dumps({
        "name": "Foo Bar",
        "age": 78,
        "friends": ["Jane","John"],
        "balance": 345.80,
        "other_names":("Doe","Joe"),
        "active":True,
        "spouse":None
    }, sort_keys=True, indent=4)

output:
{
    "active": true,
    "age": 78,
    "balance": 345.8,
    "friends": [
        "Jane",
        "John"
    ],
    "name": "Foo Bar",
    "other_names": [
        "Doe",
        "Joe"
    ],
    "spouse": null
}

In the example above we passed a dictionary to the json.dumps() method, with 2 extra arguments which provide pretty 
printing of JSON string. sort_keys = True tells the encoder to return the JSON object keys in a sorted order, 
while the indent value allows the output to be formatted nicely, both for easy readability.

Similarly, lets use json.dump() on the same dictionary and write the output stream to a file.
code:
import json
with open('user.json','w') as file:
         json.dump({
            "name": "Foo Bar",
            "age": 78,
            "friends": ["Jane","John"],
            "balance": 345.80,
            "other_names":("Doe","Joe"),
            "active":True,
            "spouse":None
        }, file, sort_keys=True, indent=4) 

This example writes a user.json file to disk with similar content as in the previous example.

As in the case of serialization, the decoder converts JSON encoded data into native Python data types 
(opposite to table above)

The json module exposes two other methods for deserialization.
loads() — to deserialize a JSON document to a Python object.
load()  — to deserialize a JSON formatted stream ( which supports reading from a file) to a Python object.
code:
import json
json.loads('{ "active": true, "age": 78, "balance": 345.8,   
"friends": ["Jane","John"], "name": "Foo Bar", "other_names": ["Doe","Joe"],"spouse":null}')

output: 
{'active': True,
 'age': 78,
 'balance': 345.8,
 'friends': ['Jane', 'John'],
 'name': 'Foo Bar',
 'other_names': ['Doe', 'Joe'],
 'spouse': None}

Here we passed a JSON string to the json.loads() method, and got a dictionary as the output.
To demonstrate how json.load() works, we could read from the 
user.json file that we created during serialization in the previous section.

code:
import json
with open('user.json', 'r') as file:
     user_data = json.load(file)
print(user_data)

Serializing Custom Objects
In this section, we are going to define a custom User class, proceed to create an instance and attempt to serialize 
this instance, as we did with the built in types.

code:
class User:
   """
   Custom User Class
   """
    def __init__(self,name,age,active,balance,other_names,friends,spouse):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.other_names = other_names
        self.friends = friends
        self.spouse = spouse
        
    def __str__(self):
        return self.name

** json module only understands the built-in types, and User is not one of those.
A simple solution would be to convert our custom type in to a serializable type — i.e a built-in type. 
We can conveniently define a method convert_to_dict() that returns a dictionary representation of 
our object. json.dumps() takes in a optional argument, default , which specifies a function to be called if 
the object is not serializable. This function returns a JSON encodable version of the object.

code:
def convert_to_dict(obj):
  """
  A function takes in a custom object and returns a dictionary representation of the object.
  This dict representation includes meta data such as the object's module and class names.
  """
  
  #  Populate the dictionary with object meta data 
  obj_dict = {
    "__class__": obj.__class__.__name__,
    "__module__": obj.__module__
  }
  
  #  Populate the dictionary with object properties
  obj_dict.update(obj.__dict__)
  
  return obj_dict
  
The function takes in an object as the only argument.
We then create a dictionary named obj_dict to act as the dict representation of our object.
By calling the special dunder methods __class__.__name__ and __module__ on the object we are able to 
get crucial metadata on the object i.e the class name and the module name — with which we shall reconstruct 
the object when decoding.
Having added the metadata to obj_dict we finally add the instance 
attributes by accessing obj.__dict__ . (Python stores instance attributes in a dictionary under the hood)
The resulting dict is now serializable.
At this point we can comfortably call json.dumps() on the object and pass in default = convert_to_dict .

code:
from json_convert_to_dict import convert_to_dict
data = json.dumps(new_user,default=convert_to_dict,indent=4, sort_keys=True)
print(data)

{
    "__class__": "User",
    "__module__": "__main__",
    "active": true,
    "age": 78,
    "balance": 345.8,
    "friends": [
        "Jane",
        "John"
    ],
    "name": "Foo Bar",
    "other_names": [
        "Doe",
        "Joe"
    ],
    "spouse": null
}

At this point, we have a JSON string with data about a custom object that json.loads() doesn’t know about. 
Passing this string to json.loads()
will give us a dictionary as output, as per the conversion table above.

code:
import json
user_data = json.loads('{"__class__": "User", "__module__": "__main__", "name": "Foo Bar", "age": 78, "active": true, 
"balance": 345.8, "other_names": ["Doe", "Joe"], "friends": ["Jane", "John"], "spouse": null}')
type(user_data)
print(user_data)

As expected, user_data is of type dict .

dict
{'__class__': 'User',
 '__module__': '__main__',
 'name': 'Foo Bar',
 'age': 78,
 'active': True,
 'balance': 345.8,
 'other_names': ['Doe', 'Joe'],
 'friends': ['Jane', 'John'],
 'spouse': None}

However, we need json.loads() to reconstruct a User object from this dictionary. 
Accordingly, json.loads() takes in an optional argument object_hook which specifies a function that returns the desired 
custom object, given the decoded output (which in this case is a dict). 
We shall now go ahead and define a dict_to_obj function that returns a User object.

code:
def dict_to_obj(our_dict):
    """
    Function that takes in a dict and returns a custom object associated with the dict.
    This function makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in our_dict:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = our_dict.pop("__class__")
        
        # Get the module name from the dict and import it
        module_name = our_dict.pop("__module__")
        
        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)
        
        # Get the class from the module
        class_ = getattr(module,class_name)
        
        # Use dictionary unpacking to initialize the object
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj
    
Take in a dictionary, our_dict , obtained from decoding a JSON object. 
The dictionary should have special keys __class__ and __module__ that tell us what type of object we should create.
Extract the class name from the dictionary under the key __class__ .
Extract the module name from the dictionary under the key __module__ .
Now we can go ahead and import the module. Notice that we use __import__ since the module name isn’t known at run time.
From the imported module, we can get the class, which is one of the module’s attributes.
Finally instantiate a member of the class, by supplying the class constructor with instance arguments through 
dictionary unpacking of whatever is left of our_dict .

Now let’s go ahead and confidently call json.loads with the argument object_hook = dict_to_obj .
code:
from json_dict_to_obj import dict_to_obj
new_object = json.loads('{"__class__": "User", "__module__": "__main__", "name": "Foo Bar", "age": 78, "active": true, 
"balance": 345.8, "other_names": ["Doe", "Joe"], "friends": ["Jane", "John"], "spouse": null}',object_hook=dict_to_obj)
type(new_object) #output: __main__.User

'''
###############################
### WORKING WITH CSV ##########
'''
Reading from CSV file
Basic CSV Interaction
code:
import csv 
with open('hackers.csv', 'r', newline='') as myCsvFile: 
    reader = csv.reader(myCsvFile, delimiter=',', quotechar='|')
        for row in reader.readlines(): 
            print('row = ', row)
--code finished ---

That’s fine and all, but row returns a list - this is obviously a problem if you want to access the values of 
certain columns by column name, as opposed to numeric index (I bet you do). Well, we've got you covered:

code:
import csv 
with open('hackers.csv', 'r', newline='') as myCsvFile: 
     reader = csv.DictReader(myCsvFile) 
          for row in reader.readlines(): 
                print(row['column_name_1'], row['column_name_2'])

--code finished ---

Changing reader to DictReader outputs a dictionary per CSV row, as opposed to a simple list.
Printing all Keys and Their Values:

code:
with open('hackers.csv', 'r', newline='') as myCsvFile: 
       reader = csv.DictReader(myCsvFile) 
       for row in loc_reader: 
               for (k, v) in row.items(): 
                     print(k, ':', v)

--code finished ---
we probably don’t want to iterate over the first row of our CSV: this will output our key values alone, 
which would be useless in this context. Consider this:

code:
with open('hackers.csv', 'r') as myCsvFile:   
      next(myCsvFile) 
      for row in myCsvFile.readlines(): 
             print(row)
--code finished ---

Writing to CSV
code:
with open('hackers.csv', 'w') as myCsvFile: 
    columns = ['column_name_1', 'column_name_2'] 
    writer = csv.DictWriter(myCsvFile, fieldnames=columns)    
    writer.writeheader() 
    writer.writerow({'column_name_1': 'Mark', 'column_name_2': 'Twain'}) 
    writer.writerow({'column_name_1': 'Foo', 'column_name_2: 'Bar'})
--code finished ---

'''

##################################################
print("#### Choosing Function names rules..####")
'''
1. Is the function a test? -> test_<entity>_<behavior>.
2. Does the function has a @property decorator? -> don’t use a verb in the function name.
3. Does the function use a disk or a network:
3.1. … to store data? -> save_to, send, write_to
3.2. … to receive data? -> fetch, load, read
4. Does the function output any data? -> print, output
5. Returns boolean value? -> is_, has_/have_, can_, check_if_<entity>_<characteristic>
6. Aggregates data? -> calculate, extract, analyze
7. Put data from one form to another:
7.1. Creates a single meaningful object? -> create
7.2. Fills an existing object with data? -> initialize, configure
7.3. Clean raw data? -> clean
7.4. Receive a string as input? -> parse
7.5. Return a string as output? -> render
7.6. Return an iterator as output? ->iter
7.7. Mutates its arguments or some global state? -> update, mutate, add, remove, insert, set
7.8. Return a list of errors? -> validate
7.9. Checks data items recursively? -> walk
7.10. Finds appropriate item in data? -> find, search, match
7.11. Transform data type? -> <something>_to_<something_else>
7.12. None of the above, but still works with data? -> Check one of those: morph, compose, prepare, extract, generate, 
initialize, filter, map, aggregate, export, import, normalize, calculate .
'''
