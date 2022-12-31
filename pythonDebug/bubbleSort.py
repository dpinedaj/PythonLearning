def bubbleSort(l: list, reverse: bool = False) -> list:
    length = len(l)
    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    if reverse:
        l.reverse()
    return l
