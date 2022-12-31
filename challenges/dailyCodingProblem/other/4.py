"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer 
in linear time and constant space. 
In other words, find the lowest positive integer that does not exist 
in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""


def problem4(array: list) -> int:
    new_array = [
        i
        for i in list(set(list(range(min(array), max(array) + 1))) - set(array))
        if i > 0
    ]
    return new_array[0] if len(new_array) > 0 else max(array) + 1


assert problem4([3, 4, -1, 1]) == 2
assert problem4([1, 2, 0]) == 3
