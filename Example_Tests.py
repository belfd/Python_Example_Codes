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
Write a function called 'find_factors' which accepts a number and returns a list of all of the numbers 
which are divisible by starting from 1 and going up to the number


find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]


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