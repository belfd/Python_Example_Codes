'''
Singleton Pattern
This pattern involves a single class which is responsible for the creation of an object while making sure that it is
the only one created. This class provides a way to access it, which can be accessed directly without the need for
instantiation of the class object. The most common reason for this is to control access to some shared resource.
As an example, the pattern may come in handy when doing things like a database driver. If you are over on the client,
it comes in handy when you want to know the current state of the app that is in a Singleton.
The advantage is that you can go and get to that data anytime that you want.
The disadvantage is that once you have added that constraint,
instead of everybody being able to go and access it directly, you have got narrow down to whomever the consumers are.
This pattern is one of the most misused. Singletons are for use when a class must have exactly one instance,
no more, no less. Some developers frequently use Singletons in an attempt to replace global variables.
For intents and purposes, a Singleton is a global variable, in that it does not do away with the global variable,
it simply renames it.
The use of a Singleton is uncalled for if it is simpler to pass an object resource as a reference to
the objects that need it rather than letting objects access it globally.
You, therefore, have to know and make sure that you are using it the right way and at the right time.

Facade Pattern
Simply put, this is a structural design pattern that provides a simplified interface to a library,
a framework, or any other complex set of classes. A facade in the real world would be the front of a building,
which it hides all of the internal mechanics of the building. These would be the insulation, the rooms, the plumbing,
the wiring e.t.c. The facade pattern gives you the ability to put a nice external veneer on your app.
Take a compiler as an example. It has a parser, a lexical analyzer, a tokenizer,
and all kinds of fun stuff that no consumer sees.
The advantage of using this pattern is that it gives your consumer a good interface.
You can also choose to allow your consumers into the internals if you wish.
One of the things to watch out for is the possibility of an oversimplification.
You may end up oversimplifying the interface of that compiler that it is no longer usable or valuable.
Another thing is over verticalization. You may end up creating a facade that is so specific to
a single use case that it is no longer generalized enough to be generally useful.

Bridge Pattern
This design pattern that lets you split a large class or a set of closely related classes into
two separate hierarchies which can be developed independently of each other.
Another way of explaining this is progressively adding functionality while separating major differences using
abstract classes. A problem that requires this pattern occurs because sometimes developers try to extend
subclasses in two independent dimensions. That is a common issue with class inheritance.
The Bridge pattern attempts to solve this problem by switching from Inheritance to the object composition.
This pattern involves an interface that acts as a bridge between the abstraction classes and
the implementation classes. In a development example, the bridge interface would be something like an API.
This approach simplifies code maintenance and minimizes the risk of breaking existing code.

Strategy Pattern
This design pattern lets you define a family of algorithms, then put each of them into a separate class,
and make their objects interchangeable. Consider a scenario where you have
a code that is going to go and find customers, filter through them and then send out notifications to them via
email and text. You can use the strategy pattern to significantly clean this up by taking the mechanics of getting
access to the customer records, sending out the messages and emails, and then creating that as an infrastructure layer.
Factor out the filtering of those customers into one strategy, which is the strategy that helps you find the target
customers you want. Take the notification strategy as a different strategy which helps to decide when,
where and how you want to contact those customers. You can then use that library or that system in a whole
bunch of different scenarios, and it becomes much less stressful.

One thing you got to look out for on this is to make sure that you have decent default strategies.
So in the case of our refactoring, we go and take the existing logic around the customer filtering and
the customer send-outs and turn those into the default strategies, which people can extend later.
Otherwise, you get a system whereby default, you are asked to do a lot up front, and no customer wants to do that.

Observer Pattern
This pattern is the most popular by far because it is almost everywhere.
It allows for loose coupling between the publisher, that is creating events and the subscriber or subscribers that
are listening for those events, and you can use it anywhere. The con on this particular pattern is that you can go
overboard with it. If everything is communicating by events, you can get into nasty event loops,
which make the code hard to debug and it just gets chaotic.

There are a couple of solves for this. One, do not use the same message bus for everything,
have a specific purpose for each message bus. Two, keep these systems localized.
If you are on the client and you have got a button, and it is an admitting and event, you are good to go.
You do not need to go beyond that.
So again, as with all, all of these patterns, use them wisely but use them because most people understand
those systems when they see them. For people, who are interested in learning the design patterns,
these are just 5 to get started with as you get your feet wet. There are more patterns out there,
and many tutorials online that can help you get a good grasp of the different ones.
Do not just learn or read about the different patterns, practice them at least in small projects.
The ability to see where specific concepts might be useful in larger codebases comes only with practice,
experience, and time. Do not be in a hurry to get as many as you can under your tool belt.
If you do not get a pattern instantaneously, look for different explanations and tutorials online,
and you will get the hang of it after investing time to research.

'''


### FACTORY METHOD ###
class Bicycle:
    def __init__(self, factory):
        self.tires = factory().add_tires()
        self.frame = factory().add_frame()
class GenericFactory:
    def add_tires(self):
        return GenericTires()
    def add_frame(self):
        return GenericFrame()
class MountainFactory:
    def add_tires(self):
        return RuggedTires()
    def add_frame(self):
        return SturdyFrame()
class RoadFactory:
    def add_tires(self):
        return RoadTires()
    def add_frame(self):
        return LightFrame()
class GenericTires:
    def part_type(self):
        return 'generic_tires'
class RuggedTires:
    def part_type(self):
        return 'rugged_tires'
class RoadTires:
    def part_type(self):
        return 'road_tires'
class GenericFrame:
    def part_type(self):
        return 'generic_frame'
class SturdyFrame:
    def part_type(self):
        return 'sturdy_frame'
class LightFrame:
    def part_type(self):
        return 'light_frame'
bike = Bicycle(GenericFactory)
print(bike.tires.part_type()) #output: generic_tires
print(bike.frame.part_type()) #output: generic_frame
mountain_bike = Bicycle(MountainFactory)
print(mountain_bike.tires.part_type()) #output: rugged_tires
print(mountain_bike.frame.part_type()) #output: sturdy_frame
road_bike = Bicycle(RoadFactory)
print(road_bike.tires.part_type()) #output: road_tires
print(road_bike.frame.part_type()) #output: light_frame