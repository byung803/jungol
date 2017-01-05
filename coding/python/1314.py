val = 65
number = input()
i=0
j=0
l=number
k=val

while i < number:
	while j < number:
		if j%2==1 and j!=0 :
			k = k+(2*l-1) 
		elif j%2==0 and j!=0:
			k = k+(2*i+1)
		while(k > 90):
			if k > 90:
				k = k-26
		print chr(k),
		j = j+1
	i = i+1
	j=0
	l = l-1
	k = val+i
	print ' '

