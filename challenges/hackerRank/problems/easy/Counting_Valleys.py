#%%


def countingValleys(n, s):
    valle = 0
    nivel = 0
    for i, j in zip(s, range(n)):
        if (nivel == (-1)) & (i == "U"):
            valle += 1

        if i == "D":
            nivel -= 1
        elif i == "U":
            nivel += 1

    return valle


n = 12
s = "DDUUDDUDUUUD"

print(countingValleys(n, s))
