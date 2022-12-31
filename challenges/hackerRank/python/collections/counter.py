from collections import Counter

n = 10
s = "2 3 4 5 6 8 7 6 5 18"
c = 6
cs = ["6 55", "6 45", "6 55", "4 40", "18 60", "10 50"]


sl = Counter(s.split())
items = [[i, j] for i, j in sl.items()]
cust = [[i.split()[0], int(i.split()[1])] for i in cs]

result = 0

for c in cust:
    for it in items:
        if (c[0] == it[0]) and (it[1] > 0):
            it[1] -= 1
            result += c[1]

print(result)
