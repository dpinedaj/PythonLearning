def meanmedianmode(N,arr):
    suma=0
    for i in arr:
        suma = suma+i
    
    mean= suma/N

    arr.sort()

    if N%2==0:
        a = int((N/2) -1)
        b= int((N/2) +1)
        median = float((arr[a]+arr[b])/2)
    else:
        a=int((N//2)+1)
        median = float(arr[a])
     

    conteo = []
    for j in arr:
        conteo.append(arr.count(j))

    mode = max(conteo)


    return(mean,median,mode)





if __name__ =='__main__':

    N = int(input())
    arr = list(map(int,input().rstrip().split()))

    for i in meanmedianmode(N,arr):

        print ("%.1f\n"%i)