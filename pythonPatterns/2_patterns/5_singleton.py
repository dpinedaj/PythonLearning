# When discussing which patterns to drop, we found that we still love them all
# (Not really, I'm in favor of dropping Singleton. Its use is almost always a design smell.)

################################
# For some components it only makes sense to have one in the system
# - Database repository
# - Object Factory (This usually is stateless)
# E.g., the initializer call is expensive
# - We only do it once
# - We provide everyone with the same instance
################################
# Want to prevent anyone creating additional copies
# Need to take care of lazy instantiation

import unittest


# Singleton Allocator

class Database:
    _instance = None

    def __init__(self):
        # The init method is still called by each object you initialize
        # we must be careful with this because can initialize multiple
        # objects with the same reference
        print("Loading a database from file")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


# Singleton Decorator
# This can solve the initializer problem

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class Database:
    def __init__(self):
        print("Loading database")


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


# Singleton Metaclass
# similar implementation than decorator

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls)\
                .__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print("Loading Database")


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


# Monostate
# Will share attributes and if one of them changes, all changes
class CEO:
    __shared_state = {
        "name": "Steve",
        "age": 55,
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is {self.age} years old"


if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)
    ceo2 = CEO()
    ceo2.age = 77
    print(ceo1)
    print(ceo2)


class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self) -> str:
        return f"{self.name} manages ${self.money_managed}bn"


if __name__ == '__main__':
    cfo1 = CFO()
    print(cfo1)
    cfo2 = CFO()
    cfo2.name = "Jhon"
    cfo1.money_managed = 123
    print(cfo1)
    print(cfo2)


# Testability

class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        f = open('capitals.txt', 'r')
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i + 1].strip())
        f.close()


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]
        return result


class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db = Database()
        db2 = Database()
        self.assertEqual(db, db2)

    def test_singleton_total_population(self):
        """ This tests on a live database :( """
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        self.assertEqual(tp, 17500000 + 17400000)  # what if these change?

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(
            crf.total_population(['alpha', 'beta']),
            3
        )


if __name__ == '__main__':
    unittest.main()
