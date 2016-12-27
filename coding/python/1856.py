A, B = raw_input().split(" ")
a = int(A)
b = int(B)
i=0
j=0
while i<a:
	while j<b:
		if i%2==0 and i!=0:
			print (b*i+1+j), 
		elif i%2==1 and i!=0:
			print (b*(i+1)-j), 
		else: 
			print (j+1),
		j=j+1
	i=i+1
	j=0
	print ' '
