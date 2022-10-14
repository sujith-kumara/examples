def largestNumber(array):
    if len(array) == 1:
        return str(array[0])
    for i in range(len(array)):
        array[i] = str(array[i])
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[j]+array[i] > array[i]+array[j]:
                array[i],array[j] = array[j],array[i]
    result = ''.join(array)
    if (result == '0'*len(result)):
        return '0'
    else:
        return result
a = [54,5,56,9,7,5]
print(largestNumber(a))