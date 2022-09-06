# Proxy
# If for example you are calling foo.Bar()
# That assumes that foo is in the same process as Bar()
# What if later on, you qwant to put all Foo-related operations into a separate process
# - Can you avoid changing your code?
# Proxy to the rescue!
# - same interface, entirely different behavior
# This is called a communication proxy
# - other types: logging, virtual, guarding, ...


# Definition:
# A class that functions as an interface to a particular resource
# That resource may be remote, expensive to contruct,
# or may require logging or some other added funcionality


# * Protection Proxy
class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")


class CarProxy:
    # Protection Proxy
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print("Driver too young")


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    driver = Driver("John", 20)
    car = CarProxy(driver)
    car.drive()


# * Virtual Proxy


class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def drae(self):
        print(f"Drawing image {self.filename}")


class LazyBitmap:
    # Virtual Proxy
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)

        self._bitmap.draw()


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


if __name__ == "__main__":
    bmp = LazyBitmap("facepalm.jpg")
    draw_image(bmp)


# Exercise


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return "drinking"

    def drive(self):
        return "driving"

    def drink_and_drive(self):
        return "driving while drunk"


class ResponsiblePerson:
    def __init__(self, person):
        self._person = person

    def drive(self):
        if self._person.age >= 16:
            return self._person.drive()
        else:
            return "too young"

    def drink(self):
        if self._person.age >= 18:
            return self._person.drink()
        else:
            return "too young"

    def drink_and_drive(self):
        return "dead"
