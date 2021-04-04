# This is explanation of SOLID design principles in python #
# The principles are:
# Single Responsibility Principle
# Open Closed Princple
# Liskov's Substitutablilty Principle
# Interface Segregation Principle
# Dependency Inversion Principle

# Single Responsibility Principle(SRP):
# A class should have only one responsibility and only one reason to change.
# That means a class does not perform multiple jobs.

# Example of Violation:
# class Account:
#    """Demo bank account class """
#    def __init__(self, account_no: str):
#        self.account_no = account_no
#    def get_account_number(self):
#        """Get account number"""
#        return self.account_no
#    def save(self):  ### Violation class Account is related only to account not DB
#      """Save account number into DB"""
#      pass

# We can use Facade pattern to fix this, we will create another class that handle DB
class AccountDB:
   """Account DB management class """

   def get_account_number(self, _id):
       """Get account number"""
       pass

   def account_save(self, obj):
       """Save account number into DB"""
       pass


class Account:
   """Demo bank account class """

   def __init__(self, account_no: str):
       self.account_no = account_no
       self._db = AccountDB()

   def get_account_number(self):
       """Get account number"""
       return self.account_no

   def get(self, _id):
       """
       :param _id:
       :return:
       """
       return self._db.get_account_number(_id=_id)

   def save(self):
       """account save"""
       self._db.account_save(obj=self)

# Open and Closed Principle(OCP):
# Software entities (classes, function, module) open for extension,
# but not for modification (or closed for modification)

# Violation of this principle:
# class Discount:
#    """Demo customer discount class"""
#    def __init__(self, customer, price):
#        self.customer = customer
#        self.price = price
#    def give_discount(self):
#        """A discount method"""
#        if self.customer == 'normal':
#            return self.price * 0.2
#        elif self.customer == 'vip':
#            return self.price * 0.4

# Now we see the problem any change for example special customer that has other discount will be added
# in the implementation:
#     def give_discount(self):
#        """A discount method"""
#        if self.customer == 'normal':
#            return self.price * 0.2
#        elif self.customer == 'vip':
#            return self.price * 0.4
#        elif self.customer ==  'supvip':
#            return self.price * 0.8

class Discount:
   """Demo customer discount class"""
   def __init__(self, customer, price):
       self.customer = customer
       self.price = price
   def get_discount(self):
       """A discount method"""
       return self.price * 0.2
class VIPDiscount(Discount):
   """Demo VIP customer discount class"""
   def get_discount(self):
       """A discount method"""
       return super().get_discount() * 2
class SuperVIPDiscount(VIPDiscount):
   """Demo super vip customer discount class"""
   def get_discount(self):
       """A discount method"""
       return super().get_discount() * 4

# Liskov Substitution Principle(LSP):
# if S is a subtype of T, then objects of type T may be replaced by objects of type S, without breaking the program.

# Example of Violation of LSP:
# class Vehicle:
#    """A demo Vehicle class"""
#
#    def __init__(self, name: str, speed: float):
#        self.name = name
#        self.speed = speed
#
#    def get_name(self) -> str:
#        """Get vehicle name"""
#        return f"The vehicle name {self.name}"
#
#    def get_speed(self) -> str:
#        """Get vehicle speed"""
#        return f"The vehicle speed {self.speed}"
#
#    def engine(self):
#        """A vehicle engine"""
#        pass
#
#    def start_engine(self):
#        """A vehicle engine start"""
#        self.engine()
#
#
# class Car(Vehicle):
#    """A demo Car Vehicle class"""
#    def start_engine(self):
#        pass
#
#
# class Bicycle(Vehicle):
#    """A demo Bicycle Vehicle class"""
#    def start_engine(self): # Violation - no engine in Bicycle
#        pass

# Example of good use of Liskov principle:
class Vehicle:
   """A demo Vehicle class"""
   def __init__(self, name: str, speed: float):
       self.name = name
       self.speed = speed
   def get_name(self) -> str:
       """Get vehicle name"""
       return f"The vehicle name {self.name}"
   def get_speed(self) -> str:
       """Get vehicle speed"""
       return f"The vehicle speed {self.speed}"
class VehicleWithoutEngine(Vehicle):
   """A demo Vehicle without engine class"""
   def start_moving(self):
      """Moving"""
      raise NotImplemented
class VehicleWithEngine(Vehicle):
   """A demo Vehicle engine class"""
   def engine(self):
      """A vehicle engine"""
      pass
   def start_engine(self):
      """A vehicle engine start"""
      self.engine()
class Car(VehicleWithEngine):
   """A demo Car Vehicle class"""
   def start_engine(self):
       pass
class Bicycle(VehicleWithoutEngine):
   """A demo Bicycle Vehicle class"""
   def start_moving(self):
       pass
# Interface Segregation Principle(ISP):
# Actually, This principle suggests that “A client should not be forced to implement an interface that it does not use”

# Example of Violation of ISP: Shape has methods that are not relevant to all shapes
# class Shape:
#    """A demo shape class"""
#    def draw_circle(self):
#        """Draw a circle"""
#        raise NotImplemented
#    def draw_square(self):
#        """ Draw a square"""
#        raise NotImplemented
# class Circle(Shape):
#     """A demo circle class"""
#    def draw_circle(self):
#        """Draw a circle"""
#        pass
#    def draw_square(self): # Non relevant to Circle
#        """ Draw a square"""
#        pass

# Correct the example:
class Shape:
   """A demo shape class"""
   def draw(self):
      """Draw a shape"""
      raise NotImplemented
class Circle(Shape):
   """A demo circle class"""
   def draw(self):
      """Draw a circle"""
      pass
class Square(Shape):
   """A demo square class"""
   def draw(self):
      """Draw a square"""
      pass

# Dependency Inversion Principle(DIP):
# This principle suggests that below two points.
# a. High-level modules should not depend on low-level modules. Both should depend on abstractions.
# b. Abstractions should not depend on details. Details should depend on abstractions.

# Violation of DIP:
# class BackendDeveloper:
#     """This is a low-level module"""
#     @staticmethod
#     def python():
#         print("Writing Python code")
# class FrontendDeveloper:
#     """This is a low-level module"""
#     @staticmethod
#     def javascript():
#         print("Writing JavaScript code")
# class Project:
#     """This is a high-level module"""
#     def __init__(self):
#         self.backend = BackendDeveloper()
#         self.frontend = FrontendDeveloper()
#     def develop(self):
#         self.backend.python()
#         self.frontend.javascript()
#         return "Develop codebase"
# project = Project()
# print(project.develop())

# The project class is a high-level module and backend & frontend are the low-level modules.
# In this example, we found that the high-level module depends on the low-level module.
# Hence this example are violated the Dependency Inversion Principle

# Solution according to DIP: Using static methods as private so high level is not exposed to low level implementations
class BackendDeveloper:
   """This is a low-level module"""
   def develop(self):
       self.__python_code()
   @staticmethod
   def __python_code():
       print("Writing Python code")
class FrontendDeveloper:
   """This is a low-level module"""
   def develop(self):
       self.__javascript()
   @staticmethod
   def __javascript():
       print("Writing JavaScript code")
class Developers:
   """An Abstract module"""
   def __init__(self):
       self.backend = BackendDeveloper()
       self.frontend = FrontendDeveloper()
   def develop(self):
       self.backend.develop()
       self.frontend.develop()
class Project:
   """This is a high-level module"""
   def __init__(self):
       self.__developers = Developers()
   def develops(self):
       return self.__developers.develop()
project = Project()
print(project.develops())