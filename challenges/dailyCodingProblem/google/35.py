"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array so that all the Rs come first, the Gs come second, 
and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def problem35(arr: list) -> list:
    return sorted(arr, key=lambda x: {"R": 1, "G": 2, "B": 3}[x])


arr = ["G", "B", "R", "R", "B", "R", "G"]

print(problem35(arr))


def problem35(arr: list) -> list:
    for i in range(1, len(arr) - 1):
        prev = arr[i - 1]
        curr = arr[i]
        foll = arr[i + 1]
        if curr == "R" and prev in ("G", "B"):
            arr[i - 1] = curr
            arr[i] = prev
    return arr


arr = ["G", "B", "R", "R", "B", "R", "G"]

print(problem35(arr))


arr = ["G", "B", "R", "R", "B", "R", "G"]
print(list(reversed(sorted(arr))))
