
def minplatforms(arr:list,dep:list):
    maxcount,count=1,0
    arr.sort()
    dep.sort()
    i,j=0,0
    while i<len(arr) and j<len(dep):
        if arr[i]<=dep[j]:
            count+=1
            i+=1
        else:
            count-=1
            j+=1
        maxcount=max(count,maxcount)


    return maxcount






if __name__ == "__main__":
    print(minplatforms([900,945,955,1100,1500,1800],[920,1200,1130,1150,1900,2000]))