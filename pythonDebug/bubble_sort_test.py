import unittest
from bubbleSort import bubbleSort as bs


class Test_TestCannedValue(unittest.TestCase):
    ##Test Driven development
    # To acticate debug unittest, in command pallete execute:
    # Python: Configure Test

    def test_simple(self):
        testList = [4, 5, 2, 1]
        expectedList = testList.copy()

        expectedList.sort()  ##If i skip this line, the test go wrong
        actualList = bs(testList)
        self.assertEqual(actualList, expectedList)

    def test_empty(self):
        testList = []
        expectedList = testList.copy()
        expectedList.sort()
        actualList = bs(testList)
        self.assertEqual(actualList, expectedList)

    def test_presorted(self):
        testList = [1, 2, 3, 4]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = bs(testList)
        self.assertEqual(actualList, expectedList)

    def test_negative(self):
        testList = [-4, -3, -2, -1]
        expectedList = testList.copy()
        expectedList.sort()
        actualList = bs(testList)
        self.assertEqual(actualList, expectedList)
