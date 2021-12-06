# This findall() function returns a list of strings that are matched with the pattern.
import re
text = "Hello 12, how are you? This is 13"
pattern = "\d+"
result = re.findall(pattern, text)
print(result) #Output: ['12', '13']

# This search() method is used to search a particular pattern in a given text/string.
# This method returns a match object if the matched pattern is found in the text. Otherwise, it returns None .

import re
text = "Python is a programming language"
#cheking if 'Python' is present at the beginning
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
print(result) #Output: ['Hello ', ', how are you? This is ', '']

# This sub() function is used to find a pattern in a string and then replace that pattern with some other text.
# This function takes three parameters pattern, replace, string as input.

import re
text = "Namaste World! How are you doing?"
#replacing whitespace characters with '!!'
result = re.sub("\s", "!!", text)
print(result) #Output: Namaste!!World!!!How!!are!!you!!doing?

# This subn() method is almost similar to sub() method. The only difference is in the output of both methods.
# The sub() method returns the string after replacing the matched pattern with replace parameter text,
# and the subn() method returns a tuple that consists of a modified string along with the number of replacements
# in the string.

import re
text = "Namaste world. I prefer to work at night"
pattern = "wo"
result = re.subn(pattern, "~", text)
print(result) # Output: ('Namaste ~rld. I prefer to ~rk at night', 2)

