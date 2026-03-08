
def fractionalknapsackalgo(arr:list,weight:int):
    arr.sort(key=lambda m:(int)(m[0]/m[1]),reverse=True)
    value=0
    for i in arr:
        if i[1]<=weight:
            value+=i[0]
            weight-=i[1]
        else:
            value+=(int)(i[0]/i[1])*weight
            break
    return value






if __name__ == "__main__":
    print(fractionalknapsackalgo([(100,20),(60,10),(100,50),(200,50)],90))