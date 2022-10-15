def extract(a):
	b=[]
	c=[]
	d=[]
	e=[]
	for i in a:
		b.append(str(i))
	for i in b:
		l=len(i)
		for j in range(0,l):
			c.append(i[j])
	for i in c:
		d.append(int(i))
	for i in d:
		e.append(i%2)
	return e
n=int(input("Enter the size of the array:\n"))
arr=[]
for i in range(0,n):
	x=int(input("Enter element {} :\n".format(i+1)))
	arr.append(x)
print("The output array is:\n")
op=extract(arr)
print(op)
