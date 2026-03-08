class Intervals:
    def __init__(self,sttime:int,endtime:int):
        self.sttime=sttime
        self.endtime=endtime

def nonoverlappingintervals(l:list):
    intervals=[Intervals(i[0],i[1]) for i in l]
    intervals.sort(key=lambda m:m.endtime)
    finishTime,c=0,0
    for i in range(len(intervals)):
        if intervals[i].sttime>=finishTime:
            c+=1
            finishTime=intervals[i].endtime
    return len(intervals)-c



if __name__ == "__main__":
    print(nonoverlappingintervals([(0,5),(3,4),(1,2),(5,9),(5,7),(7,9)]))