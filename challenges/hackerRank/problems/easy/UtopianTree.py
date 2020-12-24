

def utopianTree(n):
    alt = 1
    for i in range(1,n+1):
        if i%2!=0:
            alt = alt*2
        else:
            alt+=1
    return alt

if __name__ == '__main__':
   

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(result+"\n")