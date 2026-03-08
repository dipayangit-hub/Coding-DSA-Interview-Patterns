def mySqrt(x):
    res=0
    l,r=0,x
    while l<=r:
        mid=l+((r-l)//2)
        if mid*mid>x:
            r=mid-1
        elif mid*mid<x:
            res=mid
            l=mid+1 
        else:
            return mid  
    return res

print(mySqrt(2))