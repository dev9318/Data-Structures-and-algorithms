def partition(a,l,h):
    pivot = a[l]
    i=l-1
    j=h+1
    while i < j:
        do{
            i+=1
        }while a[i]<= pivot
        do{
            j+=1
        }while a[j]>pivot
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
quicksort(a)
print(a)