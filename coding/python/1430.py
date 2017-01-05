A = input()
B = input()
C = input()

val = A*B*C

val_str = str(val)

a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
a0=0
i=0

while i < len(val_str):
#	print val_str[i]
	if val_str[i] == str(0):
		a0+=1
	elif val_str[i] == str(1):
		a1+=1	
	elif val_str[i] == str(2):
		a2+=1	
	elif val_str[i] == str(3):
		a3+=1	
	elif val_str[i] == str(4):
		a4+=1	
	elif val_str[i] == str(5):
		a5+=1	
	elif val_str[i] == str(6):
		a6+=1	
	elif val_str[i] == str(7):
		a7+=1	
	elif val_str[i] == str(8):
		a8+=1	
	elif val_str[i] == str(9):
		a9+=1	
	i= i+1	
	  
print a0
print a1
print a2
print a3
print a4
print a5
print a6
print a7
print a8
print a9
