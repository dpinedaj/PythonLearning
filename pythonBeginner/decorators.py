def register(active=True):
    def wrap(func):
        def wrapper():
            print("Calling ", func.__name__, " decorator param", active)
            if active:
                func()
                print("Called ", func.__name__)
            else:
                print("Skipped ", func.__name__)

        return wrapper

    return wrap


# METHODS DECORATORS
def trace(method):
    def method_wrapper(self, x, y):
        print("Calling", method, "with", x, y)
        method(self, x, y)
        print("Called", method, "with", x, y)

    return method_wrapper


# CLASS DECORATORS
def singleton(cls):
    print("In singleton for: ", cls)
    instance = None

    def get_instance():
        nonlocal instance
        if instance is None:
            instance = cls()
        return instance

    return get_instance


@singleton
class Service(object):
    def print_it(self):
        print(self)
