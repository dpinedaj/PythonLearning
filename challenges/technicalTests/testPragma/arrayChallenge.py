

arr = [2, 4, 3]
n = len(arr)
result = [0]
for i in range(1, n):
    c = 0
    for j in range(i):
        diff = arr[i] - arr[j]
        val = abs(diff) if diff > 0 else -1 * abs(diff)
        c += val
    result.append(c)

return result
