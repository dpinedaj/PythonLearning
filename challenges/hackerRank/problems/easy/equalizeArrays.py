def equalize_array(arr: list):
    return len(arr) - max((arr.count(i) for i in set(arr)))



print(equalize_array([1, 2, 2, 3])) # 2

print(equalize_array([3, 3, 2, 1, 3, 6, 8])) # 4

