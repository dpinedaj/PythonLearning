from itertools import groupby

s = "1222311"

res = ["({}, {})".format(len(list(j)), i) for i, j in groupby(s)]
res = " ".join(res)
print(res)  # (1, 1) (3, 2) (1, 3) (2, 1)
