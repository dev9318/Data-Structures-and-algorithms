# to find occurances of a string/ pattern in another string

def zarray(pattern, string):
    string = pattern + '$' + string
    z = [0]*len(string)
    l = r = k = 0
    n = len(string)
    for i in range(1,n):
        if (i > r): 
            l = r = i
            # "aaaaaa" and i = 1, Z[i] and R become 5 
            while r < n and string[r - l] == string[r]: 
                r += 1
            z[i] = r - l 
            r -= 1
        else: 
            k = i - l 
            if (z[k] < r - i + 1): 
                z[i] = z[k] 
            else: 
                l = i 
                while (r < n and string[r - l] == string[r]): 
                    r += 1
                z[i] = r - l 
                r -= 1