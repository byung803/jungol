A = input()

matrix = [[0 for col in range(A)] for row in range(A)]

i=0
j=0
matrix[0][0]=1
k=2
while k<A*A+1:

	if j<A-1 and matrix[i][j+1]==0:
		while(j<A and matrix[i][j+1]==0):
			j=j+1
			matrix[i][j]=k
			k=k+1
			if(j==A-1):
				break
		continue
	elif i<A-1 and matrix[i+1][j]==0:
		while(i<A and matrix[i+1][j]==0):
			i=i+1
			matrix[i][j]=k
			k=k+1
			if(i==A-1):
				break
		continue
	elif j>0 and matrix[i][j-1]==0:
		while(j>0 and matrix[i][j-1]==0):
			j=j-1
			matrix[i][j]=k
			k=k+1
		continue
	elif i>0 and matrix[i-1][j]==0:
		while(i>0 and matrix[i-1][j]==0):
			i=i-1
			matrix[i][j]=k
			k=k+1
		continue
		
for col in matrix:
	for row in col:
		print row,
	print ' '




