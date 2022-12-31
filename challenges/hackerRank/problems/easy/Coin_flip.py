# Inserta el número de casos#
T = int(input())

# En cada caso Inserta el número de juegos#
for i in range(T):
    G = int(input())

    ###Empieza Cada Juego##
    sln = []
    for j in range(G):

        IQN = input().split()

        I = int(IQN[0])
        N = int(IQN[1])
        Q = int(IQN[2])

        if N % 2 != 0 and I + Q == 1:
            sln.append((N // 2) + 1)

        else:
            sln.append(N // 2)

for k in sln:
    print(k)


## T are the test cases##
## in each T case are G denoting the number of games##

### I N Q,
##I=1 all are head, I=0 all are tail
### N denotes the number of coins
## Q=1 is needed the heads, Q=2 is needed the Tails
