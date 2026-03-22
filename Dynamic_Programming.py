#top down approach
def fib_memoization(dp:list,n):
    if len(dp)==0:
        dp=[-1]*(n+1)
    if n==0 or n==1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=fib_memoization(dp,n-1)+fib_memoization(dp,n-2) 
    return dp[n]

#bottom up approach
def fib_tabulation(n):
    dp=[-1]*(n+1)
    #start with smallest sub problem and move towards solution
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

#space optimization
def fib_spaceoptimized(n):
    #store only 2 previous values
    prev2=0
    prev1=1
    curr=0
    for i in  range(2,n+1):
        curr=prev1+prev2
        prev2=prev1
        prev1=curr
    return prev1


class Solution(object):
    #top down
    # def rob(self, nums):
    #     def recurse(i,nums,dp:list):
    #         if len(dp)==0:
    #             dp=[-1]*(len(nums)+1)
    #         if i>=len(nums):
    #             return 0
    #         if dp[i]!=-1:
    #             return dp[i]
    #         take=nums[i]+recurse(i+2,nums,dp)
    #         nottake=recurse(i+1,nums,dp)
    #         dp[i]=max(take, nottake)
    #         return dp[i]
    #     return recurse(0,nums,[])

    #bottom-up
    # def rob(self, nums):
    #     if len(nums)<2:
    #         return nums[0]
    #     dp=[-1]*(len(nums))
    #     dp[-1]=nums[-1]
    #     dp[-2]=max(nums[-1],nums[-2])

    #     for i in range(len(nums)-3,-1,-1):
    #         take=nums[i]+dp[i+2]
    #         nottake=dp[i+1]
    #         dp[i]=max(take,nottake)
    #     return dp[0]

    #space optimization
    def rob(self, nums):
        if len(nums)<2:
            return nums[0]
        prev2=nums[-1]
        prev1=max(nums[-2],nums[-1])
        for i in range(len(nums)-3,-1,-1):
            take=nums[i]+prev2
            nottake=prev1
            prev2=prev1
            prev1=max(take,nottake)
        return prev1
    

print(Solution().rob([2,7,9,3,1]))