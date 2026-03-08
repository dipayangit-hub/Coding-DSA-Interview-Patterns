from collections import Counter
def beautifulPairs(A, B):
    a=Counter(A)
    b=Counter(B)

    b_set=0

    for val in a:
        if val in b:
            b_set+= min(a[val],b[val])

    
    if b_set==len(A):
        return b_set-1
    else:
        return b_set+1


print(beautifulPairs([1,2,3,4],[1,2,3,3]))
    
                    
            

    