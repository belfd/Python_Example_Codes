# class Cls(object):
#     cls_attr: int = 12
#
#     def __init__(self, obj_attr):
#         self.obj_attr = obj_attr
#
#     @staticmethod
#     def static_func():
#         print(f"This is a static method")
#
#     @property
#     def prop_attr(self):
#         return self.obj_attr
#
#     @prop_attr.setter
#     def prop_attr(self, inp):
#         self.obj_attr = inp
#
#     # instance method
#     def prn_obj_method(self):
#         print(f"Value of obj_attr is {self.obj_attr}")
#
#     def create_instance_var(self):
#         self.instance_var = 123
#
#     def prn_ins_var(self):
#         print(f"Value of inner_var: {self.instance_var}")
#
#     @classmethod
#     def squaring_obj_attr(cls):
#         return (cls.cls_attr * cls.cls_attr)
#
#
# a = Cls(11)
# a.obj_attr = 22
# a.prn_obj_method() # output: Value of obj_attr is 22
# print("-------")
# print(f"Squaring class attribute: {a.squaring_obj_attr()}") # output: Squaring class attribute: 144
# print("-------")
# a.prop_attr = 13
# print(f"Value of object property: {a.prop_attr}") # output: Value of object property: 13
# print("-------")
# a.prn_obj_method() # output: Value of obj_attr is 13
# a.static_func() # output: This is a static method
# a.create_instance_var()  # you have to run this before next method
# a.prn_ins_var() # output: Value of inner_var: 123

class Car:
   def __init__(self):
      self.fuel_amount = 0

   @property
   def fuel_amount(self):
      return self._fuel_amount

   @fuel_amount.setter
   def fuel_amount(self, amount):
      if amount < 0:
         raise ValueError("Tank can't be less than empty!")

      if amount > 60:
         raise ValueError("Tank can't take more than 60 l!")

      self._fuel_amount = amount

car = Car()
#car.fuel_amount = -10 will cause "ValueError: Tank can't be less than empty!"

"""
Descriptors provide a solution that helps us separating concerns within our class, 
so our code remains nice and SOLID. By using a descriptor instead of a property, our Car class gets as short as this:
"""


#Descriptor
class SixtyLitresCapacity:
   def __set__(self, car, amount):
      if amount < 0:
         raise ValueError("Tank can't be less than empty!")

      if amount > 60:
         raise ValueError("Tank can't take more than 60 l!")

      car._fuel_amount = amount

   def __get__(self, car, objtype=None):
      return car._fuel_amount


class Car:
   fuel_amount = SixtyLitresCapacity()

   def __init__(self):
      self.fuel_amount = 0



car1 = Car()
# car1.fuel_amount = 70  ## Error occur: "ValueError: Tank can't take more than 60 l!"

#Better after refactoring:
class IsBetween:
   def __init__(self,
                min_value,
                max_value,
                below_exception=ValueError(),
                above_exception=ValueError()):
      self.min_value = min_value
      self.max_value = max_value

      self.below_exception = below_exception
      self.above_exception = above_exception

   def __set_name__(self, owner, name):
      self.private_name = '_' + name
      self.public_name = name

   def __set__(self, obj, value):
      if value < self.min_value:
         raise self.below_exception

      if value > self.max_value:
         raise self.above_exception

      setattr(obj, self.private_name, value)

   def __get__(self, obj, objtype=None):
      return getattr(obj, self.private_name)


class Car:
   fuel_amount = IsBetween(0, 60, ValueError(), ValueError())

   def __init__(self):
      self.fuel_amount = 0

car2 = Car()
# car2.fuel_amount = 70  ### Raise Error: "raise self.above_exception ValueError"