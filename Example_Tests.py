# You may set characteristics for functions in a similar way that you can for classes and objects.
# This is useful when you don’t want to explicitly return a variable using the return statement each time the function
# is run but still want the ability to recover a variable that was sent in as an intermediate.
# Also take note that attributes may be set from either inside or outside the function declaration.
def func(x):
    intermediate_var = x**2 + x + 1

    if intermediate_var % 2:
        y = intermediate_var ** 3
    else:
        y = intermediate_var **3 + 1

    # setting attributes here
    func.optional_return = intermediate_var
    func.is_awesome = 'Yes, my function is awesome.'

    return y

y = func(3)
print('Final answer is', y)
# Accessing function attributes
print('Show calculations -->', func.optional_return)
print('Is my function awesome? -->', func.is_awesome)
y = func(5)
func.var = 11
print('Show calculations -->', func.optional_return)
print('Is my function awesome? -->', func.is_awesome)
print(f"addition variable to func: {func.var}")