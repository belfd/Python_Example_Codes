# What defines tuples is not the () but ','
# Therefor a,b,c is equivalent to (a,b,c) - thats why (a) is not tuple but (a,) is tuple
# () is tuple to define empty one - although there is no ',' in it
# can define empty tuple also with tuple()

# create a tuple
digits = (0, 1, 'two')  # create a tuple directly
digits = tuple([0, 1, 'two'])  # create a tuple from a list it means we cannot add other object to the tuple
# but the list itself can be changed
zero = (0,)  # trailing comma is required to indicate it's a tuple
digits[2]  # returns 'two'
len(digits)  # returns 3
digits.count(0)  # counts the number of instances of that value, output: 1
digits.index(1)  # returns the index of the first instance of that value, output: 1

# elements of a tuple cannot be modified
# digits[2] = 2       # throws an error

# concatenate tuples - the '=' creates on left side new digits tuple
# (or else we would have receive error - tuple = immutable)
digits = digits + (3, 4)

# create a single tuple with elements repeated (also works with lists)
(3, 4) * 2  # returns (3, 4, 3, 4)

# sort a list of tuples
tens = [(20, 60), (10, 40), (20, 30)]
sorted(tens)  # sorts by first element in tuple, then second element
#   returns [(10, 40), (20, 30), (20, 60)]

# tuple unpacking = pulling values apart from a tuple
bart = ('male', 10, 'simpson')  # create a tuple
(sex, age, surname) = bart  # assign three values at once

# Trick to append values to tuple because it is immutable (non changed)
tuple1 = (1, 2, 3)
lst = list(tuple1)
lst.append(4)
lst.append(5)
tuple1 = tuple(lst)
print(f"new tuple after appending: {tuple1}")  # (1, 2, 3, 4, 5)

coords = 1, 2, 3, 4, 5, 6
x, y, z, *rest = coords
# Here 1 is assigned to x, 2 to y, 3 to z, and the rest of the values into rest.

print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")
print(f"rest: {rest}")
# Output:
# x: 1
# y: 2
# z: 3
# rest: [4, 5, 6]