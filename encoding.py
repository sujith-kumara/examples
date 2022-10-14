"""
PROGRAM:
Capital : convert to small -1
Small:  Convert to capital +1
number : number - 1
0 : _
A: *
z: ^
special character : -
"""



def encoding(x):
	for i in x:
		
		if(i>'A' and i<='Z'):
			x=x.replace(i,chr(ord(i)+32-1))
		elif(i>='a' and i<'z'):
			x=x.replace(i,chr(ord(i)-32+1))
		elif(i>'0' and i<='9'):
			x=x.replace(i,chr(ord(i)-1))
		elif(i=='0'):
			x=x.replace(i,'_')
		elif(i=='A'):
			x=x.replace(i,'*')
		elif(i=='z'):
			x=x.replace(i,'^')
		else:
			x=x.replace(i,'-')
	return x
s=input("Enter the string\n")
y=encoding(s)
print("The encoded string is: \n")
print(y)
