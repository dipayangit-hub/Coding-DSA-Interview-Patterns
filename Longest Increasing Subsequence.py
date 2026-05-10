class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp=[1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            j=0
            while j<i:
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                j+=1
        return max(dp)
    
print(Solution().lengthOfLIS([0,1,0,3,2,3]))