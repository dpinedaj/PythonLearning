# Prototype Pattern
# ------------------------------
# - Complicated Objects (e.g. cars) aren't designed from scratch
# - - They reiterate existing designs
# - An existing (Partially or fully constructed) design is a Prototype
# - We make a copy (clone) the prototype and customize it
# - - Requires 'deep copy' support
# - We make the cloning convenient (e.g, via a Factory)
# ###############################
# Definition:
# A partially or fully initialized object that you copy (clone)
# and make use of.


from copy import deepcopy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


john = Person("John", Address("123 London Road", "London", "UK"))
print(john)

# If Jane lives with John, this should be possible, but it doesn't
print("\nWrong way:")
jane = john
jane.name = 'Jane'
print(jane)
print(john)


# A good way is using deepcopy
print("\nWith deepcopy")
john = Person("John", Address("123 London Road", "London", "UK"))
jane = deepcopy(john)
jane.name = "Jane"
print(john)
print(jane)


###############################
# Prototype Factory
