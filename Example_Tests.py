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

