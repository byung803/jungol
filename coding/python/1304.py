number = input()

i=0
j=0
k=0
while i < number:
	while j < number:
		#print "j=%d" % j
		print (i+1)+(number*k),
		j += 1
		k += 1
	#print "i=%d" % i
	i += 1
	j=0
	k=0
	print ' '

