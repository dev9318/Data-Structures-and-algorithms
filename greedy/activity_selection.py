def activty_select(s,f):
    for i in range(len(f)):
        for j in range(i,len(f)-1):
            if(f[i+1]<f[i]):
                temp = s[i]
                s[i] = s[i+1]
                s[i+1] = temp
                temp = f[i]
                f[i] = f[i+1]
                f[i+1] = temp
    print(str(s[0])+" "+str(f[0]))
    last = f[0]
    for i in range(len(f)-1):
        if(s[i+1]>=last):
            print(str(s[i+1])+" "+str(f[i+1]))
            last = f[i+1]

if __name__ == "__main__":
    s = [1 , 3 , 0 , 5 , 8 , 5] 
    f = [2 , 4 , 6 , 7 , 9 , 9] 
    activty_select(s,f)