def encode(x,v):
	l1=len(x)
	s=""
	for i in range(0,l1) :
		if(x[i]!='-'):
			s=s+x[i]
	print("The value of s is:",s)
	ns=""
	k=1
	l2=len(s)
	for i in range (l2-1,-1,-1):
		ns=ns+s[i]
		if(k%v==0.0):
			ns=ns+"-"
		k=k+1
	print("The value of ns is:",ns)
	rev=""
	for i in range (len(ns)-2,-1,-1):
		rev=rev+ns[i]
	print("The value of rev is:",rev)
	return rev
x=input("Enter the string:\n")
v=int(input("Enter the value of v:\n"))
op=encode(x,v)
print("The encoded string is : \n")
print(op)
