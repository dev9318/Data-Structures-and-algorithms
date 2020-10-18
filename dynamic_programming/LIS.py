# Longest increasing subsequence

# O(n^2) approach
def lis(arr): 
    n = len(arr) 
    lis = [1]*n 
   
    for i in range (1 , n): 
        for j in range(0 , i): 
            if (arr[i] > arr[j] and lis[i]< lis[j] + 1): 
                lis[i] = lis[j]+1
   
    maxi =  max(lis)
    return maxi