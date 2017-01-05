N, M = raw_input().split(" ")

n = int(N)
m = int(M)

if m==1 and n>0 and n<=100 and n%2==1:
	i=0
	j=1
	k=0
	l=0
	while i<n:
		if i%2==0:
			j=l+1
			while k<i+1:
				print j,
				k+=1
				j+=1
				l+=1
			i+=1
			k=0
			print ' '
		else:
			j=l+i+1
			while k<i+1:
				print j,
				k+=1
				j-=1
			 	l+=1
			i+=1
			k=0
			print ' '
		
elif m==2 and n>0 and n<=100 and n%2==1:
	i=0
	j=2*n-1
	k=0
	while i<n:
		while k<i:
			print ' ',
			k+=1
		k=0
		while k<j:
			print i,
			k+=1
		i+=1
		j-=2
		k=0
		print ' '
				


elif m==3 and n>0 and n<=100 and n%2==1:
	i=0
	j=1
	k=0
	l=n
	while i<n:
		if i<(n+1)/2:
			while k<i+1 :
				print j,
				k+=1
				j+=1
			j=1
			i+=1			
			l-=1
			k=0
			print ' '
		else :
			while k<l :
				print j,
				k+=1
				j+=1
			j=1
			i+=1
			l-=1
			k=0	
			print ' '		
else:
	print "INPUT ERROR!"
