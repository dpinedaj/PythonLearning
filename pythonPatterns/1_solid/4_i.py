# Interface Segregation Principle

from abc import abstractmethod


# Violate approach


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    # Methods fax and scan would be a problem because the OldFashionedPrinter
    # will not fax or scan
    def fax(self, document):
        pass

    def scan(self, document):
        pass


# Better approach


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner, Fax):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner, fax):
        self.print = printer
        self.scanner = scanner
        self.fax = fax

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)

    def fax(self, document):
        self.fax.fax(document)
