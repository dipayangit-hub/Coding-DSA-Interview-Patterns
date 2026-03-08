def merge(intervals: list):
    intervals.sort(key= lambda l: l[0])
    n=len(intervals)
    res=[]
    res.append(intervals[0])
    e=0
    for i in range(1,n):
        if intervals[i][0]<=res[e][1]:
            res[e][1] = max(res[e][1],intervals[i][1])
        else:
            e+=1
            res.append(intervals[i])
    return res



def insert(intervals: list, newInterval: list):
    res=[]
    i=0
    while i<len(intervals) and intervals[i][1] < newInterval[0]:
         res.append(intervals[i])
         i+=1
    
    while i<len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0]=min(newInterval[0],intervals[i][0])
        newInterval[1]=max(newInterval[1],intervals[i][1])
        i+=1

    res.append(newInterval)

    while i<len(intervals):
        res.append(intervals[i])
        i+=1
    return res

    
def max_non_overlapping(intervals):
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    last_end = float('-inf')
    
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
            
    return count



print(max_non_overlapping([[1,3],[3,4],[4,9],[4,5],[5,6],[6,9],[12,16]]))
