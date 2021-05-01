'''
Write a function called  that accepts a string and returns a dictionary with
the keys as the vowels and values as the count of
times that vowel appears in the string.

vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}

VOWELS=('a','e','o','i','u')

def vowel_count(inp:str)->dict:
    dout = dict()
    for i in inp:
        if i in VOWELS:
            dout[i]=dout[i]+1 if i in dout else 1

    return dout

print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))
'''