from __future__ import print_function

N = input()


if N>0 and N<101 and N%2==1:
	i=1
#	j=(N+1)/2
	k=0
	l=N
	while i<N+1:
		if i<((N+1)/2)+1:
			while k<i-1:
				print(" ", end="")
				k+=1
			k=0
			while k<(2*i-1):
				print("*", end="")	
				k+=1
			i+=1
			l-=1
			k=0
			print (' ')
		else:
			while k<l-1:
				print(" ", end="")
				k+=1
			k=0
			while k<(2*l-1):
				print("*", end="")	
				k+=1
			i+=1
			l-=1
			k=0
			print (' ')
else:
	print ("INPUT ERROR!")
	
