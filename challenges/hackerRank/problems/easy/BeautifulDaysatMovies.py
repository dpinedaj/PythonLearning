

def beautifulDays(i, j, k):
    count=0
    for num in range(i,j+1):
        if abs(num-int(str(num)[::-1]))%k ==0:
            count+=1

    return count




if __name__ == '__main__':
    

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)