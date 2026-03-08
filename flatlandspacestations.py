def flatlandSpaceStations(n, c):
    maxi=0
    c.sort()
    for i in range(1,len(c)):
        maxi=max(maxi,(c[i]-c[i-1])//2)
    

    return max(maxi,c[0],n-1-c[-1])




print(flatlandSpaceStations(5,[0]))