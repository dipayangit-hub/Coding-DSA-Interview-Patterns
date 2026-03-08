def shortestjobfirst(bt:list):
    t,s=0,0
    bt.sort()
    for i in bt:
        s+=t
        t+=i
    return (int)(s/len(bt))
        





print(shortestjobfirst([4,3,7,1,2]))