class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        maxH=0
        for i in range(len(citations)):
                #first check if current lement vs count which is minimum, and thenconsider it in max-> for 1 element as 100 (only element), max can be 1 where 1 paper =1 citation 
                count=len(citations)-i
                maxH=max(maxH,min(citations[i],count))
        return maxH
    

print(Solution().hIndex([0]))