import math
a = input()
A = str(a)

submul = [] 
i=1
j=0

stand = math.sqrt(a)
stand = int(stand)
while i < stand+1:
	if a%i==0:
		if(i == a/i):
			i+=1
			continue
		submul.append(i)
		submul.append(a/i)
	i+=1

if stand*stand ==a:
	submul.append(stand)

submul.sort()

for j in submul:
	print j,

