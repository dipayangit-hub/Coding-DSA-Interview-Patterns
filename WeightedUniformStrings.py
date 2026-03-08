def weightedUniformStrings(s, queries):
    d={}
    res=[]
    weight=0
    for i in range(len(s)):
        if i==0 or s[i]!=s[i-1]:
            weight=ord(s[i]) - ord('a') + 1
        else:
            weight=weight+ord(s[i])-ord('a')+1
        d[weight]=1

        
    for i in queries:
        res.append("Yes" if i in d else "No")

    return res
    
print(weightedUniformStrings('abbcccdddd',[1,7,5,4,15]))