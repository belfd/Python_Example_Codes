# 1. Swapping Two Variables
a = 4
b = 5
a,b = b,a
print(a,b) #output: 5,4
#2. Multiple Variable Assignments
a,b,c = 4,5.5,'Hello'
print(a,b,c) #output: 4,5.5,hello
a,b,*c = [1,2,3,4,5]
print(a,b,c) #output: 1 2 [3,4,5]
#3. Sum of Even Numbers In a List
a = [1,2,3,4,5,6]
s = sum([num for num in a if num%2 == 0])
print(s)  #output: 12
#4. Deleting Multiple Elements from a List
#del is a keyword used in python to remove values from a list.
#### Deleting all even
a = [1,2,3,4,5]
del a[1::2]
print(a) #[1, 3, 5]
#5. Reading Files
#lst = [line.strip() for line in open('data.txt')]
#print(lst)
#There is one much simpler and shorter way of doing this using just the list function.
#list(open('data.txt'))
##Using with will also close the file after use
#with open("data.txt") as f: lst=[line.strip() for line in f]
#print(lst)
#6. Writing data to file
#with open("data.txt",'a',newline='\n') as f: f.write("Python is awsome")
#The above code will first create a file data.txt if not already there, and then it will write Python is awsome in the file.
#7. Creating Lists
lst = [i for i in range(0,10)]
print(lst) #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
## or ##
lst = list(range(0,10))
print(lst)
#We can also create a list of strings using the same method.
lst = [("Hello "+i) for i in ['Karl','Abhay','Zen']]
print(lst) #output: ['Hello Karl', 'Hello Abhay', 'Hello Zen']
#8. Mapping Lists or TypeCasting Whole List
'''Sometimes in our project, we need to change the data types of all the elements in a list. 
The first method which comes to your mind is to use a loop and then access all the elements from the list 
and then one by one change the data type of the elements. 
This method is for the old school in python we have map a function that can do the work for us.'''
list(map(int,['1','2','3'])) # [1, 2, 3]
list(map(float,[1,2,3])) # [1.0, 2.0, 3.0]
[float(i) for i in [1,2,3]] # [1.0, 2.0, 3.0]
# 9. Set Creation
'''The method we used to create lists can be also used to create Sets. 
Let’s create a set using the method that contains the square root of all the even numbers in the range.'''
#### Square of all even numbers in an range
{x**2 for x in range(10) if x%2==0} # {0, 4, 16, 36, 64}
#10. Fizz Buzz
'''In this quiz, we need to write a program that prints the numbers from 1 to 100. 
But for multiples of three, print “Fizz” instead of the number, and for the multiples of five, print “Buzz”.
It looks like we have to use loops and multiple if-else statements. 
If you try to do it in any other language that you may have to write up to 10 lines of code but using python, 
we can implement FizzBuzz using just a single line of code.'''
['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i  for i in range(1,20)]
'''In the above code, we are using list comprehension to run a loop from 1 to 20, 
and then at each iteration of the loop, we are checking whether the number is divisible with 3 or 5. 
If yes, then we are replacing the number with Fizz or Buzz accordingly, else we replace the number with FizzBuzz.'''
#11. Palindrome
#A palindrome is a number or a string that looks the same when it gets reversed.
text = 'level'
ispalindrome = text == text[::-1]
ispalindrome #output: True
# 12. Space Separated integers to a List
lis = list(map(int, input().split()))
print(lis) #output:  [1, 2, 3, 4, 5, 6, 7, 8]
# 13. Lambda Function
'''A lambda function is a small anonymous function. A lambda function can take any number of arguments, 
but can only have one expression.'''
sqr = lambda x: x * x  ##Function that returns square of any number
sqr(10) #output: 100
# 14. To Check The Existence of a number in a list
num = 5
if num in [1,2,3,4,5]:
    print('present')  #output: present
# 15. Printing Patterns
'''Patterns are something that always fascinates me. 
In python, we can draw amazing patterns using just a single line of code.'''
n = 5
print('\n'.join('😀' * i for i in range(1, n + 1)))
'''
😀
😀😀
😀😀😀
😀😀😀😀
😀😀😀😀😀
'''
# 16. Finding Factorial
# Factorial is the product of an integer and all the integers below it.
import math
n = 6
math.factorial(n) #output: 720
#17. Fibonacci Series
'''A series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. 
The simplest Fibonacci series 1, 1, 2, 3, 5, 8,13 etc. 
We can use list comprehensions and a for loop to create a Fibonacci series in a range.'''
fibo = [0,1]
[fibo.append(fibo[-2]+fibo[-1]) for i in range(5)]
fibo #output: [0, 1, 1, 2, 3, 5, 8]
#18. Prime Number
'''A prime number is a number that is divisible only by itself and 1. eg: 2,3,5,7 etc. 
To generate prime numbers in a range we can use the list function with filter and lambda to generate prime numbers.'''
list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13))) #output: [2, 3, 5, 7, 11]
#19. Finding Max Number
findmax = lambda x,y: x if x > y else y
findmax(5,14) #output: 14
## or
max(5,14) #output: 14
'''In the above code using the lambda function we are checking the comparison condition and according
 to that returning the max number. '''
# 20. Linear Algebra
''' Sometimes we need to scale the elements of a list to 2 times or 5 times. The code explains how.'''
def scale(lst, x): return [i*x for i in lst]
scale([2,3,4], 2) ## call  [4,6,8]
#21. Transpose of a matrix
'''You need to change all the rows into columns and vice versa. 
In python, you can transpose a matrix in just one line of code using zip functions. '''
a=[[1,2,3],
  [4,5,6],
  [7,8,9]]
transpose = [list(i) for i in zip(*a)]
transpose #output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# 22. Counting occurrence of a pattern
'''It is an important and useful use case when we need to know the count of occurrences of a pattern in the text. 
In python, we have the re library to do this work for you.'''
import re; len(re.findall('python','python is a programming language. python is python.')) #output: 3
#23. Replacing a text with some other text
"python is a programming language.python is python".replace("python",'Java')
#output: Java is a programming language. Java is Java
# 24. Simulating Toss of a coin
''' It may be not that important, but it can be very useful whenever you need to generate
 some random choice from a given set of choices.'''
import random; random.choice(['Head',"Tail"]) #output: Head
# 25. Generating Groups
groups = [(a, b) for a in ['a', 'b'] for b in [1, 2, 3]]
groups # [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]


