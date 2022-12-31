from math import ceil, floor

# Complete the repeatedString function below.
def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[: n % len(s)].count("a")


s = "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq"
n = 549382313570

# 16481469408

print(repeatedString(s, n))
