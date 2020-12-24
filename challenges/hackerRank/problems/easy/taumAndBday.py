# Reference: https://www.hackerrank.com/challenges/taum-and-bday/problem

def taumBday(b, w, bc, wc, z):
    wc, bc = min(wc, bc + z), min(bc, wc + z)
    return b*bc + w*wc

b, w = 3, 6

bc, wc, z = 9, 1, 1

print(taumBday(b, w, bc, wc, z))

