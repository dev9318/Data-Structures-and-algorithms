# Min no of cuts required to partition a string into 
# palindromes

# O(n^3) approach
def ispalin(stp):
    return stp == stp[::-1]

def palindrome_count(st,i,j):
    i = int(i)
    j = int(j)
    if (i>=j or ispalin(st[i:j+1])):
        return 0

    ans = 1000000000000
    for k in range(i,j):
        count = 1 + palindrome_count(st,i,k) + palindrome_count(st,k+1,j)
        ans = min(count,ans)
    return ans

# O(n^2) approach
def palin_cnt(st):
    n = len(st)
    cn = [0] * (n+1)
    palin = [[False for i in range(n+1)] for i in range(n+1)]
    
    for i in range(n):
        palin[i][i] = True
    
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            if (l == 2): 
                palin[i][j] = (st[i] == st[j]); 
            else: 
                palin[i][j] = ((st[i] == st[j]) and palin[i + 1][j - 1])
    for i in range(n): 
        if (palin[0][i] == True): 
            cn[i] = 0 
        else: 
            cn[i] = 1000000000
            for j in range(i): 
                if(palin[j + 1][i] == True and 1 + cn[j] < cn[i]): 
                    cn[i] = 1 + cn[j]
    print(cn[n-1])

if __name__ == "__main__":
    string = "ababbbabbababa"
    palin_cnt(string)
