from itertools import permutations
s = input()
w, n = s.split()

perms = sorted(["".join(i) for i in list(permutations(w, int(n)))])
for i in perms:
    print(i)

