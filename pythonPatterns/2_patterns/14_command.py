# Command
# Ordinary statements are perishable
# - Cannot undo member assignment
# - Cannot directly serialize a sequence of actions (calls)

# Want an object that represents an operation
# - e.g person should change its age to value 22 and you want to record the changes
# - e.g car should do explode() and you want to record who asked to explode the car

# Uses: GUI commands, multi-level undo/redo, macro recording and more.


# Definition: An object which represents an instruction to perform a particular action
# Contains all the information necessary for the action to be taken.

from abc import ABC
from enum import Enum
import unittest


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, balance = {self.balance}")
            return True
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


# if __name__ == "__main__":
#     ba = BankAccount()
#     cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
#     cmd.invoke()
#     print(f"After $100 deposit: {ba}")

#     cmd.undo()
#     print(f"$100 deposit undone: {ba}")

#     illegal_cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)

#     illegal_cmd.invoke()
#     print(f"After impossible withdrawal: {ba}")
#     illegal_cmd.undo()
#     print(f"After undo: {ba}")


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()

        deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
        deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)

        composite = CompositeBankAccountCommand([deposit1, deposit2])
        composite.invoke()
        print(ba)
        composite.undo()
        print(ba)


if __name__ == "__main__":
    unittest.main()
