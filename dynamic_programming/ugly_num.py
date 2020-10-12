# Ugly numbers are numbers which are multiples of 
# only 2, 3 or 5. Aim: To find nth ugly no in O(n)


def Ugly(n):
    
    uglyn = [0]*n
    uglyn[0] = 1
    i2 = i3 = i5 = 0
    mul_2 = 2
    mul_3 = 3
    mul_5 = 5
    
    for i in range(1,n):
        uglyn[i]=min(mul_2,mul_3,mul_5)
        
        if (mul_2 == uglyn[i]):
            i2 += 1
            mul_2 = uglyn[i2]*2
        if(mul_3 == uglyn[i]):
            uglyn[i] = mul_3
            i3 += 1
            mul_3 = uglyn[i3]*3
        if(mul_5 == uglyn[i]):
            uglyn[i] = mul_5
            i5 += 1
            mul_5 = uglyn[i5]*5

    print(uglyn[n-1])


if __name__ == "__main__":

    Ugly(100)
    Ugly(150)
