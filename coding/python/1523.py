from __future__ import print_function
n, m = raw_input().split(' ')

N = int(n)
M = int(m)
i=1
j=0
k=0
if M==1 and N>0 and N<101:
	while(i<N+1):
		while(j<i):
			print ("*", end="")
			j+=1
		print (' ')
		i+=1
		j=0
elif M==2 and N>0 and N<101:
	k=N
	while(i<N+1):
		while(j<k):
			print ("*", end="")
			j+=1
		print (' ')
		i+=1
		k-=1
		j=0
	
elif M==3 and N>0 and N<101:
	k=0
	l=N-1
	while(i<N+1):
		while(k<l):
			print(" ", end="")
			k+=1
		while(j<2*i-1):
			print("*", end="")
			j+=1
		print (' ')
		i+=1
		l-=1
		k=0
		j=0
else:
	print ("INPUT ERROR!")
