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
print(my_func.__code__.co_argcount)  # output: 3   ; for a,b,c - show only positional arguments
print(my_func.__code__.co_varnames)  # output: ('a', 'b', 'c', 'kw1', 'kw2', 'kw3', 'args', 'kwargs', 'i', 'j')
print(inspect.getdoc(my_func))  # output: This is a function for explanation
# print(inspect.signature(my_func).parameters) # output will be all parameters
# for k,v in inspect.signature(my_func).parameters.items():
#    print(f"{k} : {v} ") #output: all the params with values
