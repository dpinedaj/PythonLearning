# first element must be 1
# For all other elements the diference between adjacent integers must not be
# greater than 1, for 1 <= i < n, arr[i] - arr[i-1] <= 1


#%%
arr = [1, 3, 2, 2]


sorted_arr = sorted(arr)  # [1, 2, 2, 3]
sorted_arr[0] = 1
for i in range(len(sorted_arr) - 1):
    diff = sorted_arr[i + 1] - sorted_arr[i]
    sorted_arr[i + 1] = sorted_arr[i] + 1 if diff > 1 else sorted_arr[i + 1]


# %%
