def countChange(money, coins):
    if (money < 0) or (len(coins) == 0):
        return 0
    elif money == 0:
        return 1
    else:
        return countChange(money - coins[0], coins) + countChange(money, coins[1::])


def pascal(c, r):
    if (c == 0) or (c == r):
        return 1
    else:
        return pascal(c - 1, r - 1) + pascal(c, r - 1)


money = 4
coins = [1, 2]

print(countChange(money, coins))

for row in range(11):
    for col in range(row):
        print(pascal(col + 1, row), end=" ")
    print("\n")
