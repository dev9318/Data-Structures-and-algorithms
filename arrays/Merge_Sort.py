def mergeSort(arr):
    if(len(arr)==1):
        return arr
    leng = len(arr)
    left = arr[:int(leng/2)]
    print(left)
    right = arr[int(leng/2):]
    mergeSort(left)
    mergeSort(right)
    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1
    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    while j<len(left):
        arr[k] = right[j]
        j+=1
        k+=1

if __name__ == "__main__":
    a = [7,4,3,8,1,3]
    mergeSort(a)
    print(a)