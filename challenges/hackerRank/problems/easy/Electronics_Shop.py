# * b es la plata que puede gastar, n y m son cantidad de teclados y mouse


def getmoneySpent(keyboards, drivers, b):
    count = 0
    e = b
    for i in range(n):
        for j in range(m):
            c = keyboards[i] + drives[j]
            if c <= b:
                count += 1
                d = b - c
                if d < e:
                    e = d
                    s = b - e

    if count == 0:
        s = -1

    return s


bnm = input().split()

b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

moneySpent = getmoneySpent(keyboards, drivers, b)

print(moneySpent)
