"""
Python Quick Reference - edited in GitHub
"""
### CHECK PYTHON VERSION ### do verifications for customer version awareness
import sys
if sys.version_info < (3,5):
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

#define an alias to specific func from module
from math import sqrt as sq
print(f"sqrt(81) is {sq(81)}")

# PLACEHOLDER - a placeholder in a function that you haven’t implemented
def func():
    pass

def func1():
    ...

# VARIABLES
print("===============")
print("VARIABLES")

# all variables/functions/class instances etc - are objects!!!
# Variables are pointer to address in memory - they hold the address in memory not actually the value
# addresses of objects can be revealed by function id()
# Each assignment to a var changes the reference even if you do my_var = ny_var+5 it means my_var is now pointing to new
# address in memory
a = 10
print(hex(id(a))) #HEX address where a points to: 0x7ffc9daab470
b = a
print(hex(id(b))) #HEX address where a points to: 0x7ffc9daab470 the same address!!!
a = 5 # Now the a variable is pointing to other place
print(hex(id(a))) #output: 0x7ffcaea1b3d0 meaning the assignment moved var a from pointing to place of 10
# to new place of 5
print(f"b is {b}") #output: b is 10 because the assignment still to 10 in memory
b = b + 5  #b is now 15 meaning value changed - it means b is now pointing to other place
print(hex(id(b))) #HEX address where a points to: 0x7ffcaea1b510 a different address.


### DATA TYPES ###
print("===============")
print("DATA TYPES")
# determine the type of an object
type(2)  # returns 'int'
type(2.0)  # returns 'float'
type('two')  # returns 'str'
type(True)  # returns 'bool'
type(None)  # returns 'NoneType'

#python is dynamic typed - var as pointer(reference) to address type is according to what is been pointed to
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

#Notice: t is tuple of list a and b it means it is immutable but a and b are mutable,
# you cannot add new element to t but you can change the element in a and b inside the t
a = [1,2]
b = [5,6]
t = (a,b)
#t = (a,b,1) #Error - t tuple is immutable
t[0].append(3)
t[1].append(7)
print(f"t now is : {t}") #t now is : ([1, 2, 3], [5, 6, 7])

def func(inp):
    inp = inp + ' World!'
    print(f"inside func my_val is: {inp}") #inp = "Hello World!
    return inp

my_val = "Hello"
func(my_val)
print(f"Outside val of my_val is {my_val}") #my_val is: Hello   --> because string is immutable!

c = 7
print(f"address of c is {hex(id(c))}") #output: 0x7ffcaea1b410
d = 7
print(f"address of d is {hex(id(d))}") #output: 0x7ffcaea1b410 the same address - python is clever to point
# to the same address because integer is immutable - it will not change! But if values are large like 500 address are
# different
# when trying to do modification to integer it is actually pointing to new address with other value
a = [1,2,3]
print(f"address of a is {hex(id(a))}") #output: 0x2484852fb88
b = [1,2,3]
print(f"address of b is {hex(id(b))}") #output: 0x2484852fbc8 meaning -
# python memory for mutable types uses different address.
c = b
print(f"address of c is {hex(id(c))}") #output: 0x2484852fbc8 meaning - in this case same address is shared
c.append(100) # will cause c to add 100 to list and also b to add 100
print(f"b val is: {b}") #output: b val is: [1, 2, 3, 100]

### F-STRING ###
print("===============")
print("F-STRING PRINTING")

import datetime
now = datetime.datetime.now()
val = 12.3
a = 300

print(f'{now:%Y-%m-%d %H:%M}') #output: 2021-02-10 12:17
print(f'{val:.2f}') #output: 12.30
print(f'{val:.5f}') #output: 12.30000
for x in range(1, 11):
    print(f'{x:02} {x*x:3} {x*x*x:4}') #first output: 01   1    1
# hexadecimal
print(f"{a:x}") #output: 12c
# octal
print(f"{a:o}") #output: 454
# scientific
print(f"{a:e}") #output: 3.000000e+02

# To ease read of large numbers:
val = 10000000000000000
print(f"{val:_}") #output: 10_000_000_000_000_000
print(f"{val:,}") #output: 10,000,000,000,000,000


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

# Use 'is' or 'is not' to compare variable addresses (by their id)
# Use '==' ór '!=' to compare variable values

a = [1,2,3]
b = [1,2,3]
print(f"a value is: {a} and id is: {hex(id(a))}")
print(f"b value is: {b} and id is: {hex(id(b))}")
print(f"a is b : {a is b}") #False - they do not have same id(address in memory)
print(f"a == b : {a == b}") #True - there is value is the same

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
numbers = ['0','1','2','3','4','5','6','7','8','9']
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
print(first_two) #output: [1, 2]

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
s.split(' ')  # returns ['I', 'like', 'you']
s.split()  # equivalent (since space is the default delimiter)
s2 = 'a, an, the'
s2.split(',')  # returns ['a', ' an', ' the']

# join a list of strings into one string using a delimiter
stooges = ['larry', 'curly', 'moe']
' '.join(stooges)  # returns 'larry curly moe'

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4  # returns 'The meaning of life is 42'

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

#print a character
print(str_samp[3])

#make list from the string
chars=list(str_samp) #output: l
print(type(chars)) #output: <class 'list'>
print(chars[3]) #output: l

# remove new line from strings in list
data = ['alpha\n','beta\n','gamma\n']
print(data) #output: ['alpha\n', 'beta\n', 'gamma\n']
data = [s.strip() for s in data]
print(data) #output:['alpha', 'beta', 'gamma']


### +++++ ####
# namedtuple is better when importing modules because inner attributes are seen in new context
from random import randint
from collections import namedtuple

Color = namedtuple('Color','red green blue')

def rand_colors():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    return Color(red,green,blue)

color = rand_colors()
print(f"color is:{color}")



### DICTIONARIES ###
## properties: unordered, iterable, mutable, can contain multiple data types
## made of key-value pairs
## keys must be unique, and can be strings, numbers, or tuples
## values can be any type
print("===============")
print("DICTIONARIES")

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

#simple iteration dictionary using 'in'
data = {
    'France':'Paris',
    'Germany':'Berlin',
    'Italy':'Rome'
}

for country in data:
    print(f'The capital of {country} is {data[country]}')

# A safer way of reading values from dictionary - using get instead of [key]
data = {'France':'Paris','Italy':'Rome'}

#capital  = data,get('Germany') #ERROR
capital  = data.get('Germany')
# but it retuns None
print(capital) #output: None

capital = data.get('Germany','??')
print(capital) #output: ??



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
def func(a,b=1,c=2):
    pass

func(100) #meaning a receives 100 and b is 1 and c is 2
# Named argument can enable to choose which val go to which param even if not in same order
func(c=10,a=3) # will give a=3,b=1,c10  --> b received 1 as default

# use 'pass' as a placeholder if you haven't written the function body
def stub():
    pass


# return two values from a single function
def min_max(nums):
    return min(nums), max(nums)


# return values can be assigned to a single variable as a tuple
nums = [1, 2, 3]
min_max_num = min_max(nums)  # min_max_num = (1, 3)

# return values can be assigned into multiple variables using tuple unpacking
min_num, max_num = min_max(nums)  # min_num = 1, max_num = 3


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

l = [1,2,3,4,5,6]
a,b = l[0],l[1:]

print(f"a is: {a}") # a is: 1
print(f"b is: {b}") # b is: [2, 3, 4, 5, 6]

# Using *
c,*d = l

print("-----------")
print(f"c is: {c}") # c is: 1
print(f"d is: {d}") # d is: [2, 3, 4, 5, 6]
print(*d) #output: 2 3 4 5 6
### Notice: *param inside of method will removes the list structure and give list of elements


l1 = [1,2,3,4,5,6]
a1,b1,*c1,d1 = l1

print(f"a1 is: {a1}") # a1 is: 1
print(f"b1 is: {b1}") # b1 is: 2
print(f"c1 is: {c1}") # c1 is: [3, 4, 5]
print(f"d1 is: {d1}") # d1 is: 6

a,*b,(c,*d) = [1,2,3,'python']
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
    return count,total/count

print(avg(2,2,4,4)) #output: (4,3.0)

### **KWARGS ###
### an operator we can pass to functions, gather remaining arguments as a dictionary ###
print("===============")
print("**KWARGS")

def func(**kargs):
    print(kargs)


func(a=1, b=2, c=3)  # output: {'a': 1, 'b': 2, 'c': 3}


def family_members(**people):
    for name, family_name in people.items():
        print(f"His name is {name} and family name is {family_name}")


family_members(ídan="Belfer", ron="Ram", noam="Belfer")
#His name is ídan and family name is Belfer
#His name is ron and family name is Ram
#His name is noam and family name is Belfer

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
def func(a: str='xyz', b: int=5) -> str:
    return a * b

func() #output: xyzxyzxyzxyzxyz
print(func("Dan", 4)) #output: DanDanDanDan

from typing import List
def func(l: List[int])->list[int]:
    return [e**2 for e in lst]

lst=[1,2,3,4]
print(func(lst))


### ANONYMOUS (LAMBDA) FUNCTIONS ###
## primarily used to temporarily define a function for use by another function - like inline functions
## This is a real function with anonymous name , structure: lambda [param list] : expression
## The expression returns function object when it is called, param list is optional can be empty
## Lambda expression MUST be assigned to variable OR passed as argument to function
print("===============")
print("LAMBDA FUNCTIONS")

my_func = lambda x:x**2
#my_func(3) ->9
my_func = lambda x,y:x+y
#my_func(3,5) ->8
my_func = lambda: 'hello'
print(my_func()) #output: hello

# define a function the "usual" way
def squared(x):
    return x ** 2

# define an identical function using lambda
squared = lambda x: x ** 2
#print(squared(5)) #output: 25

## lambda as argument to function
def apply_func(x,fn):
    return fn(x)

print(apply_func(3,lambda x:x**2)) #output: 9
print(apply_func(2,lambda x:x+2)) #output: 4

f=lambda x,y=10:x+y
print(f(1,2)) #output:3
print(f(1)) #output:11
f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(f(1, 'a', 'b', y=100, a=10, b=20))  # output: (1, ('a', 'b'), 100, {'a': 10, 'b': 20})

l = ['C','B','a','d']
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

### FUNCTION ATTRIBUTES ####
print("=================")
print("FUNCTION ATTRIBUTES")
import inspect
def my_func(a: "first",
            b: "optional" = 1,
            c = 2,
            *args: "args here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "extra kw ")->"do nothing":
    """This is a function for explanation"""
    i=10
    j=20

print(my_func.__doc__) #output: This is a function for explanations
print(my_func.__annotations__)
#output: {'a': 'first', 'b': 'optional', 'args': 'args here', 'kwargs': 'extra kw ', 'return': 'do nothing'}
my_func.short_description = "added attribute to the function"
## all attributes of function can be seen with dir(func) method
print(my_func.__name__) #output: my_func
print(my_func.__defaults__) #output: (1,2) --> match to b=1,c=2
print(my_func.__kwdefaults__) #output: {'kw2': 100, 'kw3': 200}
# function has attribute named: __code__ which is object that we can do dir(my_func.__code__)
print(my_func.__code__.co_name) #output: my_func
print(my_func.__code__.co_argcount)  # output: 3 for a,b,c - show only positional arguments
print(my_func.__code__.co_varnames)  # output: ('a', 'b', 'c', 'kw1', 'kw2', 'kw3', 'args', 'kwargs', 'i', 'j')
print( inspect.getdoc(my_func) ) # output: This is a function for explanation
# print(inspect.signature(my_func).parameters) # output will be all parameters
#for k,v in inspect.signature(my_func).parameters.items():
#    print(f"{k} : {v} ") #output: all the params with values


### FOR LOOPS AND WHILE LOOPS ###
print("===============")
print("FOR WHILE LOOPS")

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

# for/else loop
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
x=0
while x<5:
    print(x)
    x+=1
else:
    print('Done')



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
items = [item for row in matrix
         for item in row]  # [1, 2, 3, 4]

# set comprehension
fruits = ['apple', 'banana', 'cherry']
unique_lengths = {len(fruit) for fruit in fruits}  # {5, 6}

# dictionary comprehension
fruit_lengths = {fruit: len(fruit) for fruit in fruits}  # {'apple': 5, 'banana': 6, 'cherry': 6}
fruit_indices = {fruit: index for index, fruit in enumerate(fruits)}  # {'apple': 0, 'banana': 1, 'cherry': 2}

### MAP AND FILTER ALL AND ANY ###
print("===============")
print("MAP AND FILTER ALL AND ANY ")

# 'map' applies a function to every element of a sequence
# ...and returns an iterator
# function that accepts at least 2 args, a function and íterable
# iterable = something that can be iterated over(list,string,dictionary,set,tuple)
# runs lambda for each value in the iterable and returns
# a map object which can be converted into other data structure

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
print(list(filter(lambda y:y<25, map(lambda x:x**2,l ) )  )) #output: [0, 1, 4, 9, 16]
# easy to use list comprehension
print("list comprehension:")
print([x**2 for x in range(10) if x**2 < 25]) #output: [0, 1, 4, 9, 16]

### ZIP ###
print("===============")
print("ZIP")

# make an iterator that aggregates elements from each of the iterables, only works with iterators
# Returns an iterator of tuples ,where the i-th tuple contains the i-th element
# from each of the argument sequences or iterables
# The iterator stops when the shortest input iterable is exhausted
num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
print(list(zip(num1,num2))) #output: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(dict(zip(num1,num2))) #output: {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}
l1 = [1,2,3]
l2 = [a,b,c,d]
print(list(zip(l1,l2)))

l1 = [1,2,3]
l2 = ['a','b','c','d']
print(list(zip(l1, l2))) #output: [(1, 'a'), (2, 'b'), (3, 'c')]

l1 = [1,2,3]
l2 = [10,20,30]
print([x+y for x,y in zip(l1,l2)]) #output: [11,22,33]

print("Example of transpose of 2D data:")
m = [(1,2,3),(4,5,6)]
print(f"We have matrix: m = {m}")

print(f"Use *m to load the args - these 2 tuples to transpose the lists: list(zip(*m)) :{list(zip(*m))}")

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

# 'all' return True if all elements of iterable are truthy (or iterable empty)
all([0, 1, 2, 3])  # False
all([char for char in 'eio' if char in 'aeiou'])
all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])  # True
# 'any' return True if any element of iterable is truthy. If iterable is empty ,retruns False
any([0, 1, 2, 3])  # True
any([val for val in [1, 2, 3] if val > 2])  # True
any([val for val in [1, 2, 3] if val > 5])  # False

### GLOBAL LOCAL SCOPES ####
print("===============")
print("GLOBAL LOCAL SCOPES")
# Python is familiar with scopes. The highest is Builtin scope (where defined True,list,print etc...)
# Next there is Global scope - all space that is outside of main() or any function
# Local scope is inside the function we work with
# When python encounter a function at complie-time it will scan for any variables that have values assigned to them
# It will search them anywhere in the function, if the variable has not been specified as global,then it is local
# If the variable is not found - only at run-time python will start looking higher in hierarchy to find the vars.

a=10
def func1():
    print("Inside func1")
    print(f"a: {a}")  #there is no assignment or definition locally so it will print a: 10

def func2():
    print("Inside func2")
    a=100    #Here python identifies a locally and the val is 100
    print(f"a: {a}") #output: a:100

def func3():
    global a
    a=200 #Here the assignment with global means we refer to a from globla scope so assignment of a = 200

def func4():
    #print(a)  #This will cause run-time error - because a is defined in the local scope but not yet, there is no
    #need to bring value from global scope where it exists, it is only run-time error ,at compile time it works
    print("Inside func4")
    a=100
    print(f"a: {a}") #output a:100  --> local

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
    x='hello'

    def inner1():
        x='python'
        def inner2():
            nonlocal x # this means it is closure - x inside inner2 refers to x in inner1
            x='monty'
        print(f"inner before {x}") #output: inner before python --> here x is still python
        inner2()
        print(f"inner after {x}") #outpt: inner after monty --> inside inner2() the globla to inner2 is x from inner1

    inner1()
    print(f"outer {x}") #output: outer hello -->The x of most global is not modified
    # - nonlocal of inner2 only relates to inner1
outer()
print("========================")
print("## ANOTHER NONLOCAL EXAMPLE ##")
def outer():
    x='hello'

    def inner1():
        nonlocal x
        x='python'
        def inner2():
            nonlocal x
            x='monty'
        print(f"inner before {x}") #output: inner before python --> here x python and it changed x with 'hello'
        inner2()
        print(f"inner after {x}") #outpt: inner after monty --> inside inner2() the globla to inner2 is x from inner1

    inner1()
    print(f"outer {x}") #output: outer monty -->The x of most global was modified because of nonlocal defined in inner1
outer()
print("========================")
print("## THIRD NONLOCAL EXAMPLE ##")

x=100
def outer():
    x='python'

    def inner1():
        nonlocal x
        x='monty'
        def inner2():
            global x
            x='hello'
        print(f"inner before {x}") #output: inner before monty --> here x python and it changed x to monthy
        inner2()
        print(f"inner after {x}") #outpt: inner after monty --> inside inner2() the global x 100 became hello

    inner1()
    print(f"outer {x}") #output: outer monty -->The x is still monty

outer()
print(f"After outer call x is {x}") #output: After outer call x is hello

### CLOSURE ####
print("========================")
print("## CLOSURE ##")

class Averager: #class example
    def __init__(self):
        self.total=0
        self.count=0

    def add (self,number):
        self.total+=number
        self.count+=1
        return self.total / self.count

def averager(): #closure with functions example
    total=0
    count=0
    def add(number):
        nonlocal total
        nonlocal count
        total+=number
        count+=1
        return total/count
    return add

avg_func = averager()  #each add will calcultate total/count
print(avg_func(10)) #output: 10   --> 10/1
print(avg_func(20)) #output: 15   --> (10+20)/2

avg_instance = Averager() # using instance of class
print(avg_instance.add(10)) #output: 10
print(avg_instance.add(20)) #output: 15

### DECORATORS ###
# Use this design pattern when 2 or more functions rely on another function
# Use this design pattern when a function has multiple responsibilities
# Use this design pattern when a function behavior needs to be extended
print("===============")
print("DECORATORS")

# Definition of general decorator
def dec(fn):
    print("Running Decorator")

    def inner(*args,**kwargs):
        print("Running Inner")
        return fn(*args,**kwargs)
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

        def inner(*args,**kwargs):
            print("Running Inner")
            return fn(*args,**kwargs)
        return inner
    return dec

@dec_factory()  #is the same as:  my_func = dec_factory()(my_func)
def my_func():
    print("Running myfunc")

my_func()
print("*********")
def dec_factory(a,b): #decorator factory with params - to create decorator that passes params
    print("Running dec_factory")
    def dec(fn):
        print("Running Decorator")

        def inner(*args,**kwargs):
            print("Running Inner")
            print(f"a={a},b={b}")
            return fn(*args,**kwargs)
        return inner
    return dec

@dec_factory(100,200)
def my_func():
    print("Running myfunc")

my_func()

print("====+++====")
print("Using Class as decorator:")
class MyClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self, fn):
        print("Calling __call__")
        def inner(*args,**kwargs):
            print("Inside Inner")
            print(f"decorated call function called: a={self.a}, b={self.b}")
            return fn(*args,**kwargs)
        return inner

@MyClass(10,20)
def my_func(s):
    print("Inside my_func")
    print(f"Hello {s}!")

#This is the same as creating instance: obj=MyClass(10,20)
# and then:  my_func = obj(my_func)

my_func('World')
print("====+++====")

## Decorating a class ##
from datetime import datetime,timezone

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
    cls.debug = info  #this is attribute added to the class dynamically
    return cls

@debug_info
class Person:
    def __init__(self,name,birth_year):
        self.name=name
        self.birth_year = birth_year

    def say_hi(self):
        return 'Hello There!'


p = Person('Dan', 1972)
print(p.debug()) #output: ['time: 10/02/21', 'Class: Person', 'id: 0x284cdfadfd0', 'name:Dan', 'birth_year:1972']


def timed(fn): # decorator for measure time
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args,**kwargs):
        start = perf_counter()
        result = fn(*args,**kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k}={v}" for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print((f"{fn.__name__}({args_str}) took {elapsed:.6f}s to run"))
        print(result)

        return result
    return inner

#fibonachi_recorsion
def calc_recursive_fib(n):
    if n<=2:
        return 1
    else:
        return calc_recursive_fib(n-1)+calc_recursive_fib(n-2)

@timed
def fib_recursive(n):
    return calc_recursive_fib(n)

#fibonachi_loop
@timed
def fib_loop(n):
    fib_1=1
    fib_2=1
    for i in range(3,n+1):
        fib_1,fib_2 = fib_2,fib_1+fib_2
    return fib_2

#fibonachi_func_with_cache
def memorize(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@memorize
def fib(n):
    return 1 if n<3 else fib(n-1) + fib(n-2)

class Fib:
    def __init__(self):
        self.cache = {1:1,2:1}

    def fib(self,n):
        if n not in self.cache:
            self.cache[n] = self.fib(n-1)+self.fib(n-2)
        return self.cache[n]

fib_recursive(30) #output: fib_recursive(30) took 0.145620s to run
fib_loop(30) #output: fib_loop(30) took 0.000010s to run

from time import perf_counter
start = perf_counter()
fib_instance = Fib()
end = perf_counter()
print((f"fib_instance took {end-start:.6f}s to run")) #output: fib_instance took 0.000004s to run
print(fib_instance.fib(30))

print(f"Fibonatch with cache: {fib(30)}") #output: Fibonatch with cache: 832040

## simple time measure decorator example ###
import time

def time_measure(f):
    t0 = time.time()
    f()
    t= time.time()
    return t-t0

@time_measure
def slow_code():
    time.sleep(2)

print(slow_code) #output: 2.011594533920288
print("=========&&&&&&&*********&&&&&&&&=======")
## Another simple decorator example ###
def print_argument(func):
    def wrapper(the_number):
        print("Decorator added explanation: Argument for",func.__name__,"is", the_number)
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
        int:pr_int,
        float:pr_float,
        str:pr_string
    }
    fn = registry.get(type(inp))
    return fn(inp)

func_inp(4) #output: This is an int: 4
func_inp(1.1) #output: This is float: 1.1000
func_inp("dan") #output: This is a string: dan

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

@func_arg.register(int)  #the operation here is: pr_int = func_arg.register(int)(pr_int)
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
	for i, e in enumerate(s):print(i, e)

fun('Oklahoma') # output: OKLAHOMA
fun(10) #output: 20
fun(['g', 'e', 'e', 'k', 's'])

@fun.register(float)
@fun.register(Decimal)
def _3(s):
    print(round(s, 2))

fun(2.3456789) #output: 2.35
fun(Decimal(4.897)) #output: 4.90

# dispatch() – To check which implementation will the generic function choose for a given type.
print(fun.dispatch(dict)) #output: <function fun at 0x0000021BEDFCD3A0>
print(fun.dispatch(list)) #output: <function _2 at 0x0000021BEDFF89D0>

# registry() – read-only attribute to access all registered implementations.
print(fun.registry.keys()) #output: dict_keys([<class 'object'>, <class 'int'>, <class 'list'>...
print(fun.registry[int]) #output: <function _1 at 0x000002C4468F8940>
print(fun.registry[object]) #output: <function fun at 0x000002C4468CD3A0>





### EXCEPTION RAISE ERROR ###
print("===============")
print("EXCEPTION RAISE ERRORS")
def colorize(text,color):
    colors = ["RED","GREEN","BLUE"]
    if type(color) is not str:
        raise TypeError("color must be string")
    if type(text) is not str:
        raise TypeError("text must be string")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

#colorize(1,"blue") #TypeError: text must be string
#colorize("dan",10) #TypeError: color must be string
#colorize("dan","blue") #ValueError: color is invalid color

### TRY/CATCH Blocks ###
print("===============")
print("TRY_CATCH Blocks")

def divide(a,b):
    try:
        result = a/b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong!")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")
    finally:
        print("==Will be printed anyway==")


print(divide(1,2))
print(divide(1,'a')) #unsupported operand type(s) for /: 'int' and 'str'
print(divide(1,0))   #division by zero

# How to create your own exception
class ExceptionA(Exception):
    pass

class ExceptionB(Exception):
    pass

for i in range(4):
    try:
        if i%2==0:
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
#Example for implemet print(__str__ or __repr__) and +

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

p1 = Point(1,2)
p2 = Point(4,5)
print(p2) #(4,5)
p3 = p1+p2
print(p3) #(5,7)


### CLASS ###
print("===============")
print("CLASS")

# regular class
class ClassSample:
    class_attribute=0  #this attribute is known to any instance of the class

    def __init__(self,attr1,attr2=0):
        self.attr1 = attr1
        self.attr2 = attr2
        self._private = "This is like private but can be accessed directly in main"
        self.__hidden = "This really can't be accessed in main\n \
        only by _ClassSample__hidden if need to access from main"
        self.__dunder__="Not recommended to use such function - only for python"
        ClassSample.class_attribute+=1  #counter of number of instances

    @classmethod
    def func_handle_class_attribute(cls,inp):
        print(f"This is method related to class attribute: {cls.class_attribute} and can use {inp}")

    @staticmethod
    def func_as_utility_not_related_to_cls():
        print(f"This is utility and {ClassSample.class_attribute} is not related to it")

    def instance_method(self,inp):
        print(f"This is instance_method with value {self._private} that receives {inp}")

    def logged_out(self):
        ClassSample.class_attribute-=1 #decrease number when logged out

    def print(self):
        print(f"We have {self.attr1} & {self.attr2} also have {self._private} and {self.__hidden} ")
        print(f"And our count is {ClassSample.class_attribute}")

    def __repr__(self):
        print("This method pretty the print of the instance ,i.e.: print(instance) is shown in __repr__")
        pass

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
    def priv(self,new_val):
        #value_if_true if condition else value_if_false
        self._private = new_val if new_val > 0 and new_val % 2 == 0 else 2

cs = ClassSample(123)
cs1 = ClassSample(321)
cs.print()
cs.priv=445
print(f"The value of _private in cs instance is {cs.priv}")

#Creating Custom Ctor and Custome Dtor
class C:
    def __init__(self):
        print("Contructor")

    def pr(self):
        print("Hello!!")

    def __del__(self):
        print("Destructor")

c = C()
c.pr()
#output: Constructor\nHello!!\nDestructor

#Demonstrating the work of __enter__ and __exit__ methods
class C:
    def some_work(self):
        print("Some work being Done!")
    def __enter__(self):
        print("ENTER")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT")

obj=C()
with obj:
    #as soon as you have 'with' you work with __enter__ & __exit__
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
    def __init__(self, fname, lname,school_name):
        super().__init__(fname, lname)
        self.uninversity = school_name

    def __repr__(self):
        return f"The student {self.firstname} {self.lastname} is studing in {self.uninversity} university"

st = Student("Mike","Pence","UCLA")
print(st) #The student Mike Pence is studing in UCLA university

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
    def __init__(self,name):
        self.name = name
        print(f"This is init of parent named {self.name}")

    def mtd(self):
        print(f"Parent method named {self.name}")

class Child1(Parent):
    def __init__(self, name,age):
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

c1 = Child1("c1",11)
c2 = Child2("c2",1234)
c1.mtd()
c2.mtd()
c3 = Child1("c3",22)
c4 = Child2("c4",4321)
c5 = Child1("c5",33)
c6 = Child2("c6",5678)

lst = [c1,c2,c3,c4,c5,c6]
for i in lst:
    i.mtd() #this is actually polymorphism

#ITERATORS VS ITERABLES
print("====================")
print("ITERATORS VS ITERABLES")

# Iterator = Object that returns data each time next() is called on it. Like pointer it = iter(var) == it is iterator.
# var is the iterable, we can do next() on iterator ,i.e.: next(it) bring next char in string
# Iterable = Object that returns an iterator when iter() is called on it.Data strcuture we can loop upon like list,str..
# next(string) will not work, next(iterator_to_string) will work.
# To make a class an Iterable we need to define __iter__() method
# To loop on the class - we need to define __next__() method

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
my_for(ls,print)
my_for(name, print)

print("Counter iterable example:")
class Counter:
    def __init__(self,low,high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num=self.current
            self.current+=1
            return num
        raise StopIteration

for x in Counter(10,15):
    print(x)

#Another basic example of custome iterator
class C:
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        self.n += 1
        return self.n

c = C()
i = iter(c) #get an iterator

for _ in range(5):
    #use the iterator
    print(next(i)) #output: 1 2 3 4 5

#GENERATORS
print("====================")
print("GENERATORS")

#Generators are iterators
#Can be created with generator functions
#use yield keyword
#Can be created with generator expressions

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
        yield i #not 'return'

g1 = f() #first generator object
g2 = f() #second generator object

print(next(g1)) #val from generator 1 #output: 0
print(next(g2)) #val from generator 2 #output: 0
print(next(g1)) #val from generator 1 #output: 1
print(next(g2)) #val from generator 2 #output: 1
print(next(g1)) #val from generator 1 #output: 2
print(next(g2)) #val from generator 2 #output: 2


# PICKLE
print("====================")
print("PICKLE")
# We can serialize simple objects on files - it is called pickle

import json
import pickle

class SomeClass:
    def __init__(self,name="",family="",age=0):
        self.name = name
        self.family = family
        self.age = age

    def __repr__(self):
        return f"This is {self.name} {self.family} aged {self.age}"

man = SomeClass("Dan","Belfer",48)
print(man)

json_structure = json.dumps(man.__dict__) #saved in json like a dictionary
print(json_structure)  #output: {"name": "Dan", "family": "Belfer", "age": 48}

# To pickle an object: Serialize it
with open("people.pickle", "wb") as file:
     pickle.dump(man, file)

# To unpickle something:
with open("people.pickle", "rb") as file:
     new_man = pickle.load(file)
     print(new_man)

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

#This is the clean easy to understand same solution like nested one - it is better!
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
name = {'first_name':'Dan','last_name':'Belfer'}
job = {'company':'Argus','role':'QA Engineer'}
contact = {'email':'blabla','twiter':'stam'}
"""We want to merge the 3 dictionaries to one dictionary"""
""""Example 1 : Very complicated way"""
items = [name,job,contact]
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

print("Example 2: Pythonic update a dictionary")
print(profile2)

dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged = { **dict1, **dict2 }

print("Example 3: Pythonic ** a dictionary")
print (merged)
# {'a': 1, 'b': 3, 'c': 4}

# Since Python 3.9 merging - with |

# Python >= 3.9 only
merged3_9 = dict1 | dict2
print("Example 4: Since Python 3.9 | a dictionary")
print (merged3_9)
# {'a': 1, 'b': 3, 'c': 4}


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
#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
#assert x == "goodbye"

#if condition returns False, AssertionError is raised:
#assert x == "goodbye", "x should be 'hello'"

# using assert to break the program if your data is wrong
def divide(x,y):
    assert y != 0
    return x/y

a = divide(100,10) #OK
print(f"Val of division is: {a}")

#a = divide(100,0) #ERROR
#print(f"Val of division is: {a}") #will not be printed


#### MEMORY USAGE ####
print("=====================")
print("MEMORY USAGE")

import sys

mylist = range(0, 10000)
print(f"Memory Usage of Mylist is {sys.getsizeof(mylist)}") #output: 48

#  why is this huge list only 48 bytes?
'''It’s because the range function returns a class that only behaves like a list. 
A range is a lot more memory efficient than using an actual list of numbers.
You can see for yourself by using a list comprehension to create an actual list of numbers from the same range:'''
import sys

myreallist = [x for x in range(0, 10000)]
print(f"Memory Usage of My real list is {sys.getsizeof(myreallist)}")