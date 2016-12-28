A = input()

matrix = [[0 for col in range(A)] for row in range(A)]

i=0
j=0
matrix[0][0]=1
k=2
#오른쪽 아래 왼쪽 위 순서로 우선순위다. 
#if문 확인해서 오른쪽으로 끝까지 쭉가고 막히면 아래, 막히면 왼쪽, 막히면 위
#이런 방식으로 흘러간다. 매번 확인하는게 아니라 한번 확인하고  막힐때까지 가고 
#그 다음 또 확인하고 막힐때까지 가고 하는  방식이다. 
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




