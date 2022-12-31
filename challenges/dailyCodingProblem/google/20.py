"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with 
the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


def problem20(arr1, arr2):
    return list(set(enumerate(arr1)).intersection(set(enumerate(arr2))))[0][1]


problem20([1, 2, 3, 4], [4, 5, 3, 1])
