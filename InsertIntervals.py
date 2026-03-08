
def insertintervals(intervals:list,newinterval:list):
    res=[]
    i=0
    while i<len(intervals) and intervals[i][1]<newinterval[0]:
        res.append([intervals[i][0],intervals[i][1]])
        i+=1

    while i<len(intervals) and intervals[i][0]<=newinterval[1]:
        newinterval[0]=min(newinterval[0],intervals[i][0])
        newinterval[1]=max(newinterval[1],intervals[i][1])
        i+=1
    res.append([newinterval[0],newinterval[1]])

    while i<len(intervals):
        res.append([intervals[i][0],intervals[i][1]])
        i+=1
    
    return res




if __name__ == "__main__":
    print(insertintervals([[1,2],[3,4],[7,7],[8,10],[12,16]],[5,6]))