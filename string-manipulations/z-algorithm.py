# to find occurances of a string/ pattern in another string

def zarray(pattern, string):
    string = pattern + '$' + string
    z = [0]*len(string)
    l = r = k = 0
    for i in range(1,n):
        