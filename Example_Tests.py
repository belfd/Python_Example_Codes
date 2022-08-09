class Circle(object):
    pi = 3.14 # class attribute

    def __init__(self,radius_value):
        self.radius = radius_value   # instance attribute
        self.area = Circle.pi * self.radius ** 2  # instance attribute was not input from parameters
        self.circumference = self.pi * 2 * self.radius  # instance attribute was not input from parameters


my_circle = Circle(5)
my_circle.color = 1  # attribute defined outside of init
print(my_circle.radius)  # output: 5
print(my_circle.pi)  # output: 3.14
print(my_circle.color)  # output: 1
print(my_circle.area)  # output: 78.5