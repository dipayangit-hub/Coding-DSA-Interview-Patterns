class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        curmin,minsum=0,nums[0]
        curmax,maxsum=0,nums[0]
        total=0
        n=len(nums)
        for i in range(n):
            total+=nums[i]

            curmin=min(curmin+nums[i],nums[i])
            minsum=min(minsum,curmin)

            curmax=max(nums[i],curmax+nums[i])
            maxsum=max(maxsum,curmax)


        return max(maxsum,total-minsum) if maxsum>0 else maxsum

print(Solution().maxSubarraySumCircular([1,-2,3,-2]))

