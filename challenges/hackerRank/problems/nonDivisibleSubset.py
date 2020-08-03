
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    r, o = [0] * k, 0                            # 1
    for i in s:
        r[i % k] += 1                            # 2
    for j in range((k + 2) // 2):                # 3
        if not j or not k % 2 and j == k // 2:
            o += r[j] > 0                        # 4
        else:
            o += max(r[j], r[k - j])             # 5
    return(o)


s = [19, 10, 12, 10, 24, 25, 22 ]
k = 4

print(nonDivisibleSubset(k, s))