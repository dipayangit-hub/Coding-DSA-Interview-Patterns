def assigncookies(greed:list,s:list):
    greed.sort()
    s.sort()

    l,r=0,0
    while l<len(s) and r<len(greed):
        if s[l]>=greed[r]:
            r+=1
        l+=1
    return r





print(assigncookies([1,5,3,3,4],[4,2,1,2,1,3]))