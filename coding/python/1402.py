A, B = raw_input().split(" ")

a = int(A)
b = int(B)

submul = [] 
i=1
while i<a+1:
	if(a%i==0):
		submul.append(i)
	i+=1
#i=0
#while i< len(submul):
#	print submul[i],
#	i+=1
#print ' '

if len(submul) < b:
	print 0
else:
	print submul[b-1]
