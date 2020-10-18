# Longest Common Subsequent

# recursive approach

def LCS(a,b,m,n):
    if m==0 or n==0:
        return 0
    if a[m-1] == b[n-1]:
        return 1 + LCS(a,b,m-1,n-1)
    else:
        return max(LCS(a,b,m,n-1),LCS(a,b,m-1,n))

# DP approach

def lcs(a,b):
    m = len(a)
    n = len(b)
    C = [[None]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                C[i][j] = 0
            elif a[i-1] == b[j-1]:
                C[i][j] = 1 + C[i-1][j-1]
            else:
                C[i][j] = max(C[i-1][j],C[i][j-1])
    return C[m][n]

if __name__ == "__main__":
    print(lcs("AGGTAB","GXTXAYB"))
