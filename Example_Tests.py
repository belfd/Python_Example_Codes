## Static and Class methods can be inherited ##

class A:
    def __init__(self,attr1=1,attr2=2):
        self.attr1=attr1
        self.attr2=attr2

    def instance_method(self):
        print(f"info of class {self} with attributes attr1: {self.attr1} attr2: {self.attr2}")

    @classmethod
    def get_instance(cls,atr1,atr2):
        print(f"class method of {cls}")
        return cls(atr1,atr2)

    @staticmethod
    def static_func(in1,in2):
        print(f"static method of A")

class DeriveA(A):
    def __init__(self,a1,a2,da1=111,da2=222):
        self.derattr1 = da1
        self.derattr2 = da2
        super().__init__(a1,a2)

    def instance_method(self):
        print(f"info of class {self} with attributes derattr1: {self.derattr1} derattr2: {self.derattr2}")


a_sample = A(15,3)
a_sample.instance_method() #info of class <__main__.A object at 0x00000217CAD9FEE0> with attributes attr1: 15 attr2: 3
print("class method:\n")
a_sample.get_instance(11,22).instance_method()
#class method of <class '__main__.A'>
#info of class <__main__.A object at 0x00000217CAD9FF70> with attributes attr1: 11 attr2: 22
A.static_func(2,3) # static method of A

da_sample = DeriveA(1,2,3,4)
da_sample.instance_method()
# info of class <__main__.DeriveA object at 0x00000217CAD9FF70> with attributes derattr1: 3 derattr2: 4
da_sample.get_instance(20,30).instance_method()  # class method of <class '__main__.DeriveA'>
# info of class <__main__.DeriveA object at 0x00000217CAD9FE20> with attributes derattr1: 111 derattr2: 222
da_sample.static_func(5,6) # static method of A



