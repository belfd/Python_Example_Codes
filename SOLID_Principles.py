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
from abc import abstractmethod


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

### Another example of violation Single Responsibility:
# class Album:
#     def __init__(self, name, artist, songs) -> None:
#         self.name = name
#         self.artist = artist
#         self.songs = songs
#     def add_song(self, song):
#         self.songs.append(song)
#     def remove_song(self, song):
#         self.songs.remove(song)
#     def __str__(self) -> str:
#         return f"Album {self.name} by {self.artist}\nTracklist:\n{self.songs}"
#     #### breaks the SRP ###
#     def search_album_by_artist(self):
#         """ Searching the database for other albums by same artist """
#         pass

### Fixed version:
# instead, create 'AlbumBrowser' class dedicated for browsing DBs:
class AlbumBrowser:
    """ Class for browsing the Albums database"""

    def search_album_by_artist(self, albums, artist):
        pass

    def search_album_starting_with_letter(self, albums, letter):
        pass


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

### Another example of OCP:
class Album:
    def __init__(self, name, artist, songs, genre):
        self.name = name
        self.artist = artist
        self.songs = songs
        self.genre = genre
# #before
# class AlbumBrowser:
#     def search_album_by_artist(self, albums, artist):
#         return [album for album in albums if album.artist == artist]
#     def search_album_by_genre(self, albums, genre):
#         return [album for album in albums if album.genre == genre]
### Now what happens if I want to search by artist and genre?
# What if I add release year? I will have to write new function every time - problem!

### Instead, I should define a base class with a common interface for my specification,
# and then define subclasses for each type of specification that inherits this interface from the base class:
# after
class SearchBy:
    def is_matched(self, album):
        pass


class SearchByGenre(SearchBy):
    def __init__(self, genre):
        self.genre = genre

    def is_matched(self, album):
        return album.genre == self.genre


class SearchByArtist(SearchBy):
    def __init__(self, artist):
        self.artist = artist

    def is_matched(self, album):
        return album.artist == self.artist


class AlbumBrowser:
    def browse(self, albums, searchby):
        return [album for album in albums if searchby.is_matched(album)]

# But what about multiple criteria? This allows use to join browsing criteria to be joined together by &:
# add __and__:
class SearchBy:
    def is_matched(self, album):
        pass

    def __and__(self, other):
        return AndSearchBy(self, other)


class AndSearchBy(SearchBy):
    def __init__(self, searchby1, searchby2):
        self.searchby1 = searchby1
        self.searchby2 = searchby2

    def is_matched(self, album):
        return self.searchby1.is_matched(album) and self.searchby2.is_matched(album)

# EXample to use & :
LAWoman = Album(
    name="L.A. Woman",
    artist="The Doors",
    songs=["Riders on the Storm"],
    genre="Rock",
)
Trash = Album(
    name="Trash",
    artist="Alice Cooper",
    songs=["Poison"],
    genre="Rock",
)
albums = [LAWoman, Trash]
# this creates the AndSearchBy object
my_search_criteria = SearchByGenre(genre="Rock") & SearchByArtist(
    artist="The Doors"
)
browser = AlbumBrowser()
assert browser.browse(albums=albums, searchby=my_search_criteria) == [LAWoman]
# yay we found our album


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
# Actually, This principle suggests that:
# “A client should not be forced to implement an interface that it does not use”

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

# Another violation of ISP:
# class PlaySongs:
#     def __init__(self, title):
#         self.title = title
#     def play_drums(self):
#         print("Ba-dum ts")
#     def play_guitar(self):
#         print("*Soul-moving guitar solo*")
#     def sing_lyrics(self):
#         print("NaNaNaNa")
# # This class is fine, just changing the guitar and lyrics
# class PlayRockSongs(PlaySongs):
#     def play_guitar(self):
#         print("*Very metal guitar solo*")
#     def sing_lyrics(self):
#         print("I wanna rock and roll all night")
# # This breaks the ISP, we don't have lyrics
# class PlayInstrumentalSongs(PlaySongs):
#     def sing_lyrics(self):
#         raise Exception("No lyrics for instrumental songs")

# Instead, we could have a class for the singing and the music separately
# (assuming guitar and drums always happen together in our case,
# otherwise we need to split them up even more, perhaps by instrument.)
# This way, we only have the interfaces we need, we cannot call sing lyrics on instrumental songs.

# from abc import ABCMeta

class PlaySongsLyrics:
    @abstractmethod
    def sing_lyrics(self, title):
        pass

class PlaySongsMusic:
    @abstractmethod
    def play_guitar(self, title):
        pass
    @abstractmethod
    def play_drums(self, title):
        pass

class PlayInstrumentalSong(PlaySongsMusic):
    def play_drums(self, title):
        print("Ba-dum ts")
    def play_guitar(self, title):
        print("*Soul-moving guitar solo*")

class PlayRockSong(PlaySongsMusic, PlaySongsLyrics):
    def play_guitar(self):
        print("*Very metal guitar solo*")
    def sing_lyrics(self):
        print("I wanna rock and roll all night")
    def play_drums(self, title):
        print("Ba-dum ts")

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

# Another Violation of DIP:
# ViewRockAlbums explicitly depends on the fact that albums are stored in a tuple in a certain order inside AlbumStore.
# It should have no knowledge of the internal structure of Albumstore.
# Now if we change the ordering in the tuples in the album, our code would break.

# class AlbumStore:
#     albums = []
#     def add_album(self, name, artist, genre):
#         self.albums.append((name, artist, genre))
#
# class ViewRockAlbums:
#     def __init__(self, album_store):
#         for album in album_store.albums:
#             if album[2] == "Rock":
#                 print(f"We have {album[0]} in store.")

# Instead, we need to add an abstract interface to AlbumStore to hide the details,
# that can be called by other classes. This should be done as in the example in the Open-Closed Principle,
# but assuming we don’t care about filtering by anything else, I’ll just add a filter_by_genre method.
# Now if we had another type of AlbumStore, that decides to store the album differently,
# it would need to implement the same interface for filter_by_genre to make ViewRockAlbums work.

class GeneralAlbumStore:
    @abstractmethod
    def filter_by_genre(self, genre):
        pass
class MyAlbumStore(GeneralAlbumStore):
    albums = []
    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))
    def filter_by_genre(self, genre):
        if albums[2] == "Rock":
            yield albums[0]
class ViewRockAlbums:
    def __init__(self, album_store):
        for album_name in album_store.filter_by_genre("Rock"):
            print(f"We have {album_name} in store.")

