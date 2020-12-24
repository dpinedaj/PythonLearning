def angryProfessor(k, a):
    answer="YES"
    count=0
    for i in a:
        if i <=0:
            count+=1
    if count >=k:
        answer="NO"

    return answer



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

      