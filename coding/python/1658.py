A, B = raw_input().split(" ")

a = int(A)
b = int(B)
mat1 = []
mat2 = []
mat3 = []
i=1
while i<a+1:
	if a%i==0:
		mat1.append(i)
	i+=1
i=1
while i<b+1:
	if b%i==0:
		mat2.append(i)
	i+=1
i=0
j=0
while i<len(mat1):
	while j<len(mat2):
		if mat1[i]==mat2[j]:
			mat3.append(mat1[i])
		j+=1
	i+=1
	j=0


#print mat1
#print mat2
#print mat3

print max(mat3)
print max(mat3)*(a/max(mat3))*(b/max(mat3))
