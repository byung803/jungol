val = 65
number = input()
i=0
j=0
k= val+(number*number-1)
l=0
while i < number:
	while j < number:
		while(k > 90):
			if k > 90:
				k = k-26
		l = k-(j*number)
		while(l < 65):
			if l < 65:
				l = l+26
		print chr(l),
		j = j+1
	i = i+1
	j=0
	k = k-1
	print ' '

