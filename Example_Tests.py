# ## Static and Class methods can be inherited ##
#
# class A:
#     def __init__(self,attr1=1,attr2=2):
#         self.attr1=attr1
#         self.attr2=attr2
#
#     def instance_method(self):
#         print(f"info of class {self} with attributes attr1: {self.attr1} attr2: {self.attr2}")
#
#     @classmethod
#     def get_instance(cls,atr1,atr2):
#         print(f"class method of {cls}")
#         return cls(atr1,atr2)
#
#     @staticmethod
#     def static_func(in1,in2):
#         print(f"static method of A")
#
# class DeriveA(A):
#     def __init__(self,a1,a2,da1=111,da2=222):
#         self.derattr1 = da1
#         self.derattr2 = da2
#         super().__init__(a1,a2)
#
#     def instance_method(self):
#         print(f"info of class {self} with attributes derattr1: {self.derattr1} derattr2: {self.derattr2}")
#
#
# a_sample = A(15,3)
# a_sample.instance_method() #info of class <__main__.A object at 0x00000217CAD9FEE0> with attributes attr1: 15 attr2: 3
# print("class method:\n")
# a_sample.get_instance(11,22).instance_method()
# #class method of <class '__main__.A'>
# #info of class <__main__.A object at 0x00000217CAD9FF70> with attributes attr1: 11 attr2: 22
# A.static_func(2,3) # static method of A
#
# da_sample = DeriveA(1,2,3,4)
# da_sample.instance_method()
# # info of class <__main__.DeriveA object at 0x00000217CAD9FF70> with attributes derattr1: 3 derattr2: 4
# da_sample.get_instance(20,30).instance_method()  # class method of <class '__main__.DeriveA'>
# # info of class <__main__.DeriveA object at 0x00000217CAD9FE20> with attributes derattr1: 111 derattr2: 222
# da_sample.static_func(5,6) # static method of A
#
#
#
'''
from collections import deque


def produce_element(dq, n):
    print('\nIn producer ...\n')
    for i in range(n):
        dq.appendleft(i)
        print(f'appended {i}')
        # if deque is full, return the control back to `coordinator`
        if len(dq) == dq.maxlen:
            yield


def consume_element(dq):
    print('\nIn consumer...\n')
    while True:
        while len(dq) > 0:
            item = dq.pop()
            print(f'popped {item}')
        # once deque is empty, return the control back to `coordinator`
        yield


def coordinator():
    dq = deque(maxlen=2)
    # instantiate producer and consumer generator
    producer = produce_element(dq, 5)
    consumer = consume_element(dq)

    while True:
        try:
            # producer fills deque
            print('next producer...')
            next(producer)
        except StopIteration:
            break
        finally:
            # consumer empties deque
            print('next consumer...')
            next(consumer)


if __name__ == '__main__':
    coordinator()

'''
import abc

'''
We can say that there are two types of implementation: overloading (@ compile-time) and overriding (@ runtime). 
Overloading is not supported in Python, however, we can use a Python package, multipledispatch that does overloading.

Overriding
Methods owned by parent classes are rewritten in child classes and customized according 
to the intended use of these child classes. 
Now let me explain the subject with an example. 
I have a method, it accepts a device and opens it by pressing the button as long as the device has a device.
@@ Example:

from abc import ABC

class ADevice(ABC):
    @abc.abstractclassmethod
    def press_button(self):
        pass

class Device(ADevice):
    def press_button(self):
        print("Starting Device..")

def open_device(device):
    try:
        device.press_button()
    except AttributeError:
        print("This device has no button to open..")

class Laptop(Device):
    def press_button(self):
        print("Starting CPU..")

class Television(Device):
    def press_button(self):
        print("Starting Screen..")

class Speaker(Device):
    def press_button(self):
        print("Playing Sound..")

L,T,S = Laptop(),Television(),Speaker()
device_list = [L,T,S]

for d in device_list:
    open_device(d)

## output:
#Starting CPU..
#Starting Screen..
#Playing Sound..
'''
'''
Overloading in Python
Python doesn’t support overloading as Java does. It can be applied indirectly. I will use multipledispatch package.

from multipledispatch import dispatch

class Car:
    def __init__(self):
        self.speed=100

    @dispatch()
    def accelerate(self):
        self.speed+=10

    @dispatch(int)
    def accelerate(self,acc):
        self.speed+=acc

    @dispatch(float)
    def accelerate(self,acc):
        self.speed+=(self.speed*acc)

    @dispatch(int,float)
    def accelerate(self,acc,percentage):
        acc*=percentage
        self.speed+=acc

    def get_speed(self):
        print(f"Current speed is: {self.speed}")

C = Car()
C.accelerate()
C.get_speed() #output: Current speed is: 110
C.accelerate(20)
C.get_speed() #output: Current speed is: 130
C.accelerate(0.1)
C.get_speed() #output: Current speed is: 143.0
C.accelerate(50,0.1)
C.get_speed() #output: Current speed is: 148.0
'''





