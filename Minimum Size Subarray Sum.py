class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        sum,minl=0,float('inf')
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                minl=min(minl,r-l+1)
                sum-=nums[l]
                l+=1
        return 0 if minl==float('inf') else minl
            

print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))