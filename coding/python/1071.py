N = input()

A = raw_input().split(" ")
M = input()
i=0
sub=0
mul=0
while i<N:
	if M>=int(A[i]) and M%int(A[i])==0:
		sub+=int(A[i])
	if M<=int(A[i]) and int(A[i])%M==0:
		mul+=int(A[i])
	i+=1

print sub
print mul
