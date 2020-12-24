

def pickingNumbers(a):
    maximum=0
    for i in a:
        c=a.count(i)
        d=a.count(i-1)
        c=c+d
        if c > maximum:
            maximum=c
    return(maximum)
	

	
	

if __name__ == '__main__':
   
	n = int(input().strip())

	a = list(map(int, input().rstrip().split()))

	result = pickingNumbers(a)

	