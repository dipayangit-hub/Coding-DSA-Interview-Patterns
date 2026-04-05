class Solution(object):
    def canJump(self, nums):
        maxjump=0 #pointer for max jump or the last index possible

        for i in range(len(nums)):
            # if we cant reach ith index
            if maxjump<i:
                return False
            maxjump=max(maxjump,nums[i]+i)
            #we reached last index
            if maxjump>=len(nums)-1:
                return True
        return True
    
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        #end is end point of current jump window
        maxjump,end=0,0
        ans=0
        for i in range(len(nums)-1):
            maxjump=max(maxjump,nums[i]+i)
            if maxjump>=len(nums)-1:
                return ans+1
            #end of current jump
            if end==i:
                ans+=1
                end=maxjump
        return ans  

    def canCompleteCircuit(self, gas, cost):
         totalgas,totalcost=0,0
         for i in range(len(gas)):
             totalgas+=gas[i]
             totalcost+=cost[i]

         if totalgas<totalcost:
             return -1
         
         pos,remaining=0,0

         for i in range(len(gas)):
             remaining+=gas[i]-cost[i]
             if remaining<0:
                 remaining=0
                 pos=i+1 #starting from next index as this will be the last remaining positive index
         return pos

print(Solution().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))