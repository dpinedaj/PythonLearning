def solution(A):
    # write your code in Python 3.6
    for i in range(min(A), max(A) + 1):
        if i not in A and i > 0:
            return i
    return max(max(A) + 1, 1)
