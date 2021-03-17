"""
4 buttons U, D, L, R

"""


s = "URDR"

v = 0
h = 0
for l in s:
    if l == 'U': v += 1
    elif l == 'D': v -= 1
    elif l == 'R': h += 1
    elif l == 'L': h -= 1

total = abs(v) + abs(h)
diff = len(s) - total

print(diff)

