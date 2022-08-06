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

*Module* is simply a .py file that can contain different functions, classes, or variables.
As an example, let’s create a file named hello.py that has a hello_world function.
def hello_world(year):
  print(f"Hello World {year}")

If we want to use the function hello_world in another .py file, we need to import the hello module first.
import hello
hello.hello_world(2022)

*Package*
Modules usually contain more items than our basic example,
so it’s recommended to import only a specific function rather than the whole module.
from hello import hello_world

Some well-known Python modules are os, re, and datetime.

When developing large applications, the number of modules you work with might increase.
In such cases, we group the modules into a package.

A package is a collection of modules that contain a file named __init__.py.
We can have modules into packages and subpackages.

To import a specific module (M1, M2, M3, or M4) from a package, we use the dot notation

import package.subpackage.m1
or
from package.subpackage import m1

Some well-known Python packages are pandas and numpy.

*Library*
Sometimes the term “library” is used interchangeably with “package” because both can contain modules and other packages.
That said, a library is usually known as a collection of packages.

Sometimes a library is created to share reusable code with the community,
so others don’t have to start from scratch when working on a project.

Some well-known Python libraries are requests, matplotlib and beautiful soup

*Framework*
Frameworks are similar to libraries but frameworks contain a basic workflow and architecture of an application.
A library doesn’t usually enforce a workflow on your code,
but a framework has already a skeleton that you need to fill in.
If you ever used Python frameworks such as Django or Flask,
you might’ve noticed that the essential building blocks
are already provided and you need to follow some guidelines to get things done.

Cheatsheet : https://github.com/gto76/python-cheatsheet
Cheatsheet : https://github.com/AbdulMalikDev/PythonCheatSheet
Cheatsheet : https://www.pythoncheatsheet.org/#Virtual-Environment
Cheatsheet : https://cheatography.com/davechild/cheat-sheets/python/
Cheatsheet : https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf

Reference to this file: Cheatsheet : https://www.pythoncheatsheet.org/cheatsheet

"""
'''
# PYTHON TEXT FORMAT
# Variable lower_snake
first_name = 'Dan Belfer'

# Class and module CamelCase
class UserDetails:

# Constant All Capital/UpperCase
USER_AGE = 100 # All uppercase

# Indentation : 4 spaces
if USER_AGE > 18:
    print('You can go to the party.')
'''

# CHECK PYTHON VERSION ### do verifications for customer version awareness
'''
import sys

if sys.version_info < (3, 5):
    print(f"Dear customer you are running old python")
print(f"Python version is: {sys.version_info}")
'''

# IMPORTS
print("===============")
print("===IMPORTS===")
"""
# 'generic import' of math module
import math

math.sqrt(25)

# import a function
from math import sqrt

sqrt(25)  # no longer have to reference the module
"""
# import multiple functions at once
'''from math import cos, floor'''

# import all functions in a module (generally discouraged)
'''from csv import *'''

# define an alias
'''import datetime as dt

print(dt.date.today())'''

# show all functions in math module
# print(dir(math))
# show help on math module
# help(math)

# define an alias to specific func from module
'''
from math import sqrt as sq

print(f"sqrt(81) is {sq(81)}")
'''

# PLACEHOLDER - a placeholder in a function that you haven’t implemented
'''
def func():
    pass


def func1():
    ...
'''
# INPUTS
print("================")
print("===INPUTS===")
# print("Multiple User input")
# normal way
# a = input("Enter name: ")
# b = input("Enter age: ")
# Better way
# a, b = input("Enter name and age: ").split()


# VARIABLES
print("===============")
print("===VARIABLES===")
'''
all variables/functions/class instances etc - are objects!!!
Variables are pointer to address in memory - they hold the address in memory not actually the value
addresses of objects can be revealed by function id()
Each assignment to a var changes the reference even if you do 
my_var = ny_var+5 it means my_var is now pointing to new
address in memory

a = 10
print(hex(id(a)))  # HEX address where a points to: 0x7ffc9daab470
b = a
print(hex(id(b)))  # HEX address where a points to: 0x7ffc9daab470 the same address!!!
a = 5  # Now the variable is pointing to other place
print(hex(id(a)))  # output: 0x7ffcaea1b3d0 meaning the assignment moved var a from pointing to place of 10
# to new place of 5
print(f"b is {b}")  # output: b is 10 because the assignment still to 10 in memory
b = b + 5  # b is now 15 meaning value changed - it means b is now pointing to other place
print(hex(id(b)))  # HEX address where a points to: 0x7ffcaea1b510 a different address.
'''
# values of integer -5 till 256 will point always to same variables
'''
k1 = 2
k2 = 2
print(f"k1 is k2: {k1 is k2} because k1 id is: {id(k1)} and it equal to id of: {id(k2)}")
'''
# DATA TYPES
print("===============")
print("===DATA TYPES===")
# determine an object type
'''
type(2)  # returns 'int'
type(2.0)  # returns 'float'
type('two')  # returns 'str'
type(True)  # returns 'bool'
type(None)  # returns 'NoneType'
'''

# python is dynamic typed - var as pointer(reference) to address type is according to what is being pointed to
''''
a = 10
print(f"type of a is: {type(a)} and its val is {a}") #output: type of a is: <class 'int'> and its val is 10
a = "Hello"
print(f"type of a is: {type(a)}  and its val is {a}") #output: type of a is: <class 'str'>  and its val is Hello
'''
# check if an object is of a given type
'''
isinstance(2.0, int)  # returns False
isinstance(2.0, (int, float))  # returns True
'''

# convert an object to a given type
'''
float(2)
int(2.9)
str(2.9)
'''

# zero, None, and empty containers are converted to False
'''
bool(0)
bool(None)
bool('')  # empty string
bool([])  # empty list
bool({})  # empty dictionary
'''

# non-empty containers and non-zeros are converted to True
'''
bool(2) # is True
bool('two') # is True
bool([2]) # is True
'''

# Object that can be changed internally (its state = its data) is called mutable (like mutants in English)
# Object that can NOT be changed internally (its state = its data) is called immutable
# Numbers (int,float,Boolean),string,tuple,Frozen set are *immutables!*
# list,set,dictionary,user defined classes are *mutable!*

# Notice: if t is tuple of and a,b are lists -->> it means it is immutable but a and b are mutable,
# you cannot add new element to t *but* you can change the elements in a and b inside the t
''''
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
'''
# MUTABLE and IMMUTABLE
print("=====================================")
print("===MUTABLE and IMMUTABLE===")
'''
the mutable objects can be changed after creation. The immutable objects cannot be changed after creation. 
Let’s check it out by two examples:
leaders = ["Elon Mask"]
print(leaders, id(leaders)) #output: ['Elon Mask'] 140700341254336
leaders.append("Dan Belfer") 
print(leaders, id(leaders))  # Same id - #output: ['Elon Mask', 'Dan Belfer'] 140700341254336

if we changed the leaders list, its content will be changed but its identity won’t be changed. 
Because the list object in Python is mutable, we can do the in-place modifications on it.

Leader = "dan"
print(Leader, id(Leader)) #output: dan 139713044786288

Leader.capitalize()
print(Leader, id(Leader))  #the Leader itself wasn't changed output: dan 139713044786288

### since a string is an immutable object in Python, we can not change anything on it, 
### even just capitalize its first letter. 
### We must assign the result of Leader.capitalize() to a new string.
Cap_Leader = Leader.capitalize()
print(Cap_Leader, id(Cap_Leader)) #output: Dan 139713044502768

list/Dict/Set are mutable (can be modified after initialized) all rest(tuple,string,number...) cannot be modified.
The '=' will create new object and label will be attached to the new object.
**Everything in Python is an object and the assignment operation is just binding a name to an object**

leaders = ["Elon Mask"]
print(leaders, id(leaders)) #output: ['Elon Mask'] 140009549940864
leaders.append("Dan Belfer")
print(leaders, id(leaders))  # Same id - output: ['Elon Mask', 'Dan Belfer'] 140009549940864
leaders = ["Mark Zuckerberg"]
print(leaders, id(leaders))  # the id changed! - output: ['Mark Zuckerberg'] 140009549461184

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
print(B, A)             # ['Mark'] ['Elon', 'Dan', 'Mark']
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
## IF insted of using '=' we modified the list in other way , like append the L and Vals are the same:
L = [1, 2, 3]

def func(vals):
    vals.append(4)
    print(f"id(vals): {id(vals)}") #output: id(vals): 2937882611520
    print(vals) #output: [1, 2, 3, 4]

func(L)  # [7, 8, 9]
print(f"id(L): {id(L)}") #output: id(L): 2937882611520
print(L) # [1, 2, 3] #output: [1, 2, 3, 4]
### L and Vals remain the same because there is no new assignment

Be Aware of the Mutability of Nested Objects
# we should know that the mutability of nested objects depends on each object itself. For instance:

tp = ([1, 2, 3], 4, 5)
tp[0].append(4)
print(tp)  # ([1, 2, 3, 4], 4, 5)

# The tp is a tuple which is immutable, but the first element of tp is a list that is mutable. 
# Therefore, we can modify the first element of tp even if it’s an immutable object.
'''

# F-STRING
print("=======================")
print("===F-STRING PRINTING===")

'''import datetime

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
'''
f-strings can also be used to self-document code using the = character.
What this means in practice is that when you’re printing a variable’s value to the console, 
you no longer need to write f"variable_name = {variable_name}".
'''
'''
some_variable = "HELLO!"
print(f"some_variable={some_variable}")  # output: some_variable=HELLO!

## Instead, you can simply write:
some_variable = "HELLO!"
print(f"{some_variable=}")  # output: some_variable=HELLO!

# Printing on the Same Line - if needed several strings on same line
print("Python ", end="")
print("Programming")
# output: Python Programming

print(f"{'Right Aligned' : >30}")
print(f"{'Left Aligned' : <30}")
print(f"{'Centered' : ^30}")

# output:

                Right Aligned
Left Aligned                  
           Centered           
'''

# MATH
print("===============")
print("===MATH===")
# basic operations
'''
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
'''
# BOOLEAN OPERATIONS
print("========================")
print("===BOOLEAN OPERATIONS===")
'''
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

a = 1
b = 2
c = 3
d = 5
e = 5
f = 3
print("a=1;b=2;c=3\nd=5;e=5;f=3\n")
print(f"a<b<c is {a < b < c}")
print(f"a==b==c is {a == b == c}")
print(f"a<d<=e is {a < d <= e}")
print(f"d==e != f is {d == e != f}")
print(f"d>f<e is {d > f < e}")

# Use 'is' or 'is not' to compare variable addresses (by their id)
# Use '==' ór '!=' to compare variable values
# Recommended when need to compare to None - to verify if exist or not, Null or not - prefer 'is None' to '== None'

a = [1, 2, 3]
b = [1, 2, 3]
print(f"a value is: {a} and id is: {hex(id(a))}") # output: a value is: [1, 2, 3] and id is: 0x22412660f00
print(f"b value is: {b} and id is: {hex(id(b))}") # output: b value is: [1, 2, 3] and id is: 0x22412665440
print(f"a is b : {a is b}")  # output: a is b : False - these do not have same id(address in memory)
print(f"a == b : {a == b}")  # output: a == b : True  - here the value is the same
'''

# CONDITIONAL STATEMENTS
print("============================")
print("===CONDITIONAL STATEMENTS===")
''''
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

# Condition using in
# simple if-statement condition:
n = 10
# instead of:
if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
    pass
# Type:
if n in [0, 1, 2, 3, 4, 5]:
    pass


'''
# Ternary Operator like 'a>b ? a:b' in c++
'''
# single-line if/else statement (sometimes discouraged)
# known as a 'ternary operator'
# value_if_true if condition else value_if_false
x = 10
'positive' if x > 0 else 'zero or negative'


# Chained Ternary:
age = 15

# this ternary operator:
print('kid' if age < 13 else 'teen' if age < 18 else 'adult')

# is equivalent to this if statement:
if age < 18:
     if age < 13:
         print('kid')
     else:
         print('teen')
else:
     print('adult')

# output: teen
'''
'''
The Walrus(:=) Operator
Walrus operators is one of the latest additions to Python. 
It was recently added to Python in Python version 3.8. 
It is an assignment expression that allows assignment directly in the expression.

Normal Way :

xs = [1,2,3]
n=len(xs)
if n>2:
    print(n)
Here in this example, we declare a list and then declare a variable ’n’ to assign the value of the length of the list.

Using walrus operators,

xs = [1,2,3]
if (n:=len(xs)>2):
    print(n)
Here, we declare and assign the value at the same time. That’s the power of the Walrus operator.
'''

'''
Avoid large conditions — All
long conditionals are not easy to catch in the first time; 
so, when possible, we have to avoid large conditions. For example:
if condition1 and condition2 and condition3 and condition4:
    do_something()
# same case, different syntax
if condition1:
    if condition2:
        if condition3:
            if condition4:
                do_something()
You can avoid them this way:
conditions = [condition1, condition2, condition3, condition4]
if all(conditions):
    do_something()    
'''

# 'all' return True if all elements of iterable are true (or iterable empty)
# 'all' behaves like a series of AND conditions
'''
all([0, 1, 2, 3])  # False
all([char for char in 'eio' if char in 'aeiou'])
all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])  # True
# 'any' return True if any element of iterable is true. If iterable is empty ,returns False
# 'any' behaves like a series of OR conditions
'''

'''
Avoid large conditions — Any
Sometimes, conditions are not followed just by and operators. In case of or operator:
if condition1 or condition2 or condition3 or condition4:
    do_something()
you can use any()
conditions = [condition1, condition2, condition3, condition4]
if any(conditions):
    do_something()
'''
'''
any([0, 1, 2, 3])  # True
any([val for val in [1, 2, 3] if val > 2])  # True
any([val for val in [1, 2, 3] if val > 5])  # False
# if need to validate a specific value in the collection/iterable:
if 2 in [0,1,2,3]:
    pass
'''
'''
When you need many conditions to be fulfilled in your code, 
then you can use Conditional List and All to check all the conditions. 
We can write all the conditions in the list and apply All to check if all the conditions are true.
Instead of using the if statement and writing all the conditions separated by and operator, 
we can write all the conditions in the list and apply All.
'''
'''
physics = 49
chemistry = 51
mathematics = 57

list_condition = [physics > 50, chemistry > 50, mathematics > 50]
("Pass" if all(list_condition) else "Fail")  # output: Fail
'''
'''
We can use a Conditional List and Any together when we want to check even if one of the many conditions is True.
Instead of using if statement and checking conditions separated by or operator, 
we can write all the conditions in the list and pass it to Any.
'''
'''
physics = 49
chemistry = 51
mathematics = 47

list_condition = [physics > 50, chemistry > 50, mathematics > 50]
("Pass" if any(list_condition) else "Fail")  # output: Pass
'''
''''Another example for any and all'''
# Assume some complex conditions
''''
condition1 =  5==6
condition2 =  5<7
condition3 =  10>0
condition4 =  10!=10
condition5 =  20>10
# without any
if condition1 or condition2 or condition3 or condition4 or condition5:
    print("without any")
#with any
lst = [condition1,condition2,condition3,condition4,condition5]
if any(lst):
    print("with any")

# without all
if condition3 and condition5:
    print("without and")
#with all
lst = [condition3,condition5]
if all(lst):
    print("with all")
'''

# FOR LOOPS AND WHILE LOOPS // ENUM
print("===============")
print("FOR WHILE LOOPS // ENUM")

''''
# The for loop iterates over a list, tuple, dictionary, set or string
# range returns a sequence (Python 3) of integers
range(0, 3)  # returns [0, 1, 2]: includes start value but excludes stop value
range(3)  # equivalent: default start value is 0
range(0, 5, 2)  # returns [0, 2, 4]: third argument is the step value

# break: If the execution reaches a break statement, it immediately exits the while loop’s clause
while True:
    name = input('Please type your name: ')
    if name == 'your name':
        break

>>> print('Thank you!')
# Please type your name: your name
# Thank you!

# continue: When the program execution reaches a continue statement, the program execution immediately 
# jumps back to the start of the loop.

while True:
     name = input('Who are you? ')
     if name != 'Joe':
         continue
     password = input('Password? (It is a fish.): ')
     if password == 'swordfish':
         break

>>> print('Access granted.')
# Who are you? Charles
# Who are you? Debora
# Who are you? Joe
# Password? (It is a fish.): swordfish
# Access granted.

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
'''
# ENUMERATION
print("===============")
print("ENUMERATIONS")

'''
range_name = range(to_exclusive)
range_name = range(from_inclusive, to_exclusive)
range_name = range(from_inclusive, to_exclusive, ± step_size)


for i, el in enumerate(collection [, i_start]):
    ...
'''
'''

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

# Another way to use Enum

from enum import Enum


class WeekDay(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


day = WeekDay.Friday
intDay = day.value  # This will be 5
print(f"day is: {day} and {intDay}")  # output: day is: WeekDay.Friday and 5

# Another example for using Enum:
from enum import Enum


class ProgrammingLanguage(Enum):
    PYTHON = "Python"
    JAVA = "Java"
    C = "C"
    JAVASCRIPT = "JavaScript"
    PHP = "Php"


print(f"The language I write is: {ProgrammingLanguage.PYTHON.value}")

'''
'''
from dataclasses import dataclass
from enum import Enum

class StateTax(Enum):
    OR = 0.05
    WA = 0.10
    CA = 0.08
    NY = 0.15  # Just need to update here to add more states

@dataclass
class Car:
    model: str
    price: float
    tax: StateTax

    def total_cost(self) -> float:
        return  self.price + (self.price * self.tax.value)       

    def get_tax(self):
        return self.tax.value


car1 = Car(model="RAV4", price=30000, tax=StateTax.OR)
car2 = Car(model="RAV4", price=30000, tax=StateTax.WA)
car3 = Car(model="RAV4", price=30000, tax=StateTax.CA)
car4 = Car(model="RAV4", price=30000, tax=StateTax.NY)  # create new instance

print(car1.total_cost()) # 31500.0
print(car2.total_cost()) # 33000.0
print(car3.total_cost()) # 32400.0
print(car4.total_cost()) # 34500.0
'''

# FUNCTIONS
print("===============")
print("FUNCTIONS")

''''
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

# Keyword Arguments: To improve or code readability, we should be as explicit as possible. 
# We can achieve this in our functions by using Keyword Arguments:

def say_hi(name, greeting):
    print(f"{name} {greeting}")

>>> # without keyword arguments
>>> say_hi('John', 'Hello')
# Hello John

>>> # with keyword arguments
>>> say_hi(name='Anna', greeting='Hi')
# Hi Anna

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

def func(a=0,b,c=2):  # cause error
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

# return values can be assigned multiple variables using *tuple unpacking* also called 'Assigning multiple variables'
min_num, max_num = min_max(nums)  # min_num = 1, max_num = 3

# Chained function call
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a, b = 5, 10

print(f"Chained Function calls: {(add if b > a else subtract)(a, b)}")  # output: Chained Function calls: 15

# Python is 'Pass by Object Reference' (not by value and not by reference)
def set_list(list):
    list = ["A", "B", "C"]  # here a new assignment will create object
    return list

def add(list):
    list.append("D") # here we use the original object to extend its value
    return list


my_list = ["E"]
print(f"id of my_list: {id(my_list)}")  #output: id of my_list: 1732001661184
x1 = set_list(my_list)
x2 = add(my_list)
print(f"id of my_list is {id(x1)} and value is: {x1}") # id of my_list is 1732001830400 and value is: ['A', 'B', 'C']
print(f"id of my_list is {id(x2)} and value is: {x2}") # id of my_list is 1732001661184 and value is: ['E', 'D']
'''

# GLOBAL LOCAL SCOPES
print("===============")
print("GLOBAL LOCAL SCOPES")
'''''
# Python is familiar with scopes. The highest is Builtin scope (where defined True,list,print etc...)
# Next there is Global scope - all space that is outside of main() or any function
# Local scope is inside the function we work with
# When python encounter a function at complie-time it will scan for any variables that have values assigned to them
# It will search them anywhere in the function, if the variable has not been specified as global,then it is local
# If the variable is not found - only at run-time python will start looking higher in hierarchy to find the vars.
# You cannot change the value of a global variable just by mentioning it inside a function, you need to use 'global'
# Code in the global scope cannot use any local variables.
# However, a local scope can access global variables.
# Code in a function’s local scope cannot use variables in any other local scope.
# You can use the same name for different variables if they are in different scopes. 
# That is, there can be a local variable named spam and a global variable also named spam.

global_variable = 'I am available everywhere'
def some_function():
    print(global_variable)  # because is global
    local_variable = "only available within this function"
    print(local_variable)

>>> # the following code will trow error because
>>> # 'local_variable' only exists inside 'some_function'
>>> print(local_variable)
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
NameError: name 'local_variable' is not defined

The global Statement: If you need to modify a global variable from within a function, use the global statement
def spam():
    global eggs
    eggs = 'spam'

>>> eggs = 'global'
>>> spam()
>>> print(eggs)
There are four rules to tell whether a variable is in a local scope or global scope:
If a variable is being used in the global scope (that is, outside all functions), then it is always a global variable.
If there is a global statement for that variable in a function, it is a global variable.
Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.
But if the variable is not used in an assignment statement, it is a global variable.
'''
''''
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
'''

# When working with nested functions - nonlocal means we are working on variable that is not defined locally but one
# level scope above. ''nonlocal'' is not ''global''
''''
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
'''
print("==============================")
print("## ANOTHER NONLOCAL EXAMPLE ##")
'''
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
'''
print("========================")
print("## THIRD NONLOCAL EXAMPLE ##")
'''
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
'''

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
'''
# When we pass immutable(cannot change) items as arguments to the function, it uses pass by value. For e.g:
def set_list(value):
  value= "Changed string" # the assignment created new object in memory, it is different than value in input
  return value  #Because string is immutable there is no existing method to change the string
s = "Hello"
print(set_list(s))
print(s)
Output:
Changed string
Hello


# When we pass mutables like list in the function arguments, it uses pass by reference.
def change(my_list):
   my_list.append(5)
   return my_list

my_list = [10, 20]
print(change(my_list))
print(my_list)
# Output:
# [10, 20, 5]
# [10, 20, 5]

# The list passed in the function also changed its value outside the function, when a number was appended.
# But there is a catch! Always using '=' is not assignment - it creates new object in memory!!!

# When we assign a new value to the list passed in the function, it uses pass by value.
def assign_list(my_list):
   my_list= ["A", "B", "C"]
   return my_list
my_list = [10, 20]
print(assign_list(my_list))
print(my_list)
# Output:
# ['A', 'B', 'C']
# [10, 20]

# Here, python created a new variable(within function scope) pointing to [“A”, “B”, “C”].

'''

# DOCSTRING FUNCTIONS
# Enable adding documentation to functions - can be activated by __doc__
print("===============")
print("DOCSTRING FUNCTIONS")
''''
def func_doc_string(something):
    """This is doctring that explains func_doc_string"""
    return something


func_doc_string('Hi')
print(func_doc_string.__doc__) #output: This is doctring that explains func_doc_string

# Docstrings can be considered formal documentations of functions. It generally has four essential components.
# Overall description: one sentence to describe the function’s operation, intended purpose, etc.
# Parameter list: describe each of the parameters
# Return value: what the function returns
# Exceptions (optional): describe what exceptions that the function can raise.
def calculate_fraction(a, b):
    """
    Calculate a fraction of two numbers
    :param a: int or float, the numerator of the fraction
    :param b: int or float, the denominator of the fraction
    :return: float, calculated as a /b
    :raise: ZeroDivisionError (when b is zero)
    """
    return a / b
'''

# ANONYMOUS (LAMBDA) FUNCTIONS
# primarily used to temporarily define a function for use by another function - like inline functions
# This is a real function with anonymous name , structure: lambda [param list] : expression
# The expression returns function object when it is called, param list is optional can be empty
# Lambda expression MUST be assigned to variable OR passed as argument to function
print("===============")
print("LAMBDA FUNCTIONS")

'''
# Lambda
function = lambda: return_value
function = lambda argument_1, argument_2: return_value


my_func = lambda x: x ** 2
# my_func(3) ->9
my_func = lambda x, y: x + y
# my_func(3,5) ->8
my_func = lambda: 'hello'
print(my_func())  # output: hello

# another example
def make_adder(n):
     return lambda x: x + n

>>> plus_3 = make_adder(3)
>>> plus_5 = make_adder(5)

>>> plus_3(4)
# 7
>>> plus_5(4)
# 9

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


# sorted() method can be used to sort any iterable in Python
# We have passed a lambda function as a key to sort the dictionary by age


data = [{'name': 'John', 'age': 21},
        {'name': 'Max', 'age': 19},
        {'name': 'Lisa', 'age': 22}
        ]
sorted_data = sorted(data, key=lambda x: x['age'])
print("Using sorted on dictionary by age:")
print(sorted_data)  # [{'name': 'Max', 'age': 19}, {'name': 'John', 'age': 21}, {'name': 'Lisa', 'age': 22}]
'''
'''
# Lambda extract dictionary values or keys for sorting
# Lambda function can also be used in sorted, sort, min,max, largest function.
# A typical usage is to sort a dictionary by its key or value.

# Here is the sequence:
dic = {'the':4, 'day':1, 'is':3, 'sunny':2}
# dic.items() --> decomposes dictionary into list of tuples
print(dic.items())  # dict_items([('the', 4), ('day', 1), ('is', 3), ('sunny', 2)])
print(sorted(dic.items(), key=lambda item: item[1]))  # [('day', 1), ('sunny', 2), ('is', 3), ('the', 4)]

# lambda reads the list of tuples and extract the value (item[1]) which output to key.
# after the list of values are complete, Sorted function sorts the dictionary by its values in ascending order
# and returns the sorted dictionary
# likewise, you could sort the dictionary by its key (item[0]) in ascending order.
'''

# FUNCTION ATTRIBUTES
print("=================")
print("FUNCTION ATTRIBUTES")
'''
Everything in Python is an object, and almost everything has attributes and methods. 
In python, functions too are objects. So they have attributes like other objects. 
All functions have a built-in attribute __doc__, which returns the doc string defined in the function source code. 
We can also assign new attributes to them, as well as retrieve the values of those attributes.

For handling attributes, Python provides us with “getattr” and “setattr”, a function that takes three arguments. 
There is no difference between “setattr” and using the dot-notation on the left side of the = assignment operator:

The given code can be written as follows to assign and retrieve attributes.

Example
def foo():
    pass
setattr(foo, 'age', 23 )
setattr(foo, 'name', 'John Doe' )
print(getattr(foo, 'age'))
foo.gender ='male'
print(foo.gender)
print(foo.name)
print(foo.age)
Output:
male
John Doe
23
'''
'''
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
'''

#### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### LISTS ###
## properties: ordered, iterable, mutable, can contain multiple data types
print("===============")
print("LISTS")

'''
list = list[from_inclusive : to_exclusive : ±step_size]

list.append(el)               # Or: list += [el]
list.extend(collection)       # Or: list += collection

list.sort()
list.reverse()
list = sorted(collection)
list = reversed(list)

sum_of_elements  = sum(collection)
elementwise_sum  = [sum(pair) for pair in zip(list_a, list_b)]
sorted_by_second = sorted(collection, key=lambda el: el[1])
sorted_by_both   = sorted(collection, key=lambda el: (el[1], el[0]))
flatter_list     = list(itertools.chain.from_iterable(list))
product_of_elems = functools.reduce(lambda out, el: out * el, collection)
list_of_chars    = list(str)

# Module operator provides functions itemgetter() and mul() that offer the same functionality as lambda expressions above.
int = list.count(el)         # Returns number of occurrences. Also works on strings.
index = list.index(el)       # Returns index of first occurrence or raises ValueError.
list.insert(index, el)       # Inserts item at index and moves the rest to the right.
el = list.pop([index])       # Removes and returns item at index or from the end.
list.remove(el)              # Removes first occurrence of item or raises ValueError.
list.clear()                 # Removes all items. Also works on dictionary and set.
'''
# create an empty list (two ways)
empty_list = []
empty_list = list()

# Check empty list
mylst = []
# way 1
if len(mylst) == 0:
    print("Empty!")
# way 2
if not mylst:
    print("Empty!")
# way 3
if mylst == []:
    print("Empty!")

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
print(numbers[::-1])  # reverse a List [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[::-1][::-1])  # list is like original ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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


## Sorting a List of Dictionaries
print("--------------------------------")
print("Sorting a List of Dictionaries")

person = [
    {
        'name': 'andrew',
        'age': 25,
        'id': 72365
    },
    {
        'name': 'bill',
        'age': 34,
        'id': 55443
    }
]
# Method 1
person.sort(key=lambda item: item.get("id"))
print(person)  # output: [{'name': 'bill', 'age': 34, 'id': 55443}, {'name': 'andrew', 'age': 25, 'id': 72365}]
# Method 2
person = sorted(person, key=lambda item: item.get("id"))
print(person)  # output: [{'name': 'bill', 'age': 34, 'id': 55443}, {'name': 'andrew', 'age': 25, 'id': 72365}]

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

# The filter() function takes two parameters: a function and an iterable item.
# In this case, we’ll define a function and filter a list.
original_list = [1, 2, 3, 4, 5]


def filter_three(number):
    return number > 3


filtered = filter(filter_three, original_list)
filtered_list = list(filtered)
print(filtered_list)  # Returns [4,5]

# same with list comprehension
original_list = [1, 2, 3, 4, 5]
filtered_list = [number for number in original_list if number > 3]
print(filtered_list)  # Return [4,5]

# The Python Map function allows us to apply a function to every item in an iterable object.
original_list = [1, 2, 3, 4, 5]


def square(number):
    return number ** 2


squares = map(square, original_list)
squares_list = list(squares)
print(squares)  # Returns [1, 4, 9, 16, 25]

# with list comprehension:
original_list = [1, 2, 3, 4, 5]

squares_list = [number ** 2 for number in original_list]
print(squares_list)  # Returns [1,4,9,16,25]

# There may be cases when you want to combine two or more lists.
# This is where the zip() function comes in! The zip() function creates an object containing
# the lists’ corresponding elements at each index.

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
combined = zip(numbers, letters)
combined_list = list(combined)  # returns [(1, 'a'), (2, 'b'), (3, 'c')]

# reverse list
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print(reversed_list)  # Returns: [5,4,3,2,1]

# There may be times when you want to see if an item exists in a list.
# You can do this simply by using the in operator.
games = ['Yankees', 'Yankees', 'Cubs', 'Blue Jays', 'Giants']


def isin(item, list_name):
    if item in list_name:
        print(f"{item} is in the list!")
    else:
        print(f"{item} is not in the list!")


isin('Blue Jays', games)
isin('Angels', games)
# Returns
# Blue Jays is in the list!
# Angels is not in the list!

# You may want to find the most common item in a list.
games = ['heads', 'heads', 'tails', 'heads', 'tails']
items = set(games)
print(max(items, key=games.count))

# Sometimes you’ll end up with a list that has other lists in it. You can use list comprehensions to do this easily!
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [i for j in nested_list for i in j]
print(flat_list)  # Returns [1, 2, 3, 4, 5, 6, 7, 8, 9]

# If you need to check if all items in a list are unique, you can use the power of sets to accomplish this!
list1 = [1, 2, 3, 4, 5]
list2 = [1, 1, 2, 3, 4]


def isunique(list):
    if len(list) == len(set(list)):
        print('Unique!')
    else:
        print('Not Unique!')


isunique(list1)
isunique(list2)
# Returns:  Unique!


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
print("=====================")
print("### NAMED TUPLES ####")

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
import math

Polar_Coordinate = namedtuple('Polar_Coordinate', 'r theta')


def convert_cartesian_to_polar(x, y):
    # Calculate Polar Cooordinates
    r0 = (x ** 2 + y ** 2) ** 0.5
    theta0 = math.atan2(y, x)
    # Convert from radians to degrees
    theta0 = math.degrees(theta0)

    return Polar_Coordinate(theta=theta0, r=r0)


box_position = convert_cartesian_to_polar(10, 10)
print(box_position)  # output: Polar_Coordinate(r=14.142135623730951, theta=45.0)
print(box_position.r)  # output: 14.142135623730951
print(box_position.theta)  # output: 45.0
print(type(box_position))  # output: <class '__main__.Polar_Coordinate'>

### STRINGS ###
## properties: iterable, immutable
print("===============")
print("### STRINGS ###")

'''
str  = str.strip()                         # Strips all whitespace characters from both ends.
str  = str.strip('chars')                  # Strips all passed characters from both ends.

list = str.split()                         # Splits on one or more whitespace characters.
list = str.split(sep=None, maxsplit=-1)    # Splits on 'sep' str at most 'maxsplit' times.
list = str.splitlines(keepends=False)      # Splits on \n,\r,\r\n. Keeps them if 'keepends'.
str  = str.join(coll_of_strings)           # Joins elements using string as separator.

bool = sub_str in str                      # Checks if string contains a substring.
bool = str.startswith(sub_str)             # Pass tuple of strings for multiple options.
bool = str.endswith(sub_str)               # Pass tuple of strings for multiple options.
int  = str.find(sub_str)                   # Returns start index of first match or -1.
int  = str.index(sub_str)                  # Same but raises ValueError if missing.

str  = str.replace(old, new [, count])     # Replaces 'old' with 'new' at most 'count' times.
str  = str.translate(table)                # Use `str.maketrans(dict)` to generate table.

str  = chr(int)                            # Converts int to Unicode char.
int  = ord(str)                            # Converts Unicode char to int.
'''

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

# we want to rip a number from a string
x = "BTC is $48000.12"
x = ''.join([c for c in x if c in '1234567890.'])
print(x)  # output: '48000.12'

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

# remove whitespace inside a string
message = " Welcome to the real world! "
print("first method: " + message.replace(" ", ""))  # output: Welcometotherealworld!
print("second method: " + "".join(message.split()))  # output: Welcometotherealworld!

# removing prefix of string
my_string = 'ABC-1234'


def strip_prefix(string_to_remove_from, prefix_that_being_removed):
    if string_to_remove_from.startswith(prefix_that_being_removed):
        return string_to_remove_from[len(prefix_that_being_removed):]
    else:
        return string_to_remove_from


print("~~Removing prefix: ~~")
print(strip_prefix(my_string, 'ABC'))  # output: -1234

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


# Extract Vowels
def Extract_Vowels(data):
    return [each for each in data if each in 'aeiou']


print(Extract_Vowels("langauge"))  # ['a', 'a', 'u', 'e']
print(Extract_Vowels("Developer"))  # ['e', 'e', 'o', 'e']

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

# The split() method works great when we wish to disintegrate a string based on some delimiter.
x = "mail.google.com"
x.partition(".")  # ('mail', '.', 'google.com')
print(x.partition(".")[0])  # output: 'mail'

### DICTIONARIES ###
## properties: unordered, iterable, mutable, can contain multiple data types
## made of key-value pairs
## keys must be unique, and can be strings, numbers, or tuples
## values can be any type
print("===============")
print("DICTIONARY")

'''
dict = {'x': 1, 'y': 2}                       # Dictionary example

dict.keys()                                   # Coll. of keys that reflects changes.
dict.values()                                 # Coll. of values that reflects changes.
dict.items()                                  # Coll. of key-value tuples that reflects ch

value  = dict.get(key, default=None)          # Returns default if key is missing.
value  = dict.setdefault(key, default=None)   # Returns and writes default if key is missing.
dict = collections.defaultdict(type)          # Creates a dict with default value of type.
dict = collections.defaultdict(lambda: 1)     # Creates a dict with default value 1.

dict = dict(collection)                       # Creates a dict from coll. of key-value pairs.
dict = dict(zip(keys, values))                # Creates a dict from two collections = convert lists to dictionary
dict = dict.fromkeys(keys [, value])          # Creates a dict from collection of keys.

dict.update(dict)                             # Adds items. Replaces ones with matching keys.
value = dict.pop(key)                         # Removes item or raises KeyError.
{k for k, v in dict.items() if v == value}    # Returns set of keys that point to the value.
{k: v for k, v in dict.items() if k in keys}  # Returns a dictionary, filtered by keys.

genius = {
    'name': ["Dan", "others"],
    'sex': ["Male", " "],
    'job': ["Programmer", "others"]
}
for k, (v1, v2) in genius.items():
    print(k, v1, v2)

genius = {
    'name': "Dan",
    'sex': "Male",
    'job': "Programmer"
}
#for keys
n, s, j = genius
print(n, s, j)
# name sex job

genius = {
    'name': "Dan",
    'sex': "Male",
    'job': "Programmer"
}
#for values
n, s, j = genius.values()
print(n, s, j)
# Dan Male Programmer
'''
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
mydict = {1: 11, 2: 22, 3: 33}
mydict = {i: j for j, i in mydict.items()}
print(mydict)  # output: {11: 1, 22: 2, 33: 3}

mydict = {'John': 'Tesla', 'Jane': 'BMW'}
mydict = {i: j for j, i in mydict.items()}
print(mydict)  # output: {'Tesla': 'John', 'BMW': 'Jane'}

'''
Reverse Dictionary
'''
mydict = {1: "ab", 2: "bc", 3: "cd", 4: "de"}
# Way 1
rev1 = dict(map(reversed, mydict.items()))
print(rev1)  # {'ab': 1, 'bc': 2, 'cd': 3, 'de': 4}
# Way 2
rev2 = {value: key for key, value in mydict.items()}
print(rev2)  # {'ab': 1, 'bc': 2, 'cd': 3, 'de': 4}

'''
5 ways to Sort Dictionaries / Sort Dictionary
'''
print("~#~ 5 ways to Sort Dictionaries ~#~")
### Using sorted() function ###
## Sorting the dictionary - ascending
print("~~ Sorting the dictionary - ascending ~~")
d1 = {'cherry': 1, 'apple': 2, 'banana': 3}
print(sorted(d1.items()))
# Output:[('apple', 2), ('banana', 3), ('cherry', 1)]

# Sorting the keys in the dictionary
d1 = {'cherry': 1, 'apple': 2, 'banana': 3}
print(sorted(d1.keys()))
# Output:['apple', 'banana', 'cherry']

# Sorting the values in the dictionary
d1 = {'cherry': 1, 'apple': 2, 'banana': 3}
print(sorted(d1.values()))
# Output:[1,2,3]

### Sorting using reverse parameter - descending ###
# Sorting dictionary in reverse order
print("~~ Sorting dictionary in reverse order ~~")
d1 = {'cherry': 1, 'apple': 2, 'banana': 3}
print(sorted(d1.items(), reverse=True))
# Output: [('cherry', 1), ('banana', 3), ('apple', 2)]

# Sorting dictionary keys in reverse order
d1 = {'cherry': 1, 'apple': 2, 'banana': 3}
print(sorted(d1.keys(), reverse=True))
# Output:['cherry', 'banana', 'apple']

# Sorting dictionary values in reverse order.
d1 = {'cherry': 1, 'apple': 2, 'banana': 3}
print(sorted(d1.values(), reverse=True))
# Output:[3,2,1]

### Sorting using the key parameter ###
# Sorting the dictionary based on values.
print("~~ Sorting using the key parameter ~~")
d1 = {'cherry': 1, 'apple': 12, 'banana': 3}
print(sorted(d1.items(), key=lambda x: x[1]))
# Output:[('cherry', 1), ('banana', 3), ('apple', 12)]

#  Sorting dictionary based on length of keys.
d1 = {'cherry': 1, 'apple': 2, 'banana': 3}
print(sorted(d1.items(), key=lambda x: len(x[0])))
# Output:[('apple', 2), ('cherry', 1), ('banana', 3)]

### Using sorted function in a dictionary comprehension ###
# Sorting dictionary based on keys and returns a sorted dictionary.
print("~~ Using sorted function in a dictionary comprehension ~~")
d1 = {'cherry': 1, 'apple': 2, 'banana': 3}
# by default, sorted function, will sort based on keys.
sort_keys = {k: v for k, v in sorted(d1.items())}
print(sort_keys)
# Output:{'apple': 2, 'banana': 3, 'cherry': 1}

'''
# Sort dictionary by keys
product_prices = {'Z': 9.99, 'Y': 9.99, 'X': 9.99}
print({key:product_prices[key] for key in sorted(product_prices.keys())})
# output: {'X': 9.99, 'Y': 9.99, 'Z': 9.99}

# Sort dictionary by values
population = {'USA':329.5, 'Brazil': 212.6, 'UK': 67.2}
print( {k:v for k, v in sorted(population.items(), key=lambda x:x[1])} )
# output: {'UK': 67.2, 'Brazil': 212.6, 'USA': 329.5}
'''

# Sorting dictionary based on values and returns a sorted dictionary
d1 = {'cherry': 1, 'apple': 12, 'banana': 3}
# key parameter is given as second element which is dict values
sort_values = {k: v for k, v in sorted(d1.items(), key=lambda x: x[1])}
print(sort_values)
# Output:{'cherry': 1, 'banana': 3, 'apple': 12}

### Using Counter ###
print("~~ Using Counter ~~")
from collections import Counter

d1 = {'cherry': 1, 'apple': 12, 'banana': 3}
print(Counter(d1))
# Output:Counter({'apple': 12, 'banana': 3, 'cherry': 1})
c = Counter(d1)
print(c.most_common())
# Output: [('apple', 12), ('banana', 3), ('cherry', 1)]


# defaultdict
print("### defaultdict ###")
print("###################")
'''
When working with dict, if we try to access a key that is not presented - KeyError appear
defaultdict handles this error by building on top of dictionaries. 
It does not give a KeyError like the regular dictionaries. 
However, whenever you try to access or “assign to” a key that is not there, it will create that key and give it 
a default value that was already specified.
'''
from collections import defaultdict


# defaultdict requires a function telling it what to assign as a value if the key is not initially there.
# In this case, Not Present Yet will be that default value:
def default_value():
    return "Not Present Yet"


# defaultdict takes one argument: the name of the function that returns the default value.
mydict = defaultdict(default_value)  # or can be  mydict = defaultdict(lambda: "Not Present Yet")
mydict["cat"] = 2
mydict["dog"] = 4
print(mydict["cat"])  # output: 2
print(mydict["dog"])  # output: 4
print(mydict["pig"])  # output: Not Present Yet
print(mydict["rabbit"])  # output: Not Present Yet

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
# To give a type hint to the variables, you simply use the syntax: var_name: type.
# In the parentheses, you apply this syntax for each of the parameters.
# To indicate the return value’s type, you use -> type following the parentheses before the colon.
print("===============")
print("ANNOTATIONS - Type Hints")

'''
from typing import *
foo:    Any = 0 # completely dynamic type: can be anything
foobar: Tuple[()] = () # empty tuple
bar:    Tuple[int, str] = (2, "nic")
barfoo: Tuple[Any, str, int] = (9, "nic", 18)
foobaz: List[int] = [1, 2, 4, 6]
baz:    Callable = lambda x: print(f'hi {x}')
bazbar: Dict[str, int] = {"nic": 10, "mark": 4, "linus": 9}
'''

# Variable declaration - # You can declare a typed variable without assigning it a value. Here’s an example:
'''
foo: str
# assign a value later
foo = bar()
'''

# Multiple types (Union) - A Union means that the type can be either of the specified types:
'''
foo: Union[int, str]
foo = 4
foo = "nic"
'''

# Typed functions = Typed functions are a staple of well-written modules.
# You can specify the parameters’ type as well as the return type. Here’s an example:
'''# Takes an int and a function that takes an int. Can return any type.
def callFunctionOn(bar: int, foo: Callable[int]) -> Any:
  return foo(bar)

# Takes an int. Doesn't ever return since it terminates the program.
def exitProgram(code: int) -> NoReturn:
  exit(code)
'''

# Optional types = Note that optional types are not optional arguments.
# Optional[x] signals that the argument can be either None or x.
'''
# Can take either a str or None. Returns an int or None
def length(bar: Optional[str]) -> Union[int, None]:
  if bar is None:
    return None
  return len(bar)
'''

# Creating types = You can also create your own types if you wish. Here’s an example from the documentation:
'''
UserId = NewType('UserId', int)
first_user = UserId(1)
'''

# Literal types = A type that indicates that a variable’s value must be one of a specified set. Check out this example:
'''
OpenMode = Literal["r", "rb", "w", "wb"]
# Takes a string path and a string open mode. Returns a file wrapper.
def openFile(path: str, mode: OpenMode) -> _io.TextIOWrapper:
  return open(path, mode)

file = openFile("/home/nic/.profile", "rb") # OK
file = openFile("/home/nic/.profile", "rn") # Type checker highlights error
'''

# Typing with classes = You can define your own types with NewType . You can also use classes; one is shown below:
'''
class Person:
  def __init__(self, name: str, age: int):
    self.name: str = name
    self.age: int = age
  
  def greet(self, other: Person) -> str:
    return f"Hello {other.name}, I'm {self.name}"
'''

# Example of type hints function that make things clear:
'''
def make_connection(ip: str,
                    port: int,
                    timeout: datetime.timedelta,
                    on_connection: Callable[[Client], None], 
                    on_error: Callable[[ConnectionError], None]
                   ) -> Union[Client, None]:
  # ...
'''


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

### COMPREHENSIONS ###
print("===============")
print("COMPREHENSIONS")

'''
list = [i+1 for i in range(10)]                   # [1, 2, ..., 10]
set  = {i for i in range(10) if i > 5}            # {6, 7, 8, 9}
iter = (i+5 for i in range(10))                   # (5, 6, ..., 14)
dict = {i: i*2 for i in range(10)}                # {0: 0, 1: 2, ..., 9: 18}

out = [i+j for i in range(10) for j in range(10)]

# Is the same as
out = []
for i in range(10):
    for j in range(10):
        out.append(i+j)
        
# list comprehension
[expression for item in iterable]
# expanded form
for item in iterable:
    expression

# list comprehension with a conditional statement
[expression for item in iterable if some_condition]
# expanded form
for item in iterable:
    if some_condition:
        expression
        
# basic syntax
[expression0 if some_condition else expression1 for item in iterable]
# syntax explained: compared to the list comprehension's basic syntax: [expression for item in iterable], 
we can thin about that (expression0 if some_condition else expression1) is a whole part that constitutes the expression 
in the general format

# basic syntax of the nested list comprehensions
[expression for sublist in outer_list for item in sublist]
# expanded form
for sublist in outer_list:
    for item in sublist:
        expression
        
Syntax : [expression for item in iterable]
Syntax (if only): [expression for item in iterable if condition]
Syntax (if & else both): [expression if condition else expression for item in iterable ]
Syntax (Nested Loops): [(x,y) for x in iterable1 for y in iterable 2]
Syntax (Multiple if ): [x for x in iterable if condition1 and condition2]
Syntax (Multiple if & else): [x if condition1 and condition2 else condition for x in iterable]        

List Comprehension Syntax
[element for i in iterable if condition]
Breaking Down A List Comprehension:
Step 1 — Dividing into 3 main parts
At its base, a list comprehension is divided into 3 portions:
+ The element element
+ The for loop for i in iterable
+ The condition if condition (optional)

For example:   [i if i%2==1 else -i for i in range(1,101) if "1" in str(i)]
Using this as an example, let’s break this down:
+The element i if i%2==1 else -i
+The for loop for i in range(1,101)
+The condition if "1" in str(i)

Step 2 — Converting to a normal for loop
x = [element for i in iterable if condition]
Generally translates to:
x = []
for i in iterable:
    if condition:
        x.append(element)

So it is:
x = []
for i in range(1, 101):
    if "1" in str(i):
        x.append(i if i%2==1 else -i)
# [1, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, 21, 31, 41, 51, 61, 71, 81, 91, -100]

Finding squares of numbers from 1 to 10:  x = [i**2 for i in range(1,11)]
Finding numbers from 1 to 100 that contain a digit 1:  x = [i for i in range(1,101) if "1" in str(i)]
Finding squares and cubes of numbers from 1 to 5:  x = [i**n for i in range(1,6) for n in [2,3]]
Creating a 2-dimensional list:  x = [[i*n for n in [1,10,100]] for i in range(1,6)]
'''

# for loop to create a list of cubes
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
    cubes.append(num ** 3)

# equivalent list comprehension
cubes = [num ** 3 for num in nums]  # [1, 8, 27, 64, 125]

# list comprehension on nested list
vals = [[1, 2, 3], [4, 5, 2], [3, 2, 6]]
# we want to make the nested non nested list
vals_exp = [y for x in vals for y in x]  # list comprehension
print(f"vals_exp with list comprehension: {vals_exp}")  # [1,2,3,4,5,2,3,2,6]

# list comprehension using if-else
my_list = ['BuzzFizz' if i % 12 == 0
           else 'Buzz' if i % 3 == 0
else 'Fizz' if i % 4 == 0
else i for i in range(1, 15)]
print(my_list)  # output: [1, 2, 'Buzz', 'Fizz', 5, 'Buzz', 7, 'Fizz', 'Buzz', 10, 11, 'BuzzFizz', 13, 14]

# equivalent to regular using of for loops:
vals_exp = []
for x in vals:
    for y in x:
        vals_exp.append(y)
print(f"vals_exp with regular for loops: {vals_exp}")  # [1,2,3,4,5,2,3,2,6]

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

# Flattening a list
mylist = [10, 12, 36, [41, 59, 63], [77], 81, 93]
flat = []
for i in mylist:
    if isinstance(i, list):
        flat.extend(i)  # add all the elements in list in one iteration
    else:
        flat.append(i)  # add single element
print(flat)  # output: [10, 12, 36, 41, 59, 63, 77, 81, 93]

# equivalent list comprehension
items = [item for row in matrix for item in row]  # [1, 2, 3, 4]

# Example: Do apply a conditional criterion if only some items are needed
integers = [1, 2, 3, 4, 5, 6]
# Create a list of squares for even numbers only
squares_of_evens = [x * x for x in integers if x % 2 == 0]
print((squares_of_evens))  # output: [4, 16, 36]

# Example: Do Use a conditional expression
integers = [1, 2, 3, 4, 5, 6]
# Create a list of numbers, when the item is even, take the square
# when the item is odd, take the cube
custom_powers = [x * x if x % 2 == 0 else pow(x, 3) for x in integers]
print(custom_powers)  # output: [1, 4, 27, 16, 125, 36]

#  Do use nested for loops if you have a nested structure for the iterable
'''
[expression for item_outer in iterable for item_inner in item_outer]
# Equivalent to
for item_outer in iterable:
    for item_inner in item_outer:
        expression
'''
# A list of tuples
prices = [('$5.99', '$4.99'), ('$3.5', '$4.5')]
# Flattened list of prices
prices_formatted = [float(x[1:]) for price_group in prices for x in price_group]
print(prices_formatted)  # output: [5.99, 4.99, 3.5, 4.5]

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
  
+ Python works better and faster with built in functions like map
Example:
newlist = []
for word in wordlist:
    newlist.append(word.upper())
A better way to write this code is:
newlist = list(map(str.upper, wordlist))
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

# filter False,None,0 values from a list
mylst = [False, None, 0, 2, None, "", 9, 4, 7]
newlst = list(filter(None, mylst))
print(newlst)  # output: [2, 9, 4, 7]

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
# Another list comprehension but with conditions:
Genius = ["Jerry", "Jack", "tom", "Dan"]
print("List Comprehension with conditions:")
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

# The short way using list comprehension
Genius = ["Jerry", "Jack", "tom", "Dan"]
L1 = [char for name in Genius for char in name]
print(L1)  # output: ['J', 'e', 'r', 'r', 'y', 'J', 'a', 'c', 'k', 't', 'o', 'm', 'D', 'a', 'n']

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

# Remove specific element from list
x = [1, 2, 3, 2, 2, 2, 3, 4]
lst = list(filter(lambda a: a != 2, x))  # remove element 2 form the list
print(lst)  # output: [1, 3, 3, 4]

### ZIP ###
print("===============")
print("ZIP")

# make an iterator that aggregates elements from each of the iterables, only works with iterators
# for iterating over two data types at the same time, where needed the indexes to be equal
# zip creates tuple where i-th element in the tuple is i-element of one iterator and second is i-th element in second..

test_list = [1, 2, 3]
zip_result = zip(test_list)
for i in zip_result:
    print(i)

# (1,)
# (2,)
# (3,)


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

'''
import re
str   = re.sub(regex, new, text, count=0)  # Substitutes all occurrences with 'new'.
list  = re.findall(regex, text)            # Returns all occurrences as strings.
list  = re.split(regex, text, maxsplit=0)  # Use brackets in regex to include the matches.
match = re.search(regex, text)             # Searches for first occurrence of the pattern.
match = re.match(regex, text)              # Searches only at the beginning of the text.
iter  = re.finditer(regex, text)           # Returns all occurrences as match objects.
'''

print("===================================")
print(" ---- ====  REGEX ==== ------")

# This findall() function returns a list of strings that are matched with the pattern.
import re

text = "Hello 12, how are you? This is 13"
pattern = "\d+"
result = re.findall(pattern, text)
print(result)  # Output: ['12', '13']

# This search() method is used to search a particular pattern in a given text/string.
# This method returns a match object if the matched pattern is found in the text. Otherwise, it returns None .

import re

text = "Python is a programming language"
# cheking if 'Python' is present at the beginning
match = re.search('\APython', text)
if match:
    print("Pattern found")
else:
    print("Pattern not found")

# Output:Pattern found

# This split() function splits the string whenever a pattern is matched and returns the list of strings where
# the pattern has split the new string. This function takes two parameters, pattern and string, as input.
# The first parameter is a pattern that denotes the regular expression.
# Whenever the pattern is found in the string, it will split the string.

import re

text = "Hello 12, how are you? This is 13"
pattern = "\d+"
result = re.split(pattern, text)
print(result)  # Output: ['Hello ', ', how are you? This is ', '']

# This sub() function is used to find a pattern in a string and then replace that pattern with some other text.
# This function takes three parameters pattern, replace, string as input.

import re

text = "Namaste World! How are you doing?"
# replacing whitespace characters with '!!'
result = re.sub("\s", "!!", text)
print(result)  # Output: Namaste!!World!!!How!!are!!you!!doing?

# This subn() method is almost similar to sub() method. The only difference is in the output of both methods.
# The sub() method returns the string after replacing the matched pattern with replace parameter text,
# and the subn() method returns a tuple that consists of a modified string along with the number of replacements
# in the string.

import re

text = "Namaste world. I prefer to work at night"
pattern = "wo"
result = re.subn(pattern, "~", text)
print(result)  # Output: ('Namaste ~rld. I prefer to ~rk at night', 2)


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
## Example of Shallow Copy
data = [1, 2, 3, 4, 5]
updated_data = data
updated_data.append(6)
print(updated_data)
print(data)
--------------------------------
[1,2,3,4,5,6]     ## new
[1,2,3,4,5,6]     ## old
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
## Example of Deep Copy
import copy
data = [1,2,3,4,5]
updated_data = copy.deepcopy(data)
updated_data.append(6)
print(updated_data)
print(data)
------------------------------
[1,2,3,4,5,6]    ## new
[1,2,3,4,5]      ## old 
'''

### CLOSURE ####
print("========================")
print("## CLOSURE ##")
'''
The closure is a concept in the context of nested functions.
'''


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


# Another example of closure:
def outer_func():
    leader = "Dan Belfer"

    def print_leader():
        print(leader)

    return print_leader


f = outer_func()
print(outer_func.__closure__)  # output: None
print(f.__closure__)  # output: (<cell at 0x0000025113E77FD0: str object at 0x0000025113DBEF30>,)
print(f.__closure__[0].cell_contents)  # output: Dan Belfer
del outer_func

## Why its local variable [outer_func] is still alive after removing the function?
f()  # output: Dan Belfer
# outer_func() # -- causes error : name 'outer_func' is not defined

'''
The closure in Python is a function which remembers values in its enclosing scope.
The appearance of the closure must meet three conditions:
There are nested functions.
The inner function must use variables defined in its outer function.
The outer function must return the inner function.

The outer_func is not a closure and its __closure__ attribute is None. 
In the other hand, the __closure__ of f contains a cell object which saves the “remembered” value.
'''

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
[fibo.append(fibo[-2] + fibo[-1]) for _ in range(8)]


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


## Error Handling Using Decorators ##

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__} only takes numbers as the argument")

    return inner_function


@exception_handler
def area_square(length):
    print(length * length)


@exception_handler
def area_circle(radius):
    print(3.14 * radius * radius)


@exception_handler
def area_rectangle(length, breadth):
    print(length * breadth)


area_square(2)  # output: 4
area_circle(2)  # output: 12.56
area_rectangle(2, 4)  # output: 8
area_square("some_str")  # output: area_square only takes numbers as the argument
area_circle("some_other_str")  # output: area_circle only takes numbers as the argument
area_rectangle("some_other_rectangle")  # output: area_rectangle only takes numbers as the argument

##### DECORATORS EXPLAINED ############
print("========================")
print("DECORATORS EXPLAINED")

"""
def decorator(func):
    def inner():
        print("run something before actual function")
        func()
        print("run something after actual function")
    return inner


def func():
    print("something...")


decorated_func = decorator(func)
decorated_func()
## replaced by:
@decorator
def func():
    print("something...")
##

''
run something before actual function
something...
run something after actual function
''
"""

import functools


# Simple Decorator
def deco_function(func):
    @functools.wraps(func)
    def wrapped(*args):
        """
        This is the wrapper for a function to be fail safe
        """
        try:
            return func(*args)
        except:
            print("Error occured")
            return None

    return wrapped


@deco_function
def divide(a, b):
    """
    This is a function to divide two numbers
    """
    return a / b


print(divide(10, 2))


# Simple Decorator with argument

def powered(power):
    def powered_decorator(func):
        def wrapper(*args):
            return func(*args) ** power

        return wrapper

    return powered_decorator


@powered(2)
def add(*args):
    return sum(args)


print(add(10))


# Decorators within a class

def try_safe(func):
    @functools.wraps(func)
    def wrapped(*args):
        try:
            return func(*args)
        except:
            print("Error occured")
            return None

    return wrapped


class Calculator:

    def __init__(self):
        pass

    @try_safe
    def add(self, *args):
        return sum(args)

    @try_safe
    def divide(self, a, b):
        return a / b


calc = Calculator()
print(calc.divide(10, 2))


# Decorators for a Class
# Decorator for a class will activate the decorator during the instantiation of the function

def try_safe(cls):
    @functools.wraps(cls)
    def wrapped(*args):
        try:
            return cls(*args)
        except:
            print("Error occured")
            return None

    return wrapped


@try_safe
class Calculator:

    def __init__(self, a, b):
        self.ratio = a / b


calc = Calculator(1, 0)  # output: Error occured


# Injecting State for a Function using Decorators
# During the process of wrapping a function, a state could be injected into the function


def record(func):
    @functools.wraps(func)
    def wrapped(*args):
        wrapped.record += 1
        print(f"Ran for {wrapped.record} time(s)")
        return func(*args)

    wrapped.record = 0
    return wrapped


@record
def test():
    print("Running")


test()
test()
test()
''' output:
Ran for 1 time(s)
Running
Ran for 2 time(s)
Running
Ran for 3 time(s)
Running
'''


# Singleton using Python Decorators
# Singleton refers to an instance that is shared between calls, and would not duplicate for any reason.
# In simple terms, at first, an instance is created. In the following calls to make an instance,
# the existing instance will be returned.

def singleton(cls):
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        if not wrapped.object:
            wrapped.object = cls(*args, **kwargs)
        return wrapped.object

    wrapped.object = None
    return wrapped


@singleton
class SingularObject:
    def __init__(self):
        print("The object is being created")


first = SingularObject()
second = SingularObject()
print(f"second is first : {second is first}")  # output: True

# Making a Wrapper/Decorator Class

import functools


class Record:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.record = 0

    def __call__(self, *args, **kwargs):
        self.record += 1
        print(f"Ran for {self.record} time(s)")
        return self.func(*args, **kwargs)


@Record
def test():
    print("Run")


test()
test()
test()

''''
# Perform Flow Control on Function Inputs
# Check NOT Node

def check_not_None(func):
  def check(x):
    if x is not None:
      return func(x)
    else: 
      return 'is None'
  return check

@check_not_None
def f1(x):
  return x**1

@check_not_None
def f2(x):
  return x**2

@check_not_None
def f3(x):
  return x**3

print(f1(4))      # 4
print(f2(None))   # 'is None'
print(f3(4))      # 64
'''

#######################################
## CLASS DECORATOR EXPLAINED ##
print("==========================")
print("CLASS DECORATOR EXPLAINED")


# Here is a class that is decorator for a function, receive no arguments
class Power(object):
    def __init__(self, arg):
        self._arg = arg

    def __call__(self, a, b):
        retval = self._arg(a, b)
        return retval ** 2


@Power
def multiply_together(a, b):
    return a * b


print(multiply_together(3, 2))


################################
# Class Decorator that receive an argument but can also be without argument
class power(object):
    def __init__(self, arg):
        self._arg = arg

    def __call__(self, *param_arg):
        """If there are decorator arguments, __call__() is only called once
		as part of the decoration process. You can only give it a single argument,
		which is the function object
		If there are no decorator arguments, the function
		to be decorated is passed to the constructor.
		"""
        if len(param_arg) == 1:
            def wrapper(a, b):
                retval = param_arg[0](a, b)
                return retval ** self._arg

            return wrapper
        else:
            expo = 2
            retval = self._arg(param_arg[0], param_arg[1])
            return retval ** expo


# no argument - default square: result^2
@power
def multiply_together1(a, b):
    return a * b


# argument = n - default square: result^n
@power(4)
def multiply_together2(a, b):
    return a * b


print(multiply_together1(2, 2))  # output: 16 = (2*2)^2
print(multiply_together2(2, 2))  # output: 256 = (2*2)^4

#######################################

''''
*We Can Use Classes As Decorators*
Let’s say we have a simple function that greets someone

def hello(name):
    return "hello " + name
print(hello("fifi"))    # hello fifi

Let’s write our decorator class, and use it when defining our hello function

class append():
    def __init__(self, char):
        self.char = char
    def __call__(self, function):
        def inner(*args):
            return function(*args) + self.char
        return inner

@append("!")
def hello(name):
    return "hello " + name
print(hello("fifi"))    # hello fifi!
We can use multiple decorators on 1 function too:

@append("?")
@append("!")
def hello(name):
    return "hello " + name
print(hello("fifi"))    # hello fifi!?
'''

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

### ANOTHER SINGLEDISPATCH EXAMPLE
from functools import singledispatch
from decimal import Decimal

"""
When there is no registered implementation found, its MRO is used to find a more generic implementation. 
Hence the original function decorated is registered for the base object type, 
and is used if no other implementation is found.
"""


@singledispatch
def calc_num(num):
    raise NotImplementedError("cannot calculate for unknown number type")


@calc_num.register(int)
def calc_int(num):
    print(f"int: {num}")


@calc_num.register(float)
def calc_float(num):
    print(f"float: {num}")


"""
The decorator also supports decorator stacking, 
so we can create an overloaded function to handle multiple types.
"""


@calc_num.register(float)
@calc_num.register(Decimal)
def calc_float_or_decimal(num):
    print(f"float/decimal: {round(num, 2)}")


calc_num(1)
calc_num(1.0)
calc_num(1.02324)
# calc_num("num") #NotImplementedError: cannot cannot calculate for unknown number type

from functools import singledispatch
from dataclasses import dataclass


@dataclass
class Tea:
    kind: str
    temp: int


@dataclass
class Coffee:
    kind: str
    temp: int


@singledispatch
def boil(obj=None):
    raise NotImplementedError("No boiler instruction for this drink")


@boil.register(Coffee)
def _coffee_boil(obj):
    return "Successfully boiled coffee!"


@boil.register(Tea)
def _tea_boil(obj):
    return "Successfully boiled tea!"


tea = Tea(kind="white tea", temp=93)
coffee = Coffee(kind="Yunnan", temp=98)
print(boil(tea))  # output: Successfully boiled tea!
print(boil(coffee))  # output: Successfully boiled coffee!

''''
# Another SingleDispatch example:
Python@functools.singledispatch help to create a generic function composed of multiple functions implementing 
the same operation for different types. Which functions should be used during a call is determined 
by the dispatch algorithm.
### Without SingleDispatch ###
def func1(param):
    pass

def func2(param):
    pass

def func3(param):
    pass

def func4(param):
    pass

def main(param):
    if isinstance(param, int):
        return func1(param)
    elif isinstance(param, float):
        return func2(param)
    elif isinstance(param, str):
        return fun3(param)
    elif isinstance(param, list):
        return fun4(param)
##################
With SingleDispatch:
from functools import singledispatch

@singledispatch
def main(param=None):
    raise NotImplementedError("Implement process function.")
    
@main.register
def func1(param:int):
    return f"{param} is interger type. "

@main.register
def func2(param:float):
    return f"{param} is float type"

@main.register
def func3(param:str):
    return f"{param} is str type"

@main.register
def func4(param:list):
    return f"{param} is list type"

print(main(12))
print(main(12.3))
print(main("test"))
print(main([1,2,3,4]))



'''

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

'''
In python, everything is an object. And every object has attributes and methods or functions. 
Attributes are described by data variables for example like name, age, height etc.
Properties are special kind of attributes which have getter, setter and delete methods like 
__get__, __set__ and __delete__ methods.
However, there is a property decorator in Python which provides getter/setter access to an attribute Properties 
are a special kind of attributes.
'''


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
The self in instance methods refer to the instance object that calls the method, 
and the cls in the class method refers to the class (i.e., Student in our case).

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

Another example:
class Count:
   total_instances = 0
   def __init__(self):
      self.increment_count()
      pass
   @classmethod
   def increment_count(cls):
      cls.total_instances += 1

object_1 = Count()
object_2 = Count()
print(Count.total_instances) #output: 2
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

'''
Converting a Normal Method onto a Static One
A Static Method is a type of method in python classes that is bound to a particular state of the class. 
They can not access or update the state of the class. 
You can convert a normal method or instance method to a static method with the help of staticmethod(function)
class ABC:
    def abc(num1,num2):
        print(num1+numn2)


# changing torture_students into static method
ABC.abc = staticmethod(ABC.abc)

ABC.abc(4,5) ## 9
'''

'''
Difference between class method and static method

A staticmethod is a method that knows nothing about the class or instance it was called on. 
It just gets the arguments that were passed, no implicit first argument. 
It is basically useless in Python -- you can just use a module function instead of a staticmethod.

A classmethod, on the other hand, is a method that gets passed the class it was called on, 
or the class of the instance it was called on, as first argument. 
This is useful when you want the method to be a factory for the class: since it gets the actual class 
it was called on as first argument, you can always instantiate the right class, even when subclasses are involved. 
'''


class A(object):
    def foo(self, x):
        print(f"executing foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"executing class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"executing static_foo({x})")


a = A()
# Below is the usual way an object instance calls a method.
# The object instance, a, is implicitly passed as the first argument.
a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>, 1)
# With classmethods, the class of the object instance is implicitly passed as the first argument instead of self.
a.class_foo(1)
# executing class_foo(<class '__main__.A'>, 1)
# You can also call class_foo using the class.
# In fact, if you define something to be a classmethod, it is probably because you intend to call it
# from the class rather than from a class instance.
# A.foo(1) would have raised a TypeError, but A.class_foo(1) works just fine:
A.class_foo(1)
# executing class_foo(<class '__main__.A'>, 1)
# With staticmethods, neither self (the object instance) nor cls (the class) is implicitly passed as the first argument.
# They behave like plain functions except that you can call them from an instance or the class:
a.static_foo(1)
# executing static_foo(1)

A.static_foo('hi')
# executing static_foo(hi)
# Staticmethods are used to group functions which have some logical connection with a class to the class.

# foo is just a function, but when you call a.foo you don't just get the function,
# you get a "partially applied" version of the function with the object instance a bound as the first
# argument to the function. foo expects 2 arguments, while a.foo only expects 1 argument.

# a is bound to foo. That is what is meant by the term "bound" below:
print(a.foo)
# <bound method A.foo of <__main__.A object at 0xb7d52f0c>>
# With a.class_foo, a is not bound to class_foo, rather the class A is bound to class_foo.
print(a.class_foo)
# <bound method type.class_foo of <class '__main__.A'>>
# Here, with a staticmethod, even though it is a method, a.static_foo just returns a good
# 'ole function with no arguments bound. static_foo expects 1 argument, and a.static_foo expects 1 argument too.
print(a.static_foo)
# <function static_foo at 0xb7d479cc>
# And of course the same thing happens when you call static_foo with the class A instead.
print(A.static_foo)
# <function static_foo at 0xb7d479cc>


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

###
# __init__ is the initializer, some kind of first place to fill the object attributes,
# but when __init__ is called; the instance was already created.
# __new__ is the *real* constructor, it is here where the instance is created.


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
there is no naming conflict for a private method. Calling d.__private() will cause an Error
derive protected related to self of derived is chosen
'''


# Single inheritance enables a derived class to inherit properties from a single parent class,
# thus enabling code reusability and the addition of new features to existing code.

class P1:
    def mym11(self):
        print('Parent Method')


class Q1(P1):
    def mym12(self):
        print('Child Method')


a = Q1()
a.mym12()  # output: Child Method
a.mym11()  # output: Parent Method
print("##Single inheritance###")


# In multilevel inheritance, features of the base class and the derived class are further
# inherited into the new derived class. This is similar to a relationship representing a child and a grandfather.

class P2:
    def mym21(self):
        print('Parent Method')


class Q2(P2):
    def mym22(self):
        print('Child Method')


class R2(Q2):
    def mym23(self):
        print('Muli-level inheritance Method')


a = R2()
a.mym23()  # output: Muli-level inheritance Method
a.mym22()  # output: Child Method
a.mym21()  # output: Parent Method
print("##multilevel inheritance###")


# When a class can be derived from more than one base class this type of inheritance is called multiple inheritance.
# In multiple inheritance, all the features of the base classes are inherited into the derived class.

class P3:
    def mym31(self):
        print('Parent1 Method')


class Q3():
    def mym32(self):
        print('Parent2 Method')


class R3(Q3, P3):
    def mym33(self):
        print('Child Method')


a = R3()
a.mym33()  # output: Child Method
a.mym32()  # output: Parent2 Method
a.mym31()  # output: Parent1 Method
print("##multiple inheritance###")


# When more than one derived classes are created from a single base this type of inheritance is
# called hierarchical inheritance. In this program, we have a parent (base) class and two children (derived) classes.

class P4:
    def mym41(self):
        print('Parent Method')


class Q4(P4):
    def mym42(self):
        print('Child1 Method')


class R4(Q4, P4):
    def mym43(self):
        print('Child2 Method')


a = Q4()
b = R4()
a.mym42()  # output: Child1 Method
a.mym41()  # output: Parent Method
b.mym43()  # output: Child2 Method
b.mym41()  # output: Parent Method
print("##hierarchical inheritance###")


# The Python Method Resolution Order (MRO) defines the class search path used
# by Python to search for the right method to use in classes having multi-inheritance.

class A: pass


class B: pass


class C: pass


class D(A): pass


class E(B): pass


class F(D, E, C): pass


print(F.mro())  # output: [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>,


# <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

###### Multiply Inheritance Example ######
class BaseClassA:
    def __init__(self, hello: str, world: str = "test"):
        self.hello = hello
        self.world = world

    def method_from_a(self) -> str:
        return f"This is a method from class A with {self.hello}"

    def shared_method(self) -> str:
        return "This is A"


class BaseClassB:
    class_var = 0

    def method_from_b(self, input_var: int) -> int:
        self.class_var += input_var
        return self.class_var

    def shared_method(self) -> str:
        return "This is B"


class Inherited(BaseClassB, BaseClassA):
    def __init__(self, hello: str, world: str = "not test"):
        super().__init__(hello, world)
        self.inherited_var = []


inherited = Inherited("foo", "bar")
assert inherited.method_from_a() == "This is a method from class A with foo"
assert inherited.method_from_b(10) == 10
assert inherited.shared_method() == "This is B"  ## This is true only because of MRO rule,
# if a method is defined both in BaseClassA and BaseClassB, it will take the method from BaseClassB,
# as it is defined first.

''''
## Private Variables In Classes Are Not Really Private ##
class Dog():
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
        
In this Dog class, the __name attribute has a getter method but not a setter method. 
By right, we as users should only be able to read the __name attribute and not have permission 
to set a new name for our Dog object. But private variables are not that private.

dog = Dog("rocky")
print(dog.__dict__)   # {'_Dog__name': 'rocky'}

The __dict__ attribute contains all attributes of the object. 
Using the __dict__ attribute, we can control even variables and attributes that we aren’t supposed to have access to.

dog.__dict__["_Dog__name"] = "fifi"
print(dog.name)
# fifi 
'''

##########################################

####################
## COMPOSITION #####
print("===============")
print("COMPOSITION")


# Composition is a concept that models a has a relationship.
# It enables creating complex types by combining objects of other types.
# This means that a class can contain an object of another class.
# This relationship means that a class has a class.

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def Info(self):
        print('Student name is ', self.name, 'roll no ', self.rollno)


class Result:
    def __init__(self, name, rollno, marks):
        self.student = Student(name, rollno, marks)

    def printInfo(self):
        self.student.Info()


s = Result('sam', 233, 56)
s.printInfo()  # output: Student name is  sam roll no  233


# The composition is similar to inheritance but we cannot call the methods
# of the class that we defined inside the result class.

# Inheritance Vs Composition:
class Employee:
    def __init__(self, name, eid):
        self.name = name
        self.eid = eid

    def printDetails(self):
        print('Employee name is {} and Employee no is     {}'.format(self.name, self.eid))


# inheritance - is a relationship
class Supervisior(Employee):
    pass


# composition - has a relationship
class TL():
    def __init__(self, name, eid):
        self.employee = Employee(name, eid)

    def empDetails(self):
        self.employee.printDetails()


s = Supervisior('jon', 25)
t = TL('Tom', 30)
s.printDetails()  # output: Employee name is jon and Employee no is     25
t.empDetails()  # output: Employee name is Tom and Employee no is     30

# We can see that we can directly call a method of a parent class in subclass using Inheritance
# whereas in composition we have to define it under the other module.


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

'''
Object-Oriented Programming concepts
Creating class in Python
class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
    def __str__(self):
        return f"{self.sender} -> {self.recipient} : {self.amount}"

if __name__ == "__main__":
    transaction_1 = Transaction("Alice", "Bob", 100)
    print(transaction_1)
output:
Alice -> Bob : 100

Inheritance in Python
Define a base/parent class:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name} earns {self.salary}"

if __name__ == "__main__":
    e1 = Employee("John", 100)
    print(e1)
outputs:
John earns 100
Now we will define another class superclass/child class that extends the base class Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"{self.name} earns {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def __str__(self):
        return f"{self.name} earns {self.salary} and gets  {self.bonus} bonus"

if __name__ == "__main__":
    e1 = Employee("John", 100)
    e2 = Manager("John", 100, 10)
    print(e2)
output:
John earns 100 and gets 10 bonus
Polymorphism in Python
Polymorphism means more than one form, the same object performing different operations according to the requirement.
Polymorphism can be achieved by using two ways, those are
Method overriding
Method overloading
Method overloading means writing two or more methods *in the same class* by using same method name, 
but the passing parameters is different.
Method overriding means we use the method names *in the different classes*, which means parent class method 
is used in the child class.

Method Overloading in Python
When people do method overloading in languages like Java, they generally want a default value 
(if they don’t, they generally want a method with different parameters). 
In Python, we don’t do things that way. So, in Python, we can assign default values like the below:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def full_name(self, first_name=None, last_name=None):
        if first_name and last_name:
            return f"{first_name} {last_name}"
        else:
            return f"{self.name}"
if __name__ == "__main__":
    employee = Employee("John", 10000)
    print(employee.full_name())
    print(employee.full_name("John", "Doe"))

Output:
John
John Doe

Method Overriding in Python
class Dog:
    def bark(self):
        print("WOOF")

class BabyDog(Dog):
    def bark(self):
        print("WoOoOoF!")
if __name__ == "__main__":
    big_dog = Dog()
    big_dog.bark()
    baby_dog = BabyDog()
    baby_dog.bark()
output
WOOF
WoOoOoF!

Encapsulation in Python
The process of wrapping up variables and methods into a single entity is known as Encapsulation. 
It is one of the underlying concepts in object-oriented programming (OOP). 
It acts as a protective shield that puts restrictions on accessing variables and methods directly 
and can prevent accidental or unauthorized modification of data. We can implement encapsulation in the following way:
class Human:
    def __init__(self):
        self.__var = "private variable"
        self.var = "public variable"
    def print_var(self):
        # we can access the private variable in the class
        print(self.__var)
if __name__ == "__main__":
    h = Human()
    h.print_var()        # prints "private variable"
    
    print(h.var)         # prints "public variable"
    
    # private variable cannot be accessed outside the class 
    print(h.__var)       # does not work, will give error
'''

'''
What is Composition?
Composition is a concept that models a has a relationship. It enables creating complex types by combining 
objects of other types. This means that a class can contain an object of another class. 
This relationship means that a class has a class.

Example:
class Student:
 def__init__(self,name,rollno,marks):
  self.name = name
  self.rollno = rollno
  self.marks = marks
 def Info(self):
  print('Student name is ',self.name,'roll no ',self.rollno)
class Result:
 def __init__(self,name,rollno,marks)
  self.student = Student(name,rollno,marks)
 def printInfo:
  self.student.Info()
s = Result('sam',233,56)
s.printInfo()
The composition is similar to inheritance but we cannot call the methods of the class that we defined inside the result class.
'''

'''
Inheritance is defined as ‘is a relationship’ whereas composition is defined as ‘has a relationship’. 
In inheritance, a class is derived as a subclass of another class whereas in composition a class is somewhat 
called inside another class.

class Employee:
 def __init__(self,name,eid):
  self.name = name  
  self.eid = eid
 def printDetails(self):
  print('Employee name is {} and Employee no is     {}'.format(self.name,self.eid))
#inheritance - is a relationship
class Supervisior(Employee):
 pass
#composition - has a relationship
class TL():
 def __init__(self,name,eid):
  self.employee = Employee(name,eid)
 def empDetails(self):
  self.employee.printDetails()

Test:
s = Supervisior('jon',25)
t = TL('Tom',30)
s.printDetails()
t.empDetails()
Employee name is jon and Employee no is 25
Employee name is Tom and Employee no is 30;
'''
"""
## Static and Class methods can be inherited ##

class A:
    def __init__(self,attr1=1,attr2=2):
        self.attr1=attr1
        self.attr2=attr2

    def instance_method(self):
        print(f"info of class {self} with attributes attr1: {self.attr1} attr2: {self.attr2}")

    @classmethod
    def get_instance(cls,atr1,atr2):
        print(f"class method of {cls}")
        return cls(atr1,atr2)

    @staticmethod
    def static_func(in1,in2):
        print(f"static method of A")

class DeriveA(A):
    def __init__(self,a1,a2,da1=111,da2=222):
        self.derattr1 = da1
        self.derattr2 = da2
        super().__init__(a1,a2)

    def instance_method(self):
        print(f"info of class {self} with attributes derattr1: {self.derattr1} derattr2: {self.derattr2}")


a_sample = A(15,3)
a_sample.instance_method() #info of class <__main__.A object at 0x00000217CAD9FEE0> with attributes attr1: 15 attr2: 3
print("class method:\n")
a_sample.get_instance(11,22).instance_method()
#class method of <class '__main__.A'>
#info of class <__main__.A object at 0x00000217CAD9FF70> with attributes attr1: 11 attr2: 22
A.static_func(2,3) # static method of A

da_sample = DeriveA(1,2,3,4)
da_sample.instance_method() 
# info of class <__main__.DeriveA object at 0x00000217CAD9FF70> with attributes derattr1: 3 derattr2: 4
da_sample.get_instance(20,30).instance_method()  # class method of <class '__main__.DeriveA'>
# info of class <__main__.DeriveA object at 0x00000217CAD9FE20> with attributes derattr1: 111 derattr2: 222
da_sample.static_func(5,6) # static method of A bn           
"""
''''
How Abstract Base classes work :
By default, Python does not provide abstract classes. Python comes with a module that provides the base for 
defining Abstract Base classes(ABC) and that module name is ABC. ABC works by decorating methods of the base class 
as abstract and then registering concrete classes as implementations of the abstract base. 
A method becomes abstract when decorated with the keyword @abstractmethod.
Let us see an example of how the abstract method works:

from abc import *

class Newinterface(ABC):
 @abstractmethod
 def connect(self):
  pass
 @abstractmethod
 def disconnect(self):
  pass

class Videocard(Newinterface):
 def connect(self):
  print(‘connecting videocard’)
 def disconnect(self):
  print(‘disconnecting videocard’)

class TPU(Newinterface):
 def connect(self):
  print(‘connecting TPU’)
 def disconnect(self):
  print(‘disconnecting TPU’)

a = TPU()
a.connect()
a.disconnect()

#outputs:
connecting TPU
disconnecting TPU
'''
'''
We can say that there are two types of implementation: overloading (@ compile-time) and overriding (@ runtime). 
Overloading is not supported in Python, however, we can use a Python package, multipledispatch that does overloading.

Overriding
Methods owned by parent classes are rewritten in child classes and customized according 
to the intended use of these child classes. 
Now let me explain the subject with an example. 
I have a method, it accepts a device and opens it by pressing the button as long as the device has a device.
@@ Example:

from abc import ABC

class ADevice(ABC):
    @abc.abstractclassmethod
    def press_button(self):
        pass

class Device(ADevice):
    def press_button(self):
        print("Starting Device..")

def open_device(device):
    try:
        device.press_button()
    except AttributeError:
        print("This device has no button to open..")

class Laptop(Device):
    def press_button(self):
        print("Starting CPU..")

class Television(Device):
    def press_button(self):
        print("Starting Screen..")

class Speaker(Device):
    def press_button(self):
        print("Playing Sound..")

L,T,S = Laptop(),Television(),Speaker()
device_list = [L,T,S]

for d in device_list:
    open_device(d)

## output:
#Starting CPU..
#Starting Screen..
#Playing Sound..
'''
'''
Overloading in Python
Python doesn’t support overloading as Java does. It can be applied indirectly. I will use multipledispatch package.

from multipledispatch import dispatch

class Car:
    def __init__(self):
        self.speed=100

    @dispatch()
    def accelerate(self):
        self.speed+=10

    @dispatch(int)
    def accelerate(self,acc):
        self.speed+=acc

    @dispatch(float)
    def accelerate(self,acc):
        self.speed+=(self.speed*acc)

    @dispatch(int,float)
    def accelerate(self,acc,percentage):
        acc*=percentage
        self.speed+=acc

    def get_speed(self):
        print(f"Current speed is: {self.speed}")

C = Car()
C.accelerate()
C.get_speed() #output: Current speed is: 110
C.accelerate(20)
C.get_speed() #output: Current speed is: 130
C.accelerate(0.1)
C.get_speed() #output: Current speed is: 143.0
C.accelerate(50,0.1)
C.get_speed() #output: Current speed is: 148.0
'''

'''
How to create a Python class without using the class keyword!
The ‘type’ Function With 3 Arguments
NewClass = type(name, bases, dict)
If we pass in 3 arguments into the type function, it dynamically creates and returns a new class for us.

name → The name of the class, accessible by __name__
bases → A tuple that contains the base classes that our new class inherits from, accessible by __bases__.
dict → A dictionary containing attributes and methods of our new class, accessible by __dict__.
SO:
Regular way:
Dog Class To Inherit From Animal Class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("hi")
class Dog(Animal):
    def speak(self):
        print("woof")
        
Without 'class':
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("hi")
Dog = type("Dog", (Animal,), {"speak":lambda self:print("woof")})

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

# Iterators #
# If you want to create your own iterator, you just have to implement the __next__ and __iter__methods.
# __iter__ should return the iterator object (so it return self in most cases)
# __next__ should return the next element of the data structure
print("=== Private Iterators Implementation ====")


class Backward():
    def __init__(self, data):
        self.data = data  # The list we want to iterate
        self.index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if (self.index == 0):
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]


bw = Backward([1, 2, 3, 4, 5])
for elem in bw:
    print(elem, end=',')  # output: 5,4,3,2,1,

print("")

#### Accessing a class as a list ####
print("====================================")
print("==== Accessing a class as a list ==")


# When we are using lists, we can access specific values using square brackets.
# It would be nice to be able to implement something similar for our own classes.
# We can use __getitem__ and __setitem__ to do just that. These are the methods that are called
# by a list when we use the square brackets:
# x = l[idx] is the same as writing x = l.__getitem__(idx)
# l[idx] = x is the same as writing l.__setitem__(idx, x)
# So if we implement these two methods in our class, we will then be able to use the square brackets
# as we would do for a list.
# Here is a really easy example (it is a list whose size cannot be changed, and whose index start at 1):

class MyList():
    def __init__(self, dimension):
        self.l = [0 for i in range(dimension)]

    def __getitem__(self, idx):
        return self.l[idx - 1]

    def __setitem__(self, idx, data):
        self.l[idx - 1] = data


ml = MyList(5)
ml[1] = 50  # Set the first element of ml to 50
ml[2] = 100  # Set the second element of ml to 100
x = ml[1]  # x is now 50

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
'''
Generator functions allow you to declare a function that behave like an iterator, i.e. it can be used in a for loop. This greatly simplifies your code and is much more memory efficient than a simple for loop.
Example:
def simpleGeneratorFun():
 yield 1 
 yield 2
 yield 3
for value in simpleGeneratorFun():
 print(value)
#Output:
1
2
3
'''

'''
Iterator, and Generator for Beginners
---------------------------------------
An iterable is an object that can return an iterator (to return all of its elements), for example:
mylist = ['a', 'b', 'c']
for i in mylist:
     print(i)

Objects that can be iterated using a for loop are iterable objects. 
The 'strings', 'lists', 'files', etc. that we commonly use are all iterable objects.

How do iterables work?
It calls iter(x) function
It checks whether the object implements the __iter__ method, and if it is implemented, call it to obtain an iterator
If the __iter__ method is not implemented, but the __getitem__ method is implemented, Python will create an iterator and try to get the elements in order (starting at index 0)

Therefore objects with __iter__() methods or __getitem__() methods are usually called iterable objects .

An iterator is an object that contains a countable number of values. 
It can be iterated upon, meaning that you can traverse through all the values. Iterator example:
for i in range(5):
    print(i)

In simple words, an iterable object with a next() method is an iterator, 
or the relationship between an iterable object and an iterator is: Python obtains an iterator from an iterable object.

So lists, strings, etc.. that mentioned above are not iterators. 
However, you can use Python’s built-in iter() function to obtain their iterator objects. 
Let us use the iterator pattern to rewrite the previous example:
mylist = [1,2,3]
it = iter(mylist)
while True:
    try:
        print(next(it))
    except StopIteration:
        print("Stop iteration!")
        break

Python provides a generator to create your iterator function. 
A generator is a special type of function which does not return a single value, 
instead, it returns an iterator object with a sequence of values. 
In a generator function, a yield statement is used rather than a return statement.

If the amount of data is too large, such as for i in range(1000000), using the for loop 
to store all values in memory not only takes up a lot of storage space but also 
if we only need to access the first few elements, the space is wasted. 
In this case, we can use generator .
The idea of the generator is that we don’t need to create this list all at once, 
we just need to remember its creation rules, and then when we need to use it, 
we will calculate and create it again and again. Let’s take a look at one example:
my_generator = (x*x for x in range(10))
for i in my_generator:
    print(i)

You can think of yield as a return, but what it returns is a generator.
If a function uses yield as return value, then it becomes a generator function.

Unlike normal functions, after the generator function is called, the code in the function body is not executed immediately , 
but a generator is returned!
As we mentioned earlier, generator is iterator and yield can be treated as return:
def test():
    print("First")
    yield 1
    print("Second")
    yield 2
    print("Third")
    yield 3

my_generator = test()
print(type(my_generator)) # Output: <class 'generator'>

for item in my_generator:
    print(item)

# output:
# First
# 1
# Second
# 2
# Third
# 3

next(my_generator) # output: First
next(my_generator) # output: Second
next(my_generator) # output: Third
next(my_generator) # Error with StopIteration

Every time next(my_generator) is called, it only runs to the yield position and stops, 
and the next time it runs, it starts from the position where it ended last time! 
And the length of the generator depends on the number of times the yield is defined in the function.

def simple_gen(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
gen = simple_gen(14)
next(gen) #output: -> Started: a = 14

Since each time you call next(gen) , it will stop at the next yield run, so in the above example, 
the b = yield a was not fully executed, only the right side yield a was executed. 
That’s why you don’t see the -> Received: b= in the output.

In case of next(gen) again. The output is: 
-> Received: b = None
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

Since the first next(gen) call, it stopped at yield a , 
then when you call next(gen) again, b is actually None value, 
and this has caused an exception. 

To proceed, you will need to use the Send() function:
generator.send(value)

The send() method returns the next value yielded by the generator or raises StopIteration if the generator exits 
without yielding another value. When send() is called to start the generator, it must be called with None as the 
argument, because no yield expression could receive the value.

def simple_gen(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)
gen = simple_gen(14)
next(gen)
gen.send(15)
Output:
-> Started: a = 14
-> Received: b = 15
'''


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
import sys

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
# with open("people.pickle", "wb") as file:
#     pickle.dump(man, file)
#     file.close()

# To unpickle something:
# with open("people.pickle", "rb") as file:
#     new_man = pickle.load(file)
#     print(new_man)  # output: This is Dan Belfer aged 48

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


# Handling if-else logic in pro mode
# You would usually write your if else logic like given below:

TABLE_CREATION = 'table_creation'
TABLE_DROP = 'table_drop'
FETCH_ALL = 'fetch_all'


def run_table_creation():
    pass


def run_table_drop():
    pass


def run_fetch_all():
    pass


def query_handler(status):
    if status == TABLE_CREATION:
        run_table_creation()
    elif status == TABLE_DROP:
        run_table_drop()
    elif status == FETCH_ALL:
        run_fetch_all()


query_handler(TABLE_CREATION)  # this would run table creation
query_handler(TABLE_DROP)  # this would run table drop
query_handler(FETCH_ALL)  # this would run fetch all

# but you can rewrite this whole logic in a more pro more, her’s how:
TABLE_CREATION = 'table_creation'
TABLE_DROP = 'table_drop'
FETCH_ALL = 'fetch_all'


def run_table_creation():
    pass


def run_table_drop():
    pass


def run_fetch_all():
    pass


handlers = {
    TABLE_CREATION: run_table_creation,
    TABLE_DROP: run_table_drop,
    FETCH_ALL: run_fetch_all
}


def query_handler(status):
    handler = handlers[status]
    handler()


query_handler(TABLE_CREATION)  # this would run table creation
query_handler(TABLE_DROP)  # this would run table drop
query_handler(FETCH_ALL)  # this would run fetch all

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

## Replace Using “or” to Check Multiple Conditions in Python with "in"
""" 
Instead of using multiple or:
if number == 1 or number == 2 or number == 3 or number == 4:
    do_smt()

Use in:
if number in [1, 2, 3, 4]:
    do_smt()    
"""

''''
Python supports the most common if/else conditional statements, 
but it lacks switch/case statements support which is common in other programming languages.
## Avoid Multi-level Conditional Statements ##
Too deep branch nesting is one of the most common mistakes many novice programmers make. 
If a new programmer writes many levels of branch nesting, 
you may see levels of curly braces: if { if { if { ... }}}. Commonly known as "Nested If Statement Hell" .
Since Python uses indentation instead of {} , deeply nested branches can have more serious consequences. 
Let’s take a look at the following bad example:

def buy_car(customer, store):
    if store.is_open():
        if store.has_stocks("car"):
            if customer.can_afford(store.price("car", amount=1)):
                customer.buy(store, "car", amount=1)
                return
            else:
                customer.not_buy()
                return
        else:
            raise CarBuyingException("no car in store!")
    else:
        raise CarBuyingException("store is closed!")
        
        
One technique called “Early termination” can be used here:

def buy_car(customer, store):
    if not store.is_open():
        raise CarBuyingException("store is closed!")

    if not store.has_stocks("car"):
        raise CarBuyingException("no car in store!")

    if customer.can_afford(store.price("car", amount=1)):
        customer.buy(store, "car", amount=1)
        return
    else:
        customer.go_home()
        return
        
“Early termination” means: using return or raisestatement to end a function early within a branch. 
For example, in the new buy_car function , when the branch condition is not satisfied, 
we directly throw an exception to end this code branch. Such code has no nested branches, 
is more direct and easier to read.

## Encapsulate Over Complex Logicals ##
If the expression in the conditional branch is too complex and there are too many not/and/or, 
the readability of this code will be greatly reduced, such as the following code:

if activity.is_active and activity.remaining > 10 and \
        user.is_active and (user.sex == 'female' or user.level > 3):
    user.add_points(100)
    return

For such code, we can consider encapsulating specific branch logic into functions or methods to simplify the code:

if activity.allow_new_user() and user.match_activity_condition():
    user.add_points(100)
    return
    
## Avoid Duplicate Code ##
Duplicate code is the natural enemy of code quality, 
and conditional branch statements are very easy to become the hardest hit area for duplicate code. 
Therefore, when we write conditional branch statements, 
we need to pay special attention not to produce unnecessary duplication of code.

Let’s take a look at the following code example:

if user.no_profile_exists:
    create_user_profile(
        username=user.username,
        email=user.email,
        age=user.age,
        address=user.address,
        points=0,
        created=now(),
    )
else:
    update_user_profile(
        username=user.username,
        email=user.email,
        age=user.age,
        address=user.address,
        updated=now(),
    )

In the above code, we can see at a glance that under different branches, 
the program calls different functions and does different things. 
However, because of the existence of those repetitive codes, 
it is difficult for us to simply distinguish the difference between the two.

In fact, thanks to the dynamic nature of Python, the above code can be rewritten into:

if user.no_profile_exists:
    profile_func = create_user_profile
    extra_args = {'points': 0, 'created': now()}
else:
    profile_func = update_user_profile
    extra_args = {'updated': now()}

profile_func(
    username=user.username,
    email=user.email,
    age=user.age,
    address=user.address,
    **extra_args
)

## De Morgan’s Law ##
In simple words, De Morgan’s law means:

not (A or B) = (not A) and (not B)
not (A and B) = (not A) or (not B)
Sometimes if you see code like the following:

if not user.has_logged_in or not user.is_from_chrome:
    return "our service is only available for chrome logged in user"

You can use De Morgan’s law to improve the readability, by rewritten the above code to:

if not (user.has_logged_in and user.is_from_chrome):
    return "our service is only available for chrome logged in user"
        
## Use all() and any() ##
The all() and any()two functions are very suitable for use in conditional judgments. 
These two functions take an iterable and return a boolean where:

all(seq): return only seq if all objects in are boolean true True, otherwise return False
any(seq): Return as long seq as any object in is boolean true True, otherwise return False
For example, suppose we have the following code:

def all_numbers_larger_than_ten(numbers):
    if not numbers:
        return False

    for n in numbers:
        if n <= 10:
            return False
    return True

Using the all()built -in function, combined with a simple generator expression, 
the above code can be written like this:

def all_numbers_larger_than_ten(numbers):
    return bool(numbers) and all(n > 10 for n in numbers)

'''
''''
Improve Readability By Defining Temporary Variables
As business logic becomes complex, some complex expressions often appear in our code, like the following:

if user.is_active and (user.sex == 'female' or user.level > 3):
    user.add_points(000)
    return
Kind of hard to read, right? But although the logic is so, 
it does not mean that we have to write the code directly in this way. 
The code can be made more readable if the complex expression that follows is assigned to a temporary variable:

user_is_eligible = user.is_active and (user.sex == 'female' or user.level > 3):
if user_is_eligible:
    user.add_points(100)
    return
'''

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

## OR another example ##
num_lst = range(1, 12, 2)
print(num_lst)  # output: range(1, 12, 2)
# using * unpacking
print(*num_lst)  # output: 1 3 5 7 9 11

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
### **** NOTICE: assert should not come with () - because assert(True == False, 'This would never fail')
### will always be true - because there is tuple: (True ==...) and it is not empty, it is true always!!!

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

"""
Emulate switch case as Dictionary:
Original function:
def calculator(operator, x, y):
   if operator == 'add':
      add(x, y)
   elif operator == 'sub':
      sub(x, y)
   elif operator == 'mul':
      mul(x, y)
   elif operator == 'div':
      div(x, y)
   else:
      return None

Becomes:
def calculator(operator, x, y):
   return {
      'add': lambda: x + y,
      'sub': lambda: x - y,
      'mul': lambda: x * y,
      'div': lambda: x / y,
   }.get(operator, lambda: None)()
"""

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

# Sum of digits in number
sum_of_digit = lambda x: sum(map(int, str(x)))
output = sum_of_digit(123)
# print("Sum of the digits is: ", output)
# Output:
# Sum of the digits is: 6

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

### QUEUE CLASS IMPLEMENTATION ###
print("=====================================")
print("Queue class implementation")


class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        myString = ' '.join(str(i) for i in self.queue)
        return myString

    def enqueue(self, item):
        '''This function adds an item to the rear end of the queue '''
        if (self.isFull() != True):
            self.queue.insert(0, item)
        else:
            print('Queue is Full!')

    def dequeue(self):
        ''' This function removes an item from the front end of the queue '''
        if (self.isEmpty() != True):
            return self.queue.pop()
        else:
            print('Queue is Empty!')

    def isEmpty(self):
        ''' This function checks if the queue is empty '''
        return self.queue == []

    def isFull(self):
        ''' This function checks if the queue is full '''
        return len(self.queue) == self.size

    def peek(self):
        ''' This function helps to see the first element at the fron end of the queue '''
        if (self.isEmpty() != True):
            return self.queue[-1]
        else:
            print('Queue is Empty!')


MyQuere = Queue(10)
MyQuere.enqueue(1)
MyQuere.enqueue(2)
MyQuere.enqueue(3)
MyQuere.enqueue(4)

print(MyQuere)  # output: 4 3 2 1
print(MyQuere.peek())  # output: 1
print(MyQuere.isFull())  # output: False
print(MyQuere.dequeue())
print(MyQuere)  # output: 4 3 2

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

## Dispatch example
print("#################")
print("Dispatch example")
import datetime


def do_monday():
    print("Monday")


def do_tuesday():
    print("Tuesday")


def do_wednesday():
    print("Wednesday")


def do_thursday():
    print("Thursday")


def do_friday():
    print("Friday")


def do_saturday():
    print("Saturday")


def do_sunday():
    print("Sunday")


my_special_day = datetime.date.today()

print("long if-else solution")
if my_special_day.weekday() == 0:
    do_monday()
elif my_special_day.weekday() == 1:
    do_tuesday()
elif my_special_day.weekday() == 2:
    do_wednesday()
elif my_special_day.weekday() == 3:
    do_thursday()
elif my_special_day.weekday() == 4:
    do_friday()
elif my_special_day.weekday() == 5:
    do_saturday()
elif my_special_day.weekday() == 6:
    do_sunday()

print("Short dispatch solution")

dispatch = {
    0: do_monday,
    1: do_tuesday,
    2: do_wednesday,
    3: do_thursday,
    4: do_friday,
    5: do_saturday,
    6: do_sunday
}

dispatch[my_special_day.weekday()]()

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

## sum digits in number
# alternative to sum digit of number - replace to string which is iterable and use map function that iterate each char
# number = 1234
# print(sum(map((int), str(number))))

## DIGITAIZING a Number
# Digitizing means converting a number into an array or list.
# This comes in handy when you need to convert a large number into a list form.
print("===========================")
print("DIGITAIZING a Number:")


def Digitizing(num):
    return list(map(int, str(num)))


num1 = 4858
num2 = 7804
print(Digitizing(num1))  # [4, 8, 5, 8]
print(Digitizing(num2))  # [7, 8, 0, 4]

# Digitizing
integer = 234553
digitz = [int(i) for i in str(integer)]
print(digitz)  # [2, 3, 4, 5, 5, 3]

## Convert Hexadecimal Color Codes to RGB Code
print("===========================")
print("HEX To RGB:")


def Hex_To_Rgb(hex):
    rgb = tuple(int(hex[x: x + 2], 16) for x in (0, 2, 4))
    return rgb


print(f"FF5733 is: {Hex_To_Rgb('FF5733')}")  # (255, 87, 51)
print(f"33D8FF is: {Hex_To_Rgb('33D8FF')}")  # (51, 216, 255)

## Convert List of Lists to a Single List ##
import itertools

mylist = [[-2, -3], [10, 30], ['apple', 'orange']]

print(list(itertools.chain.from_iterable(mylist)))


# Output:
# [-2, -3, 10, 30, 'apple', 'orange']

## Convert Two Lists into a Dictionary
def list_to_dictionary(keys, values):
    return dict(zip(keys, values))


list1 = ["Name", "Age", "City"]
list2 = ['Roy', 26, "New York"]

print(list_to_dictionary(list1, list2))
# output: {'Name': 'Roy', 'Age': 26, 'City': 'New York'}
##

## Merge Two Dictionaries
dictionary1 = {"name": "Jeff", "age": 26}
dictionary2 = {"name": "Jeff", "city": "New York"}

merged_dict = {**dictionary1, **dictionary2}

print("Merged dictionary is:", merged_dict)


# output: Merged dictionary is: {'name': 'Jeff', 'age': 26, 'city': 'New York'}

## Convert any class into a dictionary
# Classes have an inbuilt attribute __dict__ which means objects that are created are dictionaries
# and can be used like one when needed.

class Obj:
    def __init__(self, a='test', b=108):
        self.a = a
        self.b = b


obj = Obj()
print(vars(obj))  # vars() is pythonic way to convert to dictionary
# output: {'a': 'test', 'b': 108}

## Quick Sort in one line
print("===========================")
print("Quick Sort in one line:")

lst = [12, 45, 2, 6, 67, 32, 98, 52, 68, 13, 91, 18, 36, 29, 57, 72, 1, 5, 8]
qsort = lambda l: l if len(l) <= 1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort(
    [x for x in l[1:] if x >= l[0]])
print(qsort(lst))  # output: [1, 2, 5, 6, 8, 12, 13, 18, 29, 32, 36, 45, 52, 57, 67, 68, 72, 91, 98]
print(lst)  # output: [12, 45, 2, 6, 67, 32, 98, 52, 68, 13, 91, 18, 36, 29, 57, 72, 1, 5, 8]

## longest string in from a list
print("===========================")
print("longest string in from a list:")
words = ['This', 'is', 'a', 'list', 'of', 'words']
print(max(words, key=len))  # output: 'words'

##  Find the element with the highest frequency
print("===========================")
print("Find the element with the highest frequency:")
new_list = ['a', 'b', 'a', 'd', 'e', 'g', 'g', 'a', 'c', 'f', 'k', 't', 'u', 'z', 'x', 'a']
print("Most frequent element:", max(set(new_list), key=new_list.count))  # output: Most frequent element: a

## Finding sub-strings from a list of strings
print("===========================")
print("Finding sub-strings from a list of strings:")
data = [
    "Python, Programming Language",
    "Meta, Mark Zuckerberg",
    "Sebastian Vettel, F1 racer",
    "Alexa, Amazon"
]
# Method 1
name = "Meta"
for data in data:
    if data.find(name) >= 0:
        print(data)  # output: Meta, Mark Zuckerberg

# Method 2
name = "Vettel"
for data in data:
    if name in data:
        print(data)

## Count the frequency of a character in a string
print("===========================")
print("Count the frequency of a character in a string:")
print("umbrella".count('l'))  # output 2

## Most frequent element in list
print("===========================")
print("Most frequent element in list:")
numbers = [9, 4, 5, 4, 4, 5, 9, 5, 4]
most_frequent_element = max(set(numbers), key=numbers.count)
print(f"most_frequent_element: {most_frequent_element}")  # 4

## Rotate a list
print("===========================")
print("Rotate a list:")
li = [1, 2, 3, 4, 5]
# right to left
# li[n:] + li[:n] # n is the no of rotations
print(f"right to left: {li[2:] + li[:2]}")  # [3, 4, 5, 1, 2]
# left to right
# li[-n:] + li[:-n]
# li[-1:] + li[:-1]
print(f"left to right: {li[-1:] + li[:-1]}")  # [5, 1, 2, 3, 4]

# Python One Line Nested/Double Loop
# example code Multi-Line Loop
lst1 = [1, 2]
lst2 = ["x", "y"]
for x in lst1:
    for y in lst2:
        print(x, y)

# example Code of Single Line Loop
[print(x, y) for x in lst1 for y in lst2]
# Output
# 1 x
# 1 y
# 2 x
# 2 y

# Python One Line String to Integer
strlist = ["1", "2", "3", "4", "5"]
intlist = list(map(int, strlist))
print(intlist)  # [1, 2, 3, 4, 5]

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

## Replace nested loop with itertools.product
for i in range(2):
    for j in range(2):
        print(f"i={i} and j={j}")

print("+++++ The same ++++++++")

import itertools

for i, j in itertools.product(range(2), range(2)):
    print(f"i={i} and j={j}")

'''
output: 
i=0 and j=0
i=0 and j=1
i=1 and j=0
i=1 and j=1
+++++++++++++
i=0 and j=0
i=0 and j=1
i=1 and j=0
i=1 and j=1
'''

# Use itertools chain example
from itertools import chain

li = ['ABC', 'DEF', 'GHI', 'JKL']
# using chain-single iterable.
res1 = list(chain(li))
res2 = list(chain.from_iterable(li))
print("using chain :", res1, end="\n\n")  # output: ['ABC', 'DEF', 'GHI', 'JKL']
print("using chain.from_iterable :", res2)  # output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

## tee usage - Compare or apply some operation between each pair of adjacent elements
from itertools import tee
from typing import Iterable


def window2(iterable: Iterable):
    it, offset = tee(iter(iterable))
    next(offset)
    return zip(it, offset)


l = [1, 2, 3, 4, 5, 6]
window2(l)  # Is the same that: ((1,2), (2,3), (3, 4), ...)

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

## Examples of one-liners:
'''
# Palindrome Python One-Liner
phrase.find(phrase[::-1])

# Swap Two Variables Python One-Liner
 a, b = b, a

# Sum Over Every Other Value Python One-Liner
 sum(stock_prices[::2])

# Read File Python One-Liner
 [line.strip() for line in open(filename)]

# Factorial Python One-Liner
 reduce(lambda x, y: x * y, range(1, n+1))

# Performance Profiling Python One-Liner
 python -m cProfile foo.py

# Superset Python One-Liner
 lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])

# Fibonacci Python One-Liner
 lambda x: x if x<=1 else fib(x-1) + fib(x-2)

# Quicksort Python One-liner
 lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])

# Sieve of Eratosthenes Python One-liner
 reduce( (lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n)))
'''

## dataclasses ##
print("===========================")
print("dataclasses")
'''
There are several advantages over regular classes or other alternatives like returning multiple values or dictionaries:
a data class requires a minimal amount of code
you can compare data classes because __eq__ is implemented for you
you can easily print a data class for debugging because __repr__ is implemented as well
data classes require type hints, reduced the chances of bugs

dataclass vs. Named Tuple:
The use of Data Class is most often compared with the use of Named Tuple. 
For the most part, Data Class offers the same advantage if not more than Named Tuple.
In the case where you need to unpack your variables, you might want to consider using Named Tuple instead.

dataclass vs. Dictionary
When our Dictionary has a fixed set of keys where their corresponding values have fixed types, 
it is almost always better to use Data Class.
In short, the rule of thumb is rather simple, if you create a dictionary or a class that mostly consists of 
attributes about the underlying data, use Data Class. It saves you a bunch of time.
Finally, Data Class also preserves type information for each property, which is a huge added advantage!
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

'''
Custom attribute behaviour with the field function
In some situations, you may need to create an attribute that is only defined internally, 
not when the class is instantiated. This may be the case when the attribute has a value that depends on 
previously-set attributes.
Here’s where you’d use the field function from dataclasses.
By using this function and setting itsinit and repr arguments to False to create a new field called full_name, 
we can still instantiate a Person class without setting the full_name attribute.
'''
from dataclasses import dataclass, field, astuple, asdict


@dataclass
class Person:
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "Data Scientist"
    full_name: str = field(init=False, repr=True)

    def __post_init__(self):
        self.full_name = self.first_name + " " + self.last_name


# Note that the repr argument inside the field function has been set to True to make it visible
# when the object is printed.
'''
Using dataclasses, you can create objects that are read-only. 
All you have to do is set the frozen argument to True inside the @dataclass decorator.
'''


@dataclass(frozen=True)
class Person1:
    first_name: str = "Ron"
    last_name: str = "Ronniel"
    age: int = 20
    job: str = "Artist"


'''
When you do this, you prevent anyone from modifying the values of the attributes once the object is instantiated.
If you try to set a frozen object’s attribute to a new value, a FrozenInstanceError error will be raised.
'''

'''
Instances can easily be serialized into dicts or tuples. 
This is very useful when your code interacts with other programs that expect these formats.
'''

ahmed = Person()
print(astuple(ahmed))
# ('Ahmed', 'Besbes', 30, 'Data Scientist')

print(asdict(ahmed))
# {'first_name': 'Ahmed',
# 'last_name': 'Besbes',
# 'age': 30,
# 'job': 'Data Scientist'}

'''
The attribute 'full_name' doesn’t exist yet in the instance. If we try to access it, an AttributeError is thrown.
'''
p_example = Person(first_name='Dan', last_name='Belfer', age=49, job='QA')
# print(p_example.full_name)  ## will throw an error that there is no attribute of 'full_name'
# To set the value of full_name and still keep it out of the constructor of the class?
# To do this, we’ll have to use the __post_init__method.

'''
dataclasses has a special method called __post_init__ .
As the name clearly suggests, this method is called right after the __init__ method is called.
Going back to the previous example, we can see how this method can be called to initialize 
an internal attribute that depends on previously set attributes.
Note that the repr argument inside the field function has been set to True 
to make it visible when the object is printed. 
'''


@dataclass
class Car:
    name: str = field(compare=False)  # To exclude this field from comparison
    brand: str = field(repr=False)  # To hide fields in __repr__
    price: int = 120_000
    condition: str = field(default='New')


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

# working with 'is' and 'is not'
a = "string"
b = "string"
b1 = a
print(id(a))  # 2262644416240
print(id(b))  # 2262644416240
print(a is b)  # True
print(a == b)  # True
print(a is not b1)  # False

c = ["string"]
d = ["string"]
d1 = c
print(id(c))  # 2262643597376
print(id(d))  # 2262702838464
print(c is d)  # False
print(c == d)  # True
print(c is not d1)  # False


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

####################################################################
print("### ITERTOOLS ###")

import itertools
import operator

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)
for each in result:
    print(each)

# 1
# 2
# 6
# 24
# 120

# compress - This function filters one iterable with another

countries = ['Pakistan', 'China', 'India', 'Afghanistan']
selections = [True, False, True, False]
result = itertools.compress(countries, selections)
for each in result:
    print(each)

# output:
# Pakistan
# India

#####################
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = itertools.dropwhile(lambda x: x < 5, data)
for each in result:
    print(each, end=" ")


# output: 5 6 7 8 9 10
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
General Singleton mechanism
class Singleton:
    __instance = None
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance
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


s1 = Singleton_Student("Dan", "Belfer")  # Running __new__() method.
# Running __init__() method.
s2 = Singleton_Student("Elon", "Musk")  # Running __new__() method.
# Running __init__() method.

print(s1)  # <__main__.Singleton_Student object at 0x7ff1e5a53198>
print(s2)  # <__main__.Singleton_Student object at 0x7ff1e5a53198>
print(s1 == s2)  # True
print(s1.last_name)  # Musk
print(s2.last_name)  # Musk

"""
Another example:
class SingletonPattern:     
    def __new__(cls, *args, **kwargs):   
        if cls._instance is None: # Checking if an instance of this class exists            
            cls._instance = super().__new__(cls, *args, **kwargs) # Creating a new instance           
        return cls._instance # Returing the instance 
"""

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

## Another Abstract class example
from abc import ABC, abstractmethod


class Calculation(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    def multiply(self):
        print('Method of an Abstract Class can be called without error',
              'because abstract method decorator is not used')

    @abstractmethod
    def division(self):
        pass


class Calculator(Calculation):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def subtract(self):
        print(self.a - self.b)

    def division(self):
        print(self.a / self.b)


take = Calculator(10, 5)
take.add()  # 15
take.subtract()  # 5
take.division()  # 2.0
take.multiply()  # Method of an Abstract Class can be called without error because abstract method decorator is not used
print(issubclass(Calculator, Calculation))  # True
# throws an error because abstract class method is an abstract method


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


# By using the property decorator, you can use the dot notation to access the function without calling it explicitly.
# In other words, the method appears to become a regular attribute. Consider the example below:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def employee_price(self):
        return self.price * 0.9


vacuum = Product("Vacuum", 200)
vacuum.employee_price  # output: 180.0

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


####### MRO - order of inheritance ####
# When defining a subclass, there are different ways to call the __init__ method of a parent class.

class Base(object):
    def __init__(self):
        print("Base created")


# Method 1 :: Using Parent Reference Directly
class ChildA(Base):
    def __init__(self):
        Base.__init__(self)
        print("Child A initialized")


# Method 2:: Using Super with child class
class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()
        print("Child B initialized")


# Method 3:: Using the super method
class ChildC(Base):
    def __init__(self):
        super().__init__()  # this works sincxe python 3.xx
        print("Child C initialized")


cA = ChildA()
cB = ChildB()
cC = ChildC()
''' output:
Base created
Child A initialized
Base created
Child B initialized
Base created
Child C initialized
'''
print("=================")


class Base1:
    def __init__(self):
        super().__init__()
        print("Base 1 created")


class Base2:
    def __init__(self):
        super().__init__()
        print("Base 2 created")


class A1(Base1, Base2):
    def __init__(self):
        super().__init__()
        print("Child A1 Initialized")


class A2(Base2, Base1):
    def __init__(self):
        super().__init__()
        print("Child A2 Initialized")


a1 = A1()
''' output:
Base 2 created
Base 1 created
Child A1 Initialized
'''
print("\n\n")
a2 = A2()
''' output:
Base 1 created
Base 2 created
Child A2 Initialized
'''
# mro = Method Resolution Order(MRO) denotes the way a programming language resolves a method or attribute.
print(A2.mro())
''' output:
[<class '__main__.A2'>, <class '__main__.Base2'>, <class '__main__.Base1'>, <class 'object'>]
'''
#######################################


###### Create a constant value in class ######
print("============================================")
print("##### Create a constant value in class #####")


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def pi(self):
        return 3.14

    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * self.pi * self.radius


c = Circle(4)
print(f"c.pi is: {c.pi} that cannot be modified!")

####### Multiple Class constructors ######
print("=======================================")
print("##### Multiple Class constructors #####")


class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # We want to add another Ctor to obtain the date from a String in the format dd/mm/yyyy
    @classmethod
    def fromString(obj, s):
        day = int(s[:2])
        month = int(s[3:5])
        year = int(s[6:])
        return obj(day, month, year)  # Return a new object


d1 = Date(12, 3, 1977)
d2 = Date.fromString("21/07/2020")
print(d1.day, d1.month, d1.year)  # output: 12 3 1977
print(d2.day, d2.month, d2.year)  # output: 21 7 2020

##### DESCRIPTORS ###########
print("===========================")
print("##### DESCRIPTORS #####")


class Car:
    def __init__(self):
        self.fuel_amount = 0

    @property
    def fuel_amount(self):
        return self._fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, amount):
        if amount < 0:
            raise ValueError("Tank can't be less than empty!")

        if amount > 60:
            raise ValueError("Tank can't take more than 60 l!")

        self._fuel_amount = amount


car = Car()
# car.fuel_amount = -10 will cause "ValueError: Tank can't be less than empty!"

"""
Descriptors provide a solution that helps us separating concerns within our class, 
so our code remains nice and SOLID. By using a descriptor instead of a property, our Car class gets as short as this:
"""


# Descriptor
class SixtyLitresCapacity:
    def __set__(self, car, amount):
        if amount < 0:
            raise ValueError("Tank can't be less than empty!")

        if amount > 60:
            raise ValueError("Tank can't take more than 60 l!")

        car._fuel_amount = amount

    def __get__(self, car, objtype=None):
        return car._fuel_amount


class Car:
    fuel_amount = SixtyLitresCapacity()

    def __init__(self):
        self.fuel_amount = 0


car1 = Car()


# car1.fuel_amount = 70  ## Error occur: "ValueError: Tank can't take more than 60 l!"

# Better after refactoring:
class IsBetween:
    def __init__(self,
                 min_value,
                 max_value,
                 below_exception=ValueError(),
                 above_exception=ValueError()):
        self.min_value = min_value
        self.max_value = max_value

        self.below_exception = below_exception
        self.above_exception = above_exception

    def __set_name__(self, owner, name):
        self.private_name = '_' + name
        self.public_name = name

    def __set__(self, obj, value):
        if value < self.min_value:
            raise self.below_exception

        if value > self.max_value:
            raise self.above_exception

        setattr(obj, self.private_name, value)

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)


class Car:
    fuel_amount = IsBetween(0, 60, ValueError(), ValueError())

    def __init__(self):
        self.fuel_amount = 0


car2 = Car()
# car2.fuel_amount = 70  ### Raise Error: "raise self.above_exception ValueError"


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


# What is a metaclass?
# A metaclass is a class that defines the behavior of the classes and their instances.
# A metaclass is a class whose instances are classes.

# How to create a class dynamically in python? using 'type' not metaclass
def mymethod(self):
    return self.x > 100


class_name = "MyClass"
base_classes = tuple()
params = {"x": 10, "check_greater": mymethod}
MyClass = type("MyClass", base_classes, params)  # 3 parts in init with type class - name,base_classes, attribs as dict
obj = MyClass()
print(obj.check_greater())  # output: False


# A metaclass lets us to customize the creation of our user-defined classes before they are actually created!
# In other words, it can add or remove attributes, methods or base classes to the actual class.
# Metaclass is nothing but a class that derives from class type .
#  Metaclass may override the methods__new__, __init__ or __call__ on class typeto provide customized behavior.

# Lets say, I want to create a custom type of string which has method that says whether
# the given string equals to zero. meaning "0000"
# iszero method is not part of str type

class StringFactory(type):
    def iszero(self):
        """Check if the given string is equals to one or more zeros"""
        try:
            return not sum([int(chr) for chr in self])  # when "0000" it returns True
        except:
            return False

    def __new__(cls, name, bases, dct):
        print("My class is not yet created")
        bases += (str,)  # add str class as base to the new class
        dct["iszero"] = StringFactory.iszero  # add our custom method to the new class
        class_ = type.__new__(cls, name, bases, dct)
        print("My class is created with custom method at run time")
        return class_


# define the metaclass
class MyCustomString(metaclass=StringFactory):
    pass


test_string = MyCustomString("abcd")
print(f"For 'abcd' it is: {test_string.iszero()} ")  # Outputs False
test_string = MyCustomString("0000")
print(f"For '0000' it is:{test_string.iszero()}")  # Outputs True


# Assume that, we have to create a singleton class which creates only 1 object in
# its lifetime irrespective of the number of times the class is instantiated.

# Let us see how we can use the __call__ method in a metaclass.
class MyMeta(type):
    _instances = {}  # maintain a dictionary _instances in our metaclass MyMeta which holds

    # the reference between each class and its object.

    def __call__(cls, *args, **kwargs):  # will be called each time a class is instantiated
        if cls not in MyMeta._instances:  # During first invocation, the class is not present in _instances dictionary
            MyMeta._instances[cls] = super().__call__(*args, **kwargs)  # We call the default __call__ method from type
            # get the object and update our dictionary.
        return MyMeta._instances[cls]  # For further class instantiations,the same obj from _instances dict is returned.


class Singleton(metaclass=MyMeta):
    pass


x = Singleton()
y = Singleton()
print(f"The example says x is y: {x is y}")  # Outputs True

###################################################

### Special Cases #########
## Careful with chained operations
print((False == False) in [False])  # makes sense False
print(False == (False in [False]))  # makes sense False
print(False == False in [False])  # It is True because all comparison operations in Python have the same priority when
# they’re chained together (i.e when you don’t use brackets) - so it becomes ((False == False) and (False in [False]))

for x in range(7):
    if x == 6:
        print(x)  # print 6
print(x)  # print 6 - scope of x still leave after out of function


def func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'


print(func())  # What will get printed? from_finally - because when try is returned also fianny is executed and it has
# twice return statements - the last is overwriting the first

###########################


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
"""
json.dumps() This function accepts Python’s basic data types and serializes them into strings;
json.loads() function, on the other hand, accepts a valid string and deserializes it into Python’s basic data types.
For example:
import json
params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}
params_str = json.dumps(params)
print('after json serialization')
print(f'type of params_str = {type(params_str)}, params_str = {params_str}')
original_params = json.loads(params_str)
print('after json deserialization')
print(f'type of original_params = {type(original_params)}, original_params = {original_params}')
########## Output ##########
after json serialization
type of params_str = <class 'str'>, params_str = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}
after json deserialization
type of original_params = <class 'dict'>, original_params = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}
"""

"""
Have you ever wondered why json.loads ends with a “s”? The reason is because that method is specifically 
for working on a string, and there is another related method for working on files: json.load.
json.loads is for deserialising a string containing JSON, 
while json.load (no "s") is for deserialising a file containing JSON.
The methods are very related. In fact, json.load is a wrapper around json.loads. 
It's a method provided out of the box by Python to simplify the task of reading JSON from file-like objects. 
For example, these result in the same outcome:
# bad
with open(‘some/path.json’, ‘r’) as f:
 content = json.loads(f.read())
# good
with open(‘some/path.json’, ‘r’) as f:
 content = json.load(f)

Similarly to json.loads, json.dumpsalso ends with an "s" because it's specifically for working on a string 
and there is another related method:json.dump
json.dumps is for JSON serialising an object to a string, while json.dump (no "s") is for JSON 
serialising an object to a file.
Again similar to the relationship between json.load and json.loads, json.dump is a wrapper around json.dumps. 
It's a method provided out of the box by Python to simplify the task of writing JSON to a file-like object.
For example, these result in the same outcome:
# bad
with open('some/path.json', 'w') as f:
    f.write(json.dumps({'foo': 'bar'}))
# good
with open('some/path.json', 'w') as f:
    json.dump({'foo': 'bar'}, f)
"""

'''
JMESPath
JMESPath is a JSON query language. 
JMESPath in Python allows you to obtain the data you need from a JSON document or dictionary easily. 
This library is available for Python, but also for many other programming languages, 
meaning that if you master the JMESPath query language, you can use it in many places.

Let’s start with some simple use-cases. We’ll fetch the first person from the array, 
and then get the first person’s age:

{
  "persons": [
    { "name": "erik", "age": 38 },
    { "name": "john", "age": 45 },
    { "name": "rob", "age": 14 }
  ]
}
jmespath.search(‘persons[0]’, persons)
# {‘name’: ‘erik’, ‘age’: 38}
jmespath.search(‘persons[0].age’, persons)
# 38

In the problem statement above, we wanted to extract all the age fields from the array of persons in the JSON document. This JMESPath expression will get the job done:

import jmespath
persons = {
    "persons": [
    { "name": "erik", "age": 38 },
    { "name": "john", "age": 45 },
    { "name": "rob", "age": 14 }
    ]
}
jmespath.search(‘persons[*].age’, persons)
# [38, 45, 14]
Suppose you want to filter the list, and only get the ages for people named ‘erik’. You can do so with a filter:

jmespath.search(“persons[?name==’erik’].age”, persons)
# [38]
Note that we’re now using double quotes because we need to quote the name inside the filter expression.

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
print("### Find Longest String in List ####")
# Method 1: Iterate through the list using a loop and keep track of the longest string
string_list = ["hello", "world", "let's", "learn", "some", "Python"]
longest = ""
for current_string in string_list:
    if len(current_string) > len(longest):
        longest = current_string
print(longest)  # Python

# Method 2: Iterate through the list using a functional approach
import functools

string_list = ["hello", "world", "let's", "learn", "some", "Python"]
longest = functools.reduce(lambda longest, current_string: current_string if len(current_string) >
                                                                             len(longest) else longest, string_list, "")
print(longest)  # Python

# Method 3: Using max function
string_list = ["hello", "world", "let's", "learn", "some", "Python"]
longest = max(string_list, key=len)
print(longest)  # Python



print("### Convert String to List of Characters ###")
# Method 1: Iterate through the string using a for loop
character_string = "character"
character_list = []
for character in character_string:
    character_list.append(character)
print(character_list)  # ["c", "h", "a", "r", "a", "c", "t", "e", "r"]

# Method 2: List Comprehension
character_string = "character"
character_list = [char for char in character_string]
print(character_list)  # ["c", "h", "a", "r", "a", "c", "t", "e", "r"]

print("### Convert Comma Separated String to List ###")
split_string = "Split me, please"
string_list = split_string.split()
print(string_list)  # ["Split", "me,", "please"]
string_list = split_string.split(",")
print(string_list)  # ["Split me", " please"]

print("### Check if String Contains Substring from List ###")
# Method 1: Simple Iteration
l = ['hello', 'world']
contains = "this string contains the word hello"
not_contains = "this string contains no relevant words"


def check_contains(string_list, larger_string):
    for w in string_list:
        if w in larger_string:
            return True
    return False


print(check_contains(l, contains))  # True
print(check_contains(l, not_contains))  # False

# Method 2: Set Intersections
l = ['hello', 'world']
contains = "this string contains the word hello"
not_contains = "this string contains no relevant words"


def check_contains(string_list, larger_string):
    return len(set(string_list).intersection(larger_string.split())) > 0


print(check_contains(l, contains))  # True
print(check_contains(l, not_contains))  # False

print("### Convert List of Characters to String ###")
character_list = ["c", "h", "a", "r", "a", "c", "t", "e", "r"]
result = "".join(character_list)
print(result)  # character

print("### Remove Item from List (and also Remove First and Last Item from List) ###")
'''
list.remove(x): Removes the first item from the list whose value is equal to x.
list.pop([i]): Remove the item in the list at the index denoted by i. 
If no value i is provided, the last value in the list is removed.
'''
number_list = [1, 4, 2, 6, 2, 5]
number_list.remove(2)
print(number_list)  # [1, 4, 6, 2, 5]
number_list.remove(2)
print(number_list)  # [1, 4, 6, 5]
number_list.remove(1)
print(number_list)  # [4, 6, 5]
# number_list.remove(2) # ValueError: list.remove(x): x not in list

number_list = [1, 4, 2, 6, 2, 5]
# Remove first item from list
number_list.pop(0)
print(number_list)  # [4, 2, 6, 2, 5]
# Remove last item from list
number_list.pop(len(number_list) - 1)
print(number_list)  # [4, 2, 6, 2]

print("### Remove Duplicates from List ###")
# Method 1: Iteration
number_list = [1, 1, 2, 6, 2, 5]
no_duplicates_list = []
for number in number_list:
    if number not in no_duplicates_list:
        no_duplicates_list.append(number)
print(no_duplicates_list)  # [1, 2, 6, 5]

# Method 2: Sets
number_list = [1, 1, 2, 6, 2, 5]

no_duplicates_list = list(set(number_list))
print(no_duplicates_list)  # [1, 2, 6, 5]

print("### Check if List is Empty ###")
empty_list = []
non_empty_list = [1, 2, 3]


def check_empty(l):
    if list:
        print("List is empty" if len(l) == 0 else "List not empty")


check_empty(empty_list)  # List is empty
check_empty(non_empty_list)  # List is not empty

print("### Reverse Order of List ###")
# Method 1: Use the list.reverse() Function
number_list = [1, 2, 3, 4, 5]
number_list.reverse()
print(number_list)  # [5, 4, 3, 2, 1]

# Method 2: Use List Slicing:
number_list = [1, 2, 3, 4, 5]
reversed_list = number_list[::-1]
print(reversed_list)  # [5, 4, 3, 2, 1]
print("########################")
print("########################")
##################################################
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')
# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w') ## for writing logs to file
name = 'example'  # example to enter param to the log line
# List of levels for logging by their order:
logging.debug('This is a debug message')
logging.info(f'The param \'{name}\' shows an info message')
logging.warning('This is a warning message')  # this is the default
logging.error('This is an error message')
logging.critical('This is a critical message')
print("########################")
## example of using exception info to logging ##
# try:
#   c = a / 0
# except Exception as e:
#   logging.error("Exception Occurred", exc_info=True)  ## At default it is True

'''
Handler helps you to configure your own logger and send logs to multiple places after being generated. 
handlers can send the logs messages to a specified destination, to your console, to a file, 
or send over an HTTP connection. 
A logger can have multiple handlers. Like loggers, they also have severity levels that are useful when 
you want to log messages to different places.
Suppose You have an application and You want to take logs of the application. 
You want to save logs higher than the WARNING severity level to a log file and Higher than INFO on the console. 
With the help of handlers, you can do that-
'''

# custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.WARNING)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Each of this messages appears in condole and saved in file.log file
logger.warning('This is a warning')
logger.error('This is an error')
logger.critical('This is an error')

'''
You saw the above codes they look so messy because of all the formatting we did. 
To avoid this we can add all the formatting to a new file and then use that formatting in the different logs files. 
We can load that config file using fileconfig() The file extension should be .conf :
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=

Now to use it in execution:
code:

import logging
import logging.config

## Loads The Config File
logging.config.fileConfig('logging.conf')

# create a logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format in the logging.conf file
logger = logging.getLogger('simpleExample')

## Log Messages
logger.debug('debug message')
logger.info('info message') 
'''

'''
When You are working with a large application and you have so many events to log and you only need to keep track of 
the most recent events then you should use a rotating file handler. 
It helps you to set a byte limit for your file and if the limit reaches then all the previous logs replaced by new logs.
You can even create multiple backups of the file.

code:
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for i in range(10000):
    logger.info(i)
'''
# EXAMPLES
print("========================================================")
print("================### EXAMPLES###=========================")
''''
# 6 ways to find the largest number in the list
print("##### 6 ways to find largest nmber in list: #####")
numbers_lst = [1, 2, 3, 4, 50, 6, 3, 2, 3, 8]
# 1- Fast approach using built in max function
print("Using Max Built-in function: ", max(numbers_lst))
# 2- Manual Approach iterating all the elements of the list
max_num = numbers_lst[0]
for n in numbers_lst:
    max_num = n if n >= max_num else max_num
print("Manual Iteration: ", max_num)
# 3- Using comprehensions, in this case for the list
max_num = numbers_lst[0]
[max_num := n for n in numbers_lst if n >= max_num]
print("List Comprehension: ", max_num)
# 4- Sort the list in ascending order and print the last element in the list.
numbers_lst.sort()
# printing the last element, which is in this case the largest one
print("Using the sort list method:", numbers_lst[-1])
# 5 - Using the built in sorted function and getting
# the last list element afterwards
sorted_lst = sorted(numbers_lst, reverse=True)
max_num = sorted_lst[0]
print("Sorted List: ", max_num)
# 6 - Using the built-in reversed function to reverse
# the list, convert it to a list and print first item
print(list(reversed(numbers_lst))[0])
# Another nice shortcut for this approach should be this:
print(numbers_lst[::-1][0])
'''
# one liner lambda function example
'''
Write lambda function that completes three operations:
1) remove the last "+"
2) remove ',' from the string and
3) convert string into integer

inp = '1,234+'
lam = lambda x: int(x[:-1].replace(",", ""))
print(lam(inp)) #output: 1234
'''

# Combine Nested Lists into One List
'''
main_list = [[0, 1, 2], [11, 12, 13], [52, 53, 54]]

result = [item for sublist in main_list for item in sublist]
print(result)

# output: [0, 1, 2, 11, 12, 13, 52, 53, 54]
'''

# Compare 2 Unordered lists
''''
from collections import Counter
one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]
Counter(one) == Counter(two)
# True
sorted(one) == sorted(two)
# True
'''
# Difference between two lists
''''
list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']
set1 = set(list1)
set2 = set(list2)
list3 = list(set1.symmetric_difference(set2))
# {'Smith', 'Emma'}
# Or
set1-set2
# {'Smith', 'Emma'}
'''

# Merge two dictionaries
''''
name = dict(first_name='Anand', last_name='Tripathi)
details = dict(age=28, sex='Male')
person = {**name, **details}
'''

# Converting lists into a dictionary
''''
user = [“Peter”, “John”, “Sam”]
age = [23,19,34]
dictionary = dict(zip(user, age))
print(dictionary)
'''

'''
Duck Typing
To begin with let’s recall the definition of the duck test:
If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.
'''


class Duck:
    def clean(self):
        print("Quack I'm clean")

    def feed(self):
        print("Quack I'm full")


class Owl:
    def clean(self):
        print("Woo I'm clean")

    def feed(self):
        print("Woo I'm full")


'''
Our zookeper, Arnold, takes care of all our animals at the zoo; he feeds them and cleans them daily.
'''


class Zookeeper:
    def __init__(self, animals):
        self.animals = animals

    def work(self):
        for animal in self.animals:
            animal.clean()
            animal.feed()


our_animals = [Duck(), Owl()]
arnold = Zookeeper(our_animals)
arnold.work()
# output:
# Quack I'm clean
# Quack I'm full
# Woo I'm clean
# Woo I'm full

'''
That’s the principle of duck typing. It’s kinda similar to polymorphism in statically typed languages like Java, 
except that it’s easier, more flexible and doesn’t require the creation of an interface beforehand.
The problem is that you only see it when executing the code.
'''

'''
Mixins
Our zookeeper Arnold turned to be a sadistic person. From time to time, Arnold tortures the animals. 
To create a realistic Arnold, we have to give him a method to torture the animals with. 
We already have the Zookeeper class, which applies to most zookepers, we just want to add the sadistic .play() method 
to it for sadistic zookeepers only. To solve this problem, we’ll resort to using mixins. 
Mixins are classes that don’t stand on their own, but add functionality to other classes.
Let’s create our Sadistic mixin, and make a SadisticZookeeper class to help us create Arnold:
'''


class SadisticMixin:
    def play(self):
        for animal in self.animals:
            animal.torture()


class SadisticZookeeper(Zookeeper, SadisticMixin):
    pass


'''
But now our animals should be torturable for Arnold to be able to play with them. 
We’ll create another mixin for our animals: TorturableMixin and create our torturable animals and our sadistic arnold.
'''


class TorturableMixin:
    def torture(self):
        print("AAAAAAAHHHHHHHH")


# A TorturableDuck is a Duck that has the .torture() method
class TorturableDuck(Duck, TorturableMixin):
    pass


# A TorturableOwl is an Owl that has the .torture() method
class TorturableOwl(Owl, TorturableMixin):
    pass


our_animals = [TorturableDuck(), TorturableOwl()]
arnold = SadisticZookeeper(our_animals)

arnold.play()
# output:
# AAAAAAAHHHHHHHH
# AAAAAAAHHHHHHHH

'''
Monkey patching
Monkey patching, like duck typing, is yet another simple technique with a fancy (?) name. 
Monkey patching is the technique of altering the behaviour of a class or a function during runtime.
For example, as a conscious python coder who knows monkey patching, I
’m able to incapacitate arnold and prevent him from torturing the animals, 
even though arnold was created as a SadisticZookeeper in the first place. I just have to do:
'''


def anti_torture():
    print("NO MORE TORTURING, JACKASS!! Play Tetris instead.")


arnold.play = anti_torture

arnold.play()
# output:
# NO MORE TORTURING, JACKASS!! Play Tetris instead.

##################################################
### BREAK out of nested loops ###
print("### BREAK out of nested loops ###")

'''
when we need to break out of nested loops as follows:
for a in list_a:
    for b in list_b:
        if condition(a,b):
            break
The break keyword can only help us break out of the inner-most loop. 
Can we directly break out of the two nested loops at once? 
Are there some built-in keywords or tricks for this in Python?
Unfortunately, there is no built-in support for this operation.

We see 5 ways to avoid the problem
'''
# Add a flag variable
break_out_flag = False
for i in range(5):
    for j in range(5):
        if j == 2 and i == 0:
            break_out_flag = True
            break
    if break_out_flag:
        break

# raise an exception
try:
    for i in range(5):
        for j in range(5):
            if j == 2 and i == 0:
                raise StopIteration
except StopIteration:
    pass

# check the same condition again
for i in range(5):
    for j in range(5):
        if j == 2 and i == 0:
            break
    if j == 2 and i == 0:
        break

# use the for-else syntax
for i in range(5):
    for j in range(5):
        if j == 2 and i == 0:
            break
    else:  # only execute when it's no break in the inner loop
        continue
    break


# make it as a function
def check_sth():
    for i in range(5):
        for j in range(5):
            if j == 2 and i == 0:
                return


check_sth()  # Run the function when needed

# Avoid nested loops
import itertools

for i, j in itertools.product(range(5), range(5)):
    if j == 2 and i == 0:
        break
##################################################
"""
Generating Password
===================
import secrets
import string
import random

try:
    password_length = int(input("Please enter length of the password: "))
    if password_length >= 8:
        base_chars = list()
        #Select 1 lowercase letter
        lower = secrets.choice(string.ascii_lowercase)
        #Select 1 uppercase letter
        upper = secrets.choice(string.ascii_uppercase)
        #Select 1 digit
        digit = secrets.choice(string.digits)
        #Select 1 special char
        special = secrets.choice(string.punctuation)
        #Add all the selected chars into the list for later use
        base_chars.append(lower)
        base_chars.append(upper)
        base_chars.append(digit)
        base_chars.append(special)
        #Use combination with lower,upper,special chars and digits
        password_combination = string.ascii_letters + string.digits + string.punctuation
        #Create remaining chars from the password combination in addition to the previously create 4 chars
        remainder_chars = [secrets.choice(password_combination) for _ in range(password_length - 4)]
        #Add all the chars to the list
        remainder_chars.extend(base_chars)
        #For extra layer of security the list values are shuffled
        random.shuffle(remainder_chars)
        #Create password with the values
        password = "".join(remainder_chars)
        print(password)

except Exception as e:
    print(e.args)
"""

####################################

####### Async ######
print("~~~~~ Async ~~~~")
# Asynchronous is a general programming technique that is intended to improve the performance of your project
# by delegating some computationally heavy or lengthy process to a different process or thread.
# For instance, when you make a web API request, you can implement asynchronous coding to fire the request
# in a different thread, and you can still work on your current thread, when the API responds,
# you can use the response whenever it becomes available without the need of waiting for possibly extended time.
# The above is a very general discussion of asynchronous programming.
# In Python, we can implement asynchronous programming by taking advantage of the asyncio module.
# Specifically, we can create asynchronous functions.

import time


def login_user():
    time.sleep(2)


def load_posts():
    time.sleep(3)


def launch_app():
    print("Not async operations - take more time:")
    a1 = time.time()
    print("Open App:", time.asctime())
    login_user()
    load_posts()
    b1 = time.time()
    print("App Page Loaded:", time.asctime())
    print(f"There are {(int)(b1 - a1)} seconds gap")


launch_app()

import asyncio
import time


async def login_user_async():
    await asyncio.sleep(2)


async def load_posts_async():
    await asyncio.sleep(3)


async def launch_app_async():
    print("Async operation can parallel thing ,takes less time:")
    print("Open App:", time.asctime())
    a1 = time.time()
    await asyncio.gather(
        login_user_async(),
        load_posts_async()
    )
    print("App Page Loaded:", time.asctime())
    b1 = time.time()
    print(f"There are {(int)(b1 - a1)} seconds gap")


asyncio.run(launch_app_async())

####################################################
### DEPENDENCY INJECTOR ############################
print("~~~~~ Dependency Injection ~~~~")


## Hard coupling without dependency injection
class MessageFormatter:
    def success(self, message):
        return f"👍 {message}"


class MessageWriter:
    def __init__(self):
        self.message_formatter = MessageFormatter()  ## Hard coupling

    def write(self, message):
        print(self.message_formatter.success(message))


message_writer = MessageWriter()
message_writer.write("Hello World!")


# With dependency injection
class MessageFormatter:
    def success(self, message):
        return f"👍 {message}"


class MessageWriter:
    def __init__(self, message_formatter):  # dependency injection
        self.message_formatter = message_formatter

    def write(self, message):
        print(self.message_formatter.success(message))


message_formatter = MessageFormatter()
message_writer = MessageWriter(message_formatter)
message_writer.write("Hello World!")

"""
Most Formal way is using 'dependency_injector' lib 
from dependency_injector import containers, providers

class MessageFormatter:
    def success(self, message):
        return f"👍 {message}"

class Container(containers.DeclarativeContainer):
   message_formatter = providers.Factory(MessageFormatter)


class MessageWriter:
    def __init__(self, message_formatter=None):
        if message_formatter:
            self.message_formatter = message_formatter
        else:
            self.message_formatter = Container.message_formatter()

    def write(self, message):
        print(self.message_formatter.success(message))


message_formatter = MessageFormatter()
message_writer = MessageWriter(message_formatter)
message_writer.write("Hello World!")
"""

####################################################
####### Schedule tasks with Threading ######
print("~~~~~ Schedule tasks with Threads ~~~~")

import os
import time
import threading


def task():
    task.counter += 1
    print("Job Completed!")


task.counter = 0  # function attribute


def schedule():
    while 1:
        task()
        if task.counter > 3:
            sys.exit(0)
        time.sleep(1)


# makes our logic non blocking
thread = threading.Thread(target=schedule)
thread.start()

#### REDUCE COMPLEXITY WITH EXAMPLE OF LIST OF ACTIONS ####
# Each request contains an action and a customer name.
# Actions consist of creating a new customer,
# activating a customer, suspending a customer and deleting a customer.
# There are 4 types, and each type is handled differently.

from typing import Any, Dict


def _handle_create_request(customer_name: str) -> None:
    # do something related to create
    return


def _handle_activate_request(customer_name: str) -> None:
    # do something related to activate
    return


def _handle_suspend_suspend(customer_name: str) -> None:
    # do something related to suspend
    return


def _handle_delete_request(customer_name: str) -> None:
    # do something related to delete
    return


ACTION_MAPPING = {
    "create": _handle_create_request,
    "activate": _handle_activate_request,
    "suspend": _handle_suspend_suspend,
    "delete": _handle_delete_request,
}


def function_handler(request: Dict[str, Any]) -> None:
    action = request.get("action")
    customer_name = request.get("customer")
    # validate input
    _handle_request(action, customer_name)


def _handle_request(action: str, customer_name: str) -> None:
    action_handler = ACTION_MAPPING.get(action)
    # handle action
    action_handler(customer_name)


''''
Read this article: https://formus14.medium.com/how-to-implement-a-timeout-functionality-in-python-d578d7ad985a
'''
''''  Working with one Thread
import threading
import time


class Demo:
    def __init__(self):
        self._KillTask = False

    def OnTimeout(self):
        self._KillTask = True
        print("Timeout!")

    def Counter(self, timeout):
        print("Counter() starts!")
        totalSleepTime = 0
        while (self._KillTask is False):
            totalSleepTime = totalSleepTime + 1
            time.sleep(1)
            if totalSleepTime == timeout:
                self.OnTimeout()

    def Function(self):
        while self._KillTask is False:
            # do any logic here
            print("Function is running till it timeout..")
            time.sleep(0.5)  # just a demo delay for the printed log on the terminal
        print("Function() timed out!")
        self._KillTask = True


if __name__ == '__main__':
    ## Main starts here
    print("Demo for Timeout - by Omar")
    Obj = Demo()

    ## Start thread2
    thread2 = threading.Thread(target=Obj.Counter, args=(5,))
    try:
        thread2.start()
    except Exception:
        print("Error Starting the Thread")

    ## Proceed with the logic of thread 1 -(Main thread)
    Obj.Function()
'''
''''  Working with multiple Threads
import threading
import time


class Demo:
    def __init__(self):
        self.mutex = threading.Lock()
        self.SetKillTask(False)

    def OnTimeout(self):
        self.SetKillTask(True)
        print("Timeout!")

    def Counter(self, timeout):
        print("Counter() starts!")
        totalSleepTime = 0
        while (self._KillTask is False):
            totalSleepTime = totalSleepTime + 1
            time.sleep(1)
            if totalSleepTime == timeout:
                self.OnTimeout()

    def Function(self):
        while self._KillTask is False:
            # do any logic here
            print("Function is running till it timeout..")
            time.sleep(0.5)  # just a demo delay for the printed log on the terminal
        print("Function() timed out!")
        self.SetKillTask(True)

    def SetKillTask(self, value):
        self.mutex.acquire()
        self._KillTask = value
        self.mutex.release()


if __name__ == '__main__':
    ## Main starts here
    print("Demo for Timeout - by Omar")
    Obj = Demo()

    ## Start thread2
    thread2 = threading.Thread(target=Obj.Counter, args=(5,))
    try:
        thread2.start()
    except Exception:
        print("Error Starting the Thread")

    ## Proceed with the logic of thread 1 -(Main thread)
    Obj.Function()
'''
''''
import threading
import time


class Demo:
    def __init__(self):
        self._KillTask = False

    def Function(self, timeout):
        timeout = time.time() + timeout
        while (time.time() < timeout):
            # do any logic here
            print("Function is running till it timeout..")
            time.sleep(0.5)  # just a demo delay for the printed log on the terminal
        print("Function() timed out!")

    def OtherFunction(self):
        for _ in range(15):
            print("Other Function is running now ..")
            time.sleep(0.5)  # just a demo delay for the printed log on the terminal


if __name__ == '__main__':
    ## Main starts here
    print("Demo for Timeout - by Omar")
    Obj = Demo()

    ## Start thread2
    timeout = 5
    thread2 = threading.Thread(target=Obj.Function, args=[timeout])
    try:
        thread2.start()
    except Exception:
        print("Error Starting the Thread")

    ## Proceed with the logic of thread 1 -(Main thread)
    Obj.OtherFunction()
'''

###########################################################


'''
__slots__ is an attribute you can add to a Python class when defining it. 
You define slots with the possible attributes that an instance of an object can possess. 
Here’s how you use __slots__:
class WithSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x, self.y = x, y
        
For instances of this class, you can use self.x and self.y in the same ways as a normal class instance. 
However, one key difference between this and instancing from a normal class is that you cannot add 
or remove attributes from this class’ instances. Say the instance was called w: 
you couldn’t write w.z = 2 without causing an error.
The biggest higher-level reasons to use __slots__ are 1) faster attribute getting and setting due to data 
structure optimization and 2) reduced memory usage for class instances. 
Some reasons you wouldn’t want to use it is if your class has attributes that change during 
run-time (dynamic attributes) or if there’s a complicated object inheritance tree.        
'''

# long lines are BAD - Use parentheses, not backslashes, to fix longer lines:
'''
# BAD
long_variable_name = even_longer_function_name(pretty_long_argument, another_argument) + another_function() - final_function() / 3

# BETTER
long_variable_name = even_longer_function_name(pretty_long_argument, another_argument) \
                        + another_function() - final_function() / 3
                        
# BEST!
long_variable_name = (
    even_longer_function_name(pretty_long_argument, another_argument)
    + another_function()
    - final_function() / 3
)
'''

# Python pros — You can actually write your own context managers.
# These are useful for code that has a setup and an ending action. The general structure looks like this:
'''
from functools import contextmanager  # standard library


@contextmanager
def my_context_manager():
    # setup code: runs just before entering the "with" statement
    # ...
    try:
        yield var  # or just "yield" if you don't need to pass a variable on
    finally:
        # ending code: runs right after exiting the "with" statement
        # will run even if code inside the "with" statement raised an exception!
        # ...
        
Say you wanted to have a context manager that printed to let you know when your processes start and end:

from functools import contextmanager
from datetime import datetime

@contextmanager
def log_start_and_end():
    print(f'Start time: {datetime.now()}')
    try:
        yield
    finally:
        print(f'End time: {datetime.now()}')

### That’s it! Now you can use it like this:
with log_start_and_end():
    # ...                
'''
### Positional-only arguments
'''
Often, the names of a function’s arguments are irrelevant. 
In this case, you want those arguments to always be passed positionally:
Positionally: is_capitalized("world")
Not positionally: is_capitalized(string="world")
In Python 3.8, you can force arguments to your functions to be positional! 
This can make code cleaner and more readable.
To achieve this functionality, use a / as an argument:

def is_capitalized(string, /):
    return string[0].isupper()
    
# All arguments that precede the / will need to be passed positionally:
is_capitalized("October")
# True

is_capitalized(string="October")
# TypeError: is_capitalized() got some positional-only arguments passed as [etc.]

'''

'''
############################
#######  DATETIME  #########
############################
from datetime import date, time, datetime, timedelta
from dateutil.tz import UTC, tzlocal, gettz, resolve_imaginary

# Constructors
d  = date(year, month, day)
t  = time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)
dt = datetime(year, month, day, hour=0, minute=0, second=0, ...)
td = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
                 
# Now
d/dtn  = d/dt.today()                     # Current local date or naive datetime.
dtn    = dt.utcnow()                      # Naive datetime from current UTC time.
dta    = dt.now(tzinfo)                   # Aware datetime from current tz time.

# To extract time
dtn.time()
dta.time()
dta.timetz()

# Encode
d/t/dt = d/t/dt.fromisoformat('iso')     # Object from ISO string. Raises ValueError.
dt     = dt.strptime(str, 'format')      # Datetime from str, according to format.
d/dtn  = d/dt.fromordinal(int)           # d/dtn from days since Christ, at midnight.
dtn    = dt.fromtimestamp(real)          # Local time dtn from seconds since the Epoch.
dta    = dt.fromtimestamp(real, tz.)     # Aware datetime from seconds since the Epoch.

# Decode
str    = d/t/dt.isoformat(sep='T')       # Also timespec='auto/hours/minutes/seconds'.
str    = d/t/dt.strftime('format')       # Custom string representation.
int    = d/dt.toordinal()                # Days since Christ, ignoring time and tz.
float  = dtn.timestamp()                 # Seconds since the Epoch, from dtn in local tz.
float  = dta.timestamp()                 # Seconds since the Epoch, from dta.

# Format
from datetime import datetime
dt = datetime.strptime('2015-05-14 23:39:00.00 +0200', '%Y-%m-%d %H:%M:%S.%f %z')
dt.strftime("%A, %dth of %B '%y, %I:%M%p %Z")
"Friday, 14 of July '89, 09:45PM UTC+03:00"

# Arithmatics
d/dt   = d/dt   ± td                     # Returned datetime can fall into missing hour.
td     = d/dtn  - d/dtn                  # Returns the difference, ignoring time jumps.
td     = dta    - dta                    # Ignores time jumps if they share tzinfo object.
td     = dt_UTC - dt_UTC                 # Convert dts to UTC to get the actual delta.
'''

#############
# 1. What is the difference between .py and .pyc files?
# The .py file contains the source code of the program. On the other hand .pyc files contain the compiled
# byte of your program.
# Python Compiles the .py file and saved it into a .pyc file. Then It is executed by the Python Virtual Machine.
# Before executing the main source code python looks for a compiled version of it(.pyc file)
# if python finds one then it will execute it with the help of a virtual machine.
# if not then it will look for a .py file compiles it and then execute the .py file.
# Basically, .pyc files save the compilation time, By Executing the already compiled code again.

# 2. What is Abstraction? How To Achieve Abstraction in Python?
# Abstraction is used to hide the internal functionality of a function from the users.
# They Can Interact with the function and generate results but don’t know how the results are generated.
# In Simple Words, Abstraction is used to hide the irrelevant data from the user
# to reduce the complexity of the program. In Python With The Help of the ABC Module, We can achieve abstraction.
# An Abstract Class also works as a blueprint for other classes because you can’t
# create objects for an abstract class so the only way to access elements is to use inheritance.
'''
from abs import ABC, abstractmethod

class Parent(ABC):
  @abstracmethod
  def show(self):
    pass
  
class child(Parent):
  def show(self):
    print("Child Class")
    
obj = child()
obj.show()
'''

# 3. How Shallow Copy is Different From Deep Copy Explain With an Example?
# Shallow Copy Stores reference of the object in a new memory location.
# Changes Made to the new location also reflect on the previous location. It is faster than a Deep copy.
# Deep Copy Stores the value of the object in a new location.
# Any changes made to the new location don’t reflect on the previous location.
'''
## Example of Shallow Copy
data = [1, 2, 3, 4, 5]
updated_data = data
updated_data.append(6)
print(updated_data)
print(data)
--------------------------------
[1,2,3,4,5,6]
[1,2,3,4,5,6]
## Example of Deep Copy
import copy
data = [1,2,3,4,5]
updated_data = copy.deepcopy(data)
updated_data.append(6)
print(updated_data)
print(data)
------------------------------
[1,2,3,4,5,6]
[1,2,3,4,5]
'''

# 4. What do you understand with pickling and unpicking?
# Pickling is the process where a python object hierarchy is converted into a byte stream.
# And Unpickling is the inverse operation, where a byte stream is converted back into an object hierarchy.
'''
## Pickling
import pickle
data =  {'Names': ["Karl","Robin","Lary"],
         'Id': ('G770531','G770532','G770533'),
         'Salary':[55600,88900,76000]}
output = open('data.pkl', 'wb')
pickle.dump(data, output)
output.close()
## Unpickling
import pickle
stream = open('data.pkl', 'rb')
data = pickle.load(stream)
print(data)
stream.close()
---------------------------------------
{'Names': ['Karl', 'Robin', 'Lary'], 'Id': ('G770531', 'G770532', 'G770533'), 'Salary': [55600, 88900, 76000]}
'''

# 5. What are *args and **kwargs in python?
# Both *args and **kwargs allows passing the variable number of arguments to a function.
# These are used when you are not sure about the number of arguments to be passed in a function.
# *args allows you to pass a variable number of arguments to a function.
# It is defined with an asterisk * followed by a variable.
''''
def addNumbers(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    print("Sum: ",sum)
addNumbers(3,5)
addNumbers(5,6,7)
------------------------------------
Sum: 8
Sum: 18
# In the Above Code, *numbers allows to pass variable number of arguments to the function addNumbers.
'''
# **kwargs allows you to pass a variable number of keyword arguments to a function.
# It is defined with a double asterisk followed by a variable.
'''
def addNumbers(*args,**data):
    sum = 0
    for key,value in data.items():
        sum = sum+value
    print("Sum: ",sum)
    
addNumbers(a=5, b=6)
addNumbers(a=5, b=8, c=10)
------------------------------------
Sum: 11
Sum: 23
'''

'''
How does GIL work and how can it be avoided?
GIL stands for the Global Interpreter Lock, a concurrency mechanism implemented by Python. 
It is deeply engrained into the Python code and can’t be removed at the moment. 
GIL introduces a significant downside in that it does not permit threads to be truly concurrent. 
The interpreter is locked, and even though you appear to be working with threads, 
there are no threads executing at the same time, degrading performance.
'''
"""
SOLID stands for five software development principles that are instrumental in writing cleaner, more readable code. 
There are five principles that make your code easier to read and understand and help you write better programs:
S — Single Responsibility Principle
O — Open/Closed Principle
L — Liskov Substitution Principle
I — Interface Segregation Principle
D — Dependency Inversion Principle.

Single Responsibility Principle (SRP)
Each Python module should have a single responsibility that is clear to users at every point. 
The boundaries around responsibilities can be fuzzy, so one way to apply SRP is to ask yourself 
if you’d be OK with your application breaking if part of your module were removed.
❌Bad way:
class Animal:
    def __init__(self, name: str):
        self.name = name
    def get_name(self) -> str:
        pass
    def save(self, animal: Animal):
        pass
✅Good way:
class Animal:
    def __init__(self, name: str):
            self.name = name
    def get_name(self):
        pass  
class AnimalDB:
    def get_animal(self) -> Animal:
        pass
    def save(self, animal: Animal):
        pass

Open/Closed Principle (OCP)
Unlike OOD which is concerned with objects that know how to do certain things (open), 
OCP is concerned with interfaces that can be extended or modified without changing how they work (closed).
❌Bad way:
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    def give_discount(self):
            if self.customer == 'fav':
                return self.price * 0.2
            if self.customer == 'vip':
                return self.price * 0.4
✅Good way:
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    def get_discount(self):
            return self.price * 0.2
class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
        
        
Liskov Substitution Principle (LSP)
The Liskov Substitution Principle is used when writing code. 
It is used to make sure that objects are usable in place of their parent class. 
In Python, LSP allows subclasses to extend their parent class functionality while still being usable 
by an object’s original interface (i.e., in place of their parent).
❌Bad way:
def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))
animal_leg_count(animals)
✅Good way:
def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
animal_leg_count(animals)

In other words, objects should act as a proper subset of those in their superclass or category.

Interface Segregation Principle (ISP)
If a class is dependent on another class, it’s always advisable to use IS. 
If a class depends only on one interface not multiple interfaces then that can be treated as an example of ISP.
❌Bad way:
class IShape:
    def draw_square(self):
        raise NotImplementedError
    def draw_rectangle(self):
        raise NotImplementedError
    def draw_circle(self):
        raise NotImplementedError
✅Good way:
class IShape:
    def draw(self):
        raise NotImplementedError
class Circle(IShape):
    def draw(self):
        pass
class Square(IShape):
    def draw(self):
        pass
class Rectangle(IShape):
    def draw(self):
        pass
        
Dependency Inversion Principle (DIP)
The Dependency Inversion Principle: It says that high-level modules should not depend on low-level modules. 
Both should depend on abstractions.
❌Bad way:
class XMLHttpService(XMLHttpRequestService):
    pass
class Http:
    def __init__(self, xml_http_service: XMLHttpService):             
        self.xml_http_service = xml_http_service
    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')
    def post(self, url, options: dict):        
        self.xml_http_service.request(url, 'POST')
✅Good way:
class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection
    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')
    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')

Abstractions should not depend upon details. Details should depend upon abstractions.                
"""

########################################
########################################
#### Choosing Function names rules..####
########################################
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
