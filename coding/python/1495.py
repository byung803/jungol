A = input()
matrix = [[0 for col in range(A)] for row in range(A)]
i=0
j=0
k=1
l=2*A-1
m=1
matrix[0][0]=1
while m < l:	
	if m%2==0:
		if j==A-1:
			i+=1
		else:
			j+=1
		while(i>=0 and j<A):
			k+=1
			matrix[i][j]=k
			i+=1
			j-=1
			if(j==-1 or i==A):
				i-=1
				j+=1
				break
			
	elif m%2==1:
		if i==A-1:
			j+=1
		else:
			i+=1
		while(i>=0 and j<A):
			k+=1
			matrix[i][j]=k
			i-=1
			j+=1
			if(i==-1 or j==A):
				i+=1
				j-=1
				break

	m=m+1

for col in matrix:
	for row in col :
		print row,
	print ' '
