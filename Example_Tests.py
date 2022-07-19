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