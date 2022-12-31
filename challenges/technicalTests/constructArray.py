def solution(A):
    new_arr = []

    def iter_array(val, prev_arr):
        if val not in range(0, len(A)):
            return
        v = prev_arr[val]
        if v == "x":
            return
        new_arr.append(v)
        prev_arr[val] = "x"
        iter_array(v, prev_arr)

    iter_array(0, A)
    return new_arr


test = [1, 4, -1, 3, 2]
print(solution(test))
