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


area_square(2) #output: 4
area_circle(2) #output: 12.56
area_rectangle(2, 4) #output: 8
area_square("some_str") # output: area_square only takes numbers as the argument
area_circle("some_other_str") # output: area_circle only takes numbers as the argument
area_rectangle("some_other_rectangle") #output: area_rectangle only takes numbers as the argument