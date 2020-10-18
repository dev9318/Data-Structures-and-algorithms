# Longest Common Subsequent

# recursive approach

def LCS(a,b,m,n):
    if m==0 or n==0:
        return 0
    if a[m-1] == b[n-1]:
        return 1 + LCS(a,b,m-1,n-1)
    else:
        return max(LCS(a,b,m,n-1),LCS(a,b,m-1,n))


if __name__ == "__main__":
    print(LCS("AGGTAB","GXTXAYB",6,7))
