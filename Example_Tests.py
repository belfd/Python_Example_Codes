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


def change(my_list):
   my_list.append(5)
   return my_list

my_list = [10, 20]
print(change(my_list))
print(my_list)
# Output:
# [10, 20, 5]
# [10, 20, 5]