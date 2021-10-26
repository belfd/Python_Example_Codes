
# What is a metaclass?
# A metaclass is a class that defines the behavior of the classes and their instances.
# A metaclass is a class whose instances are classes.

# How to create a class dynamically in python? using 'type' not metaclass
def mymethod(self):
    return self.x > 100

class_name = "MyClass"
base_classes = tuple()
params= {"x": 10, "check_greater": mymethod}
MyClass = type("MyClass", base_classes, params)  # 3 parts in init with type class - name,base_classes, attribs as dict
obj = MyClass()
print(obj.check_greater()) #output: False

# A metaclass lets us to customize the creation of our user-defined classes before they are actually created!
# In other words, it can add or remove attributes, methods or base classes to the actual class.
# Metaclass is nothing but a class that derives from class type .
#  Metaclass may override the methods__new__, __init__ or __call__ on class typeto provide customized behavior.

# Lets say, I want to create a custom type of string which has method that says whether
# the given string equals to zero. meaning "0000"
# iszero method is not part of str type

class StringFactory(type):
    def iszero(self):
        """Check if the given string is equals to one or more zeros"""
        try:
            return not sum([int(chr) for chr in self]) # when "0000" it returns True
        except:
            return False
    def __new__(cls, name, bases, dct):
        print("My class is not yet created")
        bases += (str,)  # add str class as base to the new class
        dct["iszero"] = StringFactory.iszero  # add our custom method to the new class
        class_ = type.__new__(cls, name, bases, dct)
        print("My class is created with custom method at run time")
        return class_

# define the metaclass
class MyCustomString(metaclass=StringFactory):
    pass

test_string = MyCustomString("abcd")
print(f"For 'abcd' it is: {test_string.iszero()} ")  # Outputs False
test_string = MyCustomString("0000")
print(f"For '0000' it is:{test_string.iszero()}")  # Outputs True

# Assume that, we have to create a singleton class which creates only 1 object in
# its lifetime irrespective of the number of times the class is instantiated.

# Let us see how we can use the __call__ method in a metaclass.
class MyMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in MyMeta._instances:
            MyMeta._instances[cls] = super().__call__(*args, **kwargs)
        return MyMeta._instances[cls]


class Singleton(metaclass=MyMeta):
    pass


x = Singleton()
y = Singleton()
print(f"The example says x is y: {x is y}")  # Outputs True

