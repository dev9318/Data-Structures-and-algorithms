def partition(a,l,h):
    pivot = a[l]
    i=l-1
    j=h+1
    while i < j:
        while True:
            i+=1
            if i==h or a[i]>= pivot:
                break
        while True:
            j-=1
            if j==l or a[j]<pivot:
                break
        if(i<j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    temp = a[l]
    a[l] = a[j]
    a[j] = temp
    return j
def quickSort(a,l,h):
    if(l<h):
        j = partition(a,l,h)
        quickSort(a,l,j-1)
        quickSort(a,j+1,h)
a = [3,6,1,7,8,2,3,4]
quickSort(a,0,7)
print(a)
