num = raw_input()
i=0

k=int(num)
while k >= 10:
	k=0
	while i<len(num):
		k += int(num[i])
		i+=1
	print k
	num = str(k)
	i=0
