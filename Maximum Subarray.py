class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum,maxsum=0,nums[0]
        for i in range(len(nums)):
            # sum+=nums[i]
            # maxsum=max(maxsum,sum)
            # if sum<0:
            #     sum=0
            sum=max(nums[i],sum+nums[i])
            maxsum=max(maxsum,sum)
        return maxsum
    
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
                
