from __future__ import print_function
n, m = raw_input().split(' ')

N = int(n)
M = int(m)


if M==1 and N>0 and N<101 and N%2==1:
	i=1
	j=0
	while i<N+1:
		if i<((N+1)/2)+1:
			while j<i:
				print("*", end="")	
				j+=1
			i+=1
			j=0
			print (' ')
		else:
			while j<N-i+1:
				print("*", end="")
				j+=1
			i+=1
			j=0
			print(' ')
	
elif M==2 and N>0 and N<101 and N%2==1:
	i=0
	j=(N+1)/2-1
	k=0
	while i<N:
		if i<(N+1)/2:
			while k<j-i:
				print(" ", end="")
				k+=1
			k=0				 
			while k<i+1:
				print("*", end="")
				k+=1
			k=0
			i+=1
			print (' ')
		else:	
			while k<abs(j-i):
				print(" ", end="")
				k+=1
			k=0
			while k<2*j-i+1:
				print("*", end="")
				k+=1
			k=0
			i+=1
			print(' ')
elif M==3 and N>0 and N<101 and N%2==1:
	i=0
	j=N
	k=0
	while i<N:
		if i<((N+1)/2):
			while k<i:
				print(" ", end="")
				k+=1
			k=0
			while k<j-i:
				print("*", end="")
				k+=1
			i+=1
			j-=1
			k=0
			print (' ')
		else:
			while k<j-1:
				print(" ", end="")
				k+=1	
			k=0
			while k<abs(j-i-2): 
				print("*", end="")
				k+=1

			print (' ')
			i+=1
			j-=1
			k=0
elif M==4 and N>0 and N<101 and N%2==1:
	i=0
	j=(N+1)/2
	k=0
	while i<N:
		if i<((N+1)/2):
			while k<i:
				print(" ", end="")
				k+=1
			k=0
			while k<j-i:
				print("*", end="")
				k+=1
			i+=1
			k=0
			print (' ')
		else:
			while k<j-1:
				print(" ", end="")
				k+=1	
			k=0
			while k<abs(j-i)+2: 
				print("*", end="")
				k+=1

			print (' ')
			i+=1
			k=0
else:
	print ("INPUT ERROR!")
