# Reference: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

#%%
def organizingContainers(container):
    n = len(container)
    cant_diff = [
        sum([container[k][j] for k in range(n) if k != j])
        == sum([container[j][k] for k in range(n) if k != j])
        for j in range(n)
    ]

    if all(cant_diff):
        print("Possible")
    else:
        print("Impossible")


cont1 = [[1, 1], [1, 2]]

cont2 = [[0, 2, 2], [1, 3, 1], [1, 3, 4]]

organizingContainers(cont2)
