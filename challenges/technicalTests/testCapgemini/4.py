myArray = [1, 2, -1, 1, 0, 1, 2, -1, -1, -2]


# Vertical - horizontal

k_pos = [0, 0]

for i in range(0, len(myArray), 2):
    p = 1
    for pos in range(i, i+2):
        new_pos = k_pos[p] + myArray[pos]
        k_pos[p] = new_pos if new_pos <= 3 else k_pos[p]
        
        p = 0
    
for i in range(4):
    for j in range(4):
        if i == k_pos[0] and j == k_pos[1]:
            print("X", end="")
        else:
            print("O", end="")

    print("")
