# Composition is a concept that models a has a relationship.
# It enables creating complex types by combining objects of other types.
# This means that a class can contain an object of another class.
# This relationship means that a class has a class.

class Student:
      def __init__(self,name,rollno,marks):
         self.name = name
         self.rollno = rollno
         self.marks = marks
      def Info(self):
         print('Student name is ',self.name,'roll no ',self.rollno)

class Result:
      def __init__(self,name,rollno,marks):
          self.student = Student(name,rollno,marks)

      def printInfo(self):
          self.student.Info()

s = Result('sam',233,56)
s.printInfo() #output: Student name is  sam roll no  233

# The composition is similar to inheritance but we cannot call the methods
# of the class that we defined inside the result class.

# Inheritance Vs Composition:
class Employee:
 def __init__(self,name,eid):
  self.name = name
  self.eid = eid
 def printDetails(self):
  print('Employee name is {} and Employee no is     {}'.format(self.name,self.eid))
#inheritance - is a relationship
class Supervisior(Employee):
 pass
#composition - has a relationship
class TL():
 def __init__(self,name,eid):
  self.employee = Employee(name,eid)
 def empDetails(self):
  self.employee.printDetails()

s = Supervisior('jon',25)
t = TL('Tom',30)
s.printDetails()  #output: Employee name is jon and Employee no is     25
t.empDetails()    #output: Employee name is Tom and Employee no is     30

# We can see that we can directly call a method of a parent class in subclass using Inheritance
# whereas in composition we have to define it under the other module.
