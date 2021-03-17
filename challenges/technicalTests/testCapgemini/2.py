n = 5
opts = ["X", "_"]
ne = 0
for i in range(n):
    for j in range(n):
        p = opts[ne]
        print(p, end="")
        ne = not ne
    print("")
        