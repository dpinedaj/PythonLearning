

def BuscaPareseImpares():

	T=int(input())
	n=0
	p=[""]*T
	i=[""]*T
	for task in range(T):
		S=str(input())
		for letra in S:
			if S.index(letra)==0 or S.index(letra)%2==0:
				p[n]+=letra
			else:
				i[n]+=letra
		n+=1
	for par in p:
		print(par,end="")
	for impar in i:
		print(impar,end="")






def VersionOptimizada():
	for N in range(int(input())):
		S = input()
		print(S[::2], S[1::2])



VersionOptimizada()