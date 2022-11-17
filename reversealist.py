def reverselist(a,start,end):
    if start >= end:
        return
    a[start],a[end] = a[end],a[start]
    reverselist(a, start+1, end-1)
a = [1,2,3,4,5,6]
print(a)
reverselist(a, 0, 5)
print(a)