'''
Write a function called  that accepts a string and returns a dictionary with
the keys as the vowels and values as the count of
times that vowel appears in the string.

vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}

# VOWELS=('a','e','o','i','u')
#
# def vowel_count(inp:str)->dict:
#     dout = dict()
#     for i in inp:
#         if i in VOWELS:
#             dout[i]=dout[i]+1 if i in dout else 1
#
#     return dout

def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}

print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))
'''

'''
Write a function called  which accepts a string of words and returns a new string 
with the first letter of every word in the string capitalized.
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"


# def titleize(string:str)->str:
#     lst=string.split(' ') # split the string to components
#     lst1=[]
#     for i in lst:
#         lst1.append(i.capitalize()) #add each component to new list by capitilizing first letter
#     strout = " ".join(lst1)  # recereate new string
#     return strout

def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))
'''

'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''
''''
import math

def find_factors(num:int)->list[int]:
    lst=[]
    # run loop on all numbers from 1 to the square root of the number
    for i in range(1,round(math.sqrt(num))):
        if num%i==0:
            lst.append(i)
    lst.append(num)
    return lst
print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
'''
'''
Write a function called 'find_factors' which accepts a number and returns a list of all of the numbers 
which are divisible by starting from 1 and going up to the number


find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]

def find_factors(num:int)->list[int]:
    i=1
    factors=[]
    while i<=num:
        if num%i==0:
            factors.append(i)
        i+=1
    return factors

print(find_factors(111))
'''

'''
Write a function called 'two_list_dictionary' which accepts two lists of varying lengths.
The first list consists of keys and the second one consists of values. 
Your function should return a dictionary created from the keys and values. 
If there are not enough values, the remaining keys should have a value of null. 
If there not enough keys, just ignore the remaining values.
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}

def two_list_dictionary(inp1,inp2):
    if len(inp1) > len(inp2):
        n=len(inp1)-len(inp2)
        lst=[]
        for i in range(n):
            lst.append(None)
        inp2=inp2+lst
    result = zip(inp1,inp2)
    dic = {}
    for k,v in result:
        dic.setdefault(k,[]).append(v)
    return dic

def two_list_dictionary(keys, values):
    collection = {}

    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
        else:
            collection[keys[idx]] = None

    return collection

print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]))
print(two_list_dictionary(['x', 'y', 'z']  , [1,2]))
'''

'''
Write a function called 'range_in_list' which accepts a list and start and end indices,
and returns the sum of the values between (and including) the start and end index.

If a start parameter is not passed in, it should default to zero. 
If an end parameter is not passed in, it should default to the last value in the list. 
Also, if the end argument is too large, the sum should still go through 
the end of the list.

def range_in_list(lst, start=0, end=None):
        end = end or lst[-1]
        return sum(lst[start:end + 1])

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0
'''

'''
Write a function called "same_frequency" which accepts two numbers and returns 
True if they contain the same frequency of digits. 
Otherwise, it returns False.

same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True


def same_frequency(inp1,inp2):
    d1 = {letter: str(inp1).count(letter) for letter in str(inp1)}
    d2 = {letter: str(inp2).count(letter) for letter in str(inp2)}

    for key, val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True

print(same_frequency(551122,221515)) #output: True
'''

'''
Write a function called find_the_duplicate which accepts an array of numbers containing a single duplicate. 
The function returns the number which is a duplicate or None if there are no duplicates.

find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None

def find_the_duplicate(lst):
    for letter in lst:
        if lst.count(letter)>1:
            return letter
    return None

print(find_the_duplicate([2,1,3,4]))
'''

'''
Write a function called min_max_key_in_dictionary which returns a list with the lowest key in the dictionary 
and the highest key in the dictionary. 
You can assume that the dictionary will have keys that are numbers.

min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]


def min_max_key_in_dictionary(inp):
    lstmin,lstmax = min(inp.keys()),max(inp.keys())
    return lstmin,lstmax

print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}))
'''

'''
Create a function "running_average" that returns a function.
When the function returned is passed a value, 
the function returns the current average of all previous function calls. 
You will have to use closure to solve this. 
You should round all answers to the 2nd decimal place.

def running_average():
    running_average.tot=0
    running_average.counter=0
    def inner(n):
        running_average.tot+=n
        running_average.counter+=1
        yield running_average.tot/running_average.counter
    return inner


rAvg = running_average()
print(next(rAvg(1))) # 1
print(next(rAvg(2))) # 1.5
print(next(rAvg(3))) # 2
print(next(rAvg(4))) # 2.5
'''

'''
Write a function called letter_counter which accepts a string and returns a function. 
When the inner function is invoked it should accept a parameter which is a letter, 
and the inner function should return the number of times that letter appears. 
This inner function should be case insensitive.
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

def letter_counter(strinp):
    letter_counter.strtmp=strinp.lower()
    letter_counter.dict={}

    for letter in letter_counter.strtmp:
        letter_counter.dict[letter] = letter_counter.dict[letter] + 1 if letter in letter_counter.dict.keys() else 1

    def inner(chr):
        return letter_counter.dict[chr]

    return inner

counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1
'''
'''
Check for Uniqueness
The following function will check if all elements in a list are unique or not.


def unique(l):
    if len(l)==len(set(l)):
        print("All elements are unique")
    else:
        print("List has duplicates")

unique([1,2,3,4]) #output: All elements are unique

unique([1,1,2,3]) #output: List has duplicates
'''

'''
convert an integer into a list of digits

num = 123456

# using map
list_of_digits = list(map(int, str(num)))

print(list_of_digits) # [1, 2, 3, 4, 5, 6]

# using list comprehension
list_of_digits = [int(x) for x in str(num)]

print(list_of_digits) # [1, 2, 3, 4, 5, 6]

# Even simpler approach
list_of_digits = list(str(num))

print(list_of_digits) # [1, 2, 3, 4, 5, 6]
'''

'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''
'''
def add(a,b):
    return a+b

def once(inp):
    once.parm=False
    once.input=inp
    def inner(a,b):
        once.parm = False
        return None if once.parm == True else inp(a,b)

    return inner


oneAddition = once(add)
print(oneAddition(2,2)) # 4
print(oneAddition(2,2) # None
print(oneAddition(12,200)) # None



# Example 1: shuffle data to ensure random class distribution in train/test split
import random

documents = ["positive tweet message", "negative tweet message"]
labels = ["pos", "neg"]

tuples = [(doc, label) for doc, label in zip(documents, labels)]
print(f"tuples is {tuples}")  # tuples is [('positive tweet message', 'pos'), ('negative tweet message', 'neg')]
random.shuffle(tuples)
X, Y = zip(*tuples)
print(f"X is {X} and Y is {Y}")  # X is ('negative tweet message', 'positive tweet message') and Y is ('neg', 'pos')

# Example 2: merging two dictionaries
first_dictionary = {"A": 1, "B": 2}
second_dictionary = {"C": 3, "D": 4}
merged_dictionary = {**first_dictionary, **second_dictionary}
print(merged_dictionary)  # output: {"A": 1, "B": 2, "C": 3, "D": 4}


# Example 3: dropping unnecessary function variables
def return_stuff():
    """Example function that returns data."""
    return "This", "is", "interesting", "This", "is", "not"


a, b, c, *_ = return_stuff()
print(f"{a} {b} {c}")  # output: This is interesting
'''
'''
data = [
    ("Hi my name is Dan, and I write sentences, often delimited by a comma", "48", "Belfer")
]
with open("texts.csv", "w") as csv_out:
    for element in data:
        csv_out.write("{0}\n".format(",".join(element)))

objects = []
with open("texts.csv", "r") as csv_in:
    for line in csv_in:
        line = line.rstrip().split(",")
        objects.append(line)

print(objects) # [['Hi my name is Dan', ' and I write sentences', ' often delimited by a comma', '48', 'Belfer']]

import json

# JSON encoding
string = "I am a Dan Belfer and works with python."
s = json.dumps(string)

with open("data.json", "w") as json_out:
    json_out.dumps(string)

# JSON decoding
string = '["list_item", {"personal":["Louis", null, 8.3, 26]}]'
s = json.loads(string)

with open("data.json", "r") as json_in:
    string = json.load(json_in)
'''
## REPLACEMENT to NESTED LOOPS - Using itertools
# import itertools

'''
list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]


for a in list_a:
    for b in list_b:
        for c in list_c:
            if a + b + c == 2077:
                print(a, b, c)


for a, b, c in itertools.product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)  #output: 70 2000 7


natural_num = count(1)
for n in natural_num:
    print(n)  #1,2,3,4,...

many_yang = itertools.cycle('Yang')
for y in many_yang:
    print(y) #Y,a,ng,Y,a,..

many_yang = itertools.repeat('Yang')
for y in many_yang:
    print(y) #Yang,Yang,...

list_a = [1, 22]
list_b = [7, 20]
list_c = [3, 70]

for i in itertools.chain(list_a, list_b, list_c):
    print(i) #1,22,7,20,3,70

from itertools import groupby

for key, group in groupby('YAaANNGGG'):
    print(key, list(group)) #Y['Y],A['A'],a['a'],['A'],N['N','N'],G['G','G','G']
'''
'''
### Using assistant class
class MessageFormatter:
    def success(self, message):
        return f"👍 {message}"


class MessageWriter:
    def __init__(self):
        self.message_formatter = MessageFormatter()

    def write(self, message):
        print(self.message_formatter.success(message))


message_writer = MessageWriter()
message_writer.write("Hello World!")
'''

#print("odd" if 14 % 2 == 0 else "even")

#  class Student(object):
#
#     def __new__(cls, *args, **kwargs):
#         print("Running __new__() method.")
#         instance = object.__new__(cls)
#         return instance
#
#     def __init__(self, first_name, last_name):
#         print("Running __init__() method.")
#         self.first_name = first_name
#         self.last_name = last_name
#
# s1 = Student("Dan", "Belfer") # Running __new__() method.
#                               # Running __init__() method.
#
# print(s1.last_name)  #Belfer

# def find_happy_numbers(inp: int) -> None:
#     inp1 = inp
#     summary = None
#     index = 0
#     while summary != 1:
#         index += 1
#         if index > 10:
#             # print(f"{inp1} is a Sad number")
#             break
#         if inp == 0:
#             inp = summary
#         summary = 0
#         while inp != 0:
#             dig = inp % 10
#             summary += dig ** 2
#             inp //= 10
#     else:
#         print(f"{inp1} is is a happy number")
#
#
# for i in range(1, 40):
#     find_happy_numbers(i)

# def square_numbers(nums):
#     for i in nums:
#         yield (i * i)
#
#
# my_nums = square_numbers([1, 2, 3, 4, 5])
#
# for num in my_nums:
#     print(num)


# def outer_func():
#     leader = "Dan Belfer"
#
#     def print_leader():
#         print(leader)
#
#     return print_leader
#
# f = outer_func()
# print(outer_func.__closure__) #output: None
# print(f.__closure__) #output: (<cell at 0x0000025113E77FD0: str object at 0x0000025113DBEF30>,)
# print(f.__closure__[0].cell_contents) #output: Dan Belfer
# del outer_func
#
# ## Why its local variable [outer_func] is still alive after removing the function?
# f() #output: Dan Belfer
# # outer_func() # -- causes error : name 'outer_func' is not defined

'''
The closure in Python is a function which remembers values in its enclosing scope.
The appearance of the closure must meet three conditions:
There are nested functions.
The inner function must use variables defined in its outer function.
The outer function must return the inner function.

The outer_func is not a closure and its __closure__ attribute is None. 
In the other hand, the __closure__ of f contains a cell object which saves the “remembered” value.
'''
# I want to test squash
# Again I want to commit

#second commit to revert
#another change
# a real one
