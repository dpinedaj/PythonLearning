"""
Multi process limited process in one second, reduced to floor (ability/2)
What is the minimun time required to schedule all the processes in the system



"""


""" example:
n = 5 ( number of precessors and size of ability[])
ability = [3, 1, 7, 2, 4]
processes = 15



"""
#%%
ability = [2, 1, 5, 3, 1]
processes = 17

n = 0
while processes > 0:
    option = max(ability)
    processes -= option
    ability[ability.index(option)] = option // 2
    n += 1

print(n) # 9
