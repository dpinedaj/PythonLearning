reference= "https://www.hackerrank.com/challenges/recursive-digit-sum/problem?isFullScreen=true"

#%%
def superDigit(n, k):
    # Write your code here
    def compute(x: str):
        if len(x) == 1:
            return x
        else:
            newX = str(sum(int(i) for i in x))
            return compute(newX)
    return compute(str(n)*k)


print(superDigit(148, 3))
# %%
