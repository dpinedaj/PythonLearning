from itertools import combinations_with_replacement

for c in list(combinations_with_replacement('12345', 2)):
    print("".join(c))

