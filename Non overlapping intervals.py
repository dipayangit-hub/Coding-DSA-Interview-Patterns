class Solution(object):
    def eraseOverlapIntervals(self, intervals):
            intervals.sort(key=lambda x:x[1])
            count=0
            last_end=intervals[0][1]
            for i in range(1,len(intervals)):
                #instead of removing interval, consider last_end as the last interval, in case previous interval is found as overlapping
                if intervals[i][0]<last_end:
                     count+=1
                else:
                     last_end=intervals[i][1]
            
            return count

print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))