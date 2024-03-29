def move_queen(n, updated_row, updated_col, r, c, obstacles):
    p = 0
    while True:
        r = updated_row(r)
        c = updated_col(c)
        key = (r - 1) * n + c
        if (c < 1 or c > n or r < 1 or r > n) or (key in obstacles):
            return p
        p += 1


def queensAttack(n, k, r_q, c_q, obs):
    obstacles = {}
    for b in obs:
        obstacles[(b[0] - 1) * n + b[1]] = None

    p = 0
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [0, -1, 1, 1, -1, 0, 1, -1]

    for i in range(8):
        p += move_queen(
            n, (lambda r: r + dr[i]), (lambda c: c + dc[i]), r_q, c_q, obstacles
        )

    return p


# Tablero nxn
# k obstáculos
# r_q posición de la fila de la reina
# c_q posición de la columna de lal reina
# obstacles posición de los obstáculos


nk = input().split()
n = int(nk[0])
k = int(nk[1])
r_qC_q = input().split()
r_q = int(r_qC_q[0])
c_q = int(r_qC_q[1])

obstacles = []

for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

result = queensAttack(n, k, r_q, c_q, obstacles)

print(str(result) + "\n")
