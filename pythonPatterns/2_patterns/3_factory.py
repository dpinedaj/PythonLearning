# Factory pattern
# --------------------------------
# - When the object creation logic becomes too convoluted
# - Initializer usually is not descriptive
# - - Cannot overload the constructor
# - - Can turn into 'optional parameter hell'
# - Wholesale object creation (non-piecewise, unlike Builder) can be
# outsourced to
# - - A separate method (Factory Method)
# - - That may exist in a separate class (Factory)
# - - Can create hierarchy of factories with Abstract Factory Design Pattern
# --------------------------------
# Fcatory is a component responsible solely for the wholesale (not piecewise)
# creation of objects.
################################

# Factory Method
from abc import ABC
from cmath import cos, sin
from enum import Enum, auto
from os import stat


class CoorinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


# This approach can works but violates the open - close principle
class Point:
    def __init__(self, a, b, system=CoorinateSystem.CARTESIAN):
        if system == CoorinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoorinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)


# This way more explicit creation is called the Factory method
# with the definition of the constructor in the static methods
class Point2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point2(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point2(rho * cos(theta), rho * sin(theta))


p1 = Point2.new_cartesian_point(1, 2)
p2 = Point2.new_polar_point(1, 2)

# Factory class is the same idea but encapsulated in a class


class PointFactory:
    def new_cartesian_point(self, x, y):
        return Point2(x, y)

    def new_polar_point(self, rho, theta):
        return Point2(rho * cos(theta), rho * sin(theta))


# Abstract Factory

class HotDrink(ABC):
    def consume(self):
        ...


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious")


class Coffe(HotDrink):
    def consume(self):
        print("This coffee is delicious")


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        ...


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Put in tea bag, boil water,"
              f" pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Grind some beans, boil water,"
              f" pour {amount}ml, enjoy!")
        return Coffe()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name.capitalize()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((factory_name, factory_instance))

    def make_drink(self):
        print("Available drinks:")
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink (0-{len(self.factories)-1}: ")
        idx = int(s)
        s = input("Specify amount: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


# Exercise
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    current_id = 0

    def create_person(self, name):
        person = Person(self.current_id, name)
        self.current_id += 1
        return person
