def chocolate(a,n,m):
    if n == 0 or m == 0:
        return 0
    if n < m:
        return -1
    a.sort()
    min_diff = arr[n-1]-arr[0]
    for i in range(len(a)-m+1):
        min_diff = min(min_diff, a[i+m-1]-a[i])
    return min_diff

arr = [12, 4, 7, 9, 2, 23, 25, 41,
           30, 40, 28, 42, 30, 44, 48,
           43, 50]
m = 7  # Number of students
n = len(arr)
print("Minimum difference is", chocolate(arr, n, m))