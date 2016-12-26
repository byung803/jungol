a, b = raw_input().split(" ")
number = int(a) 
val = int(b)
#print "number: %s" % number
#print "val: %s" % val
i=0
j=0
if val == 1:
	while i < number:
		while j < number:
			print i+1,
			j = j+1
		i =i+1
		j=0
		print ' '

elif val ==2:
	while i < number:
		if i%2 == 0:
			while j < number:
				print j+1,
				j = j+1
		else:
			k=number
			while j < number:
				print k,
				j = j+1
				k = k-1
		i =i+1
		j=0
		print ' '
elif val ==3:
	while i < number:
		while j < number:
			print (i+1)*(j+1),
			j = j+1
		i =i+1
		j=0
		print ' '
