class Solution(object):
    # def climbStairs(self, n):
    #     return self.recurse(n,0,[])
    # def recurse(self,n,i,dp):
    #     if len(dp)==0:
    #         dp=[-1  for _ in range(n)]
    #     if i==n:
    #         return 1
    #     elif i>n:
    #         return 0
    #     if dp[i]>-1:
    #         return dp[i]
    #     dp[i]=self.recurse(n,i+1,dp)+self.recurse(n,i+2,dp)
    #     return dp[i]

    def climbStairs(self, n):
        if n<2:
            return n
        prev1,prev2=2,1
        for i in range(3,n+1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        return prev1
        
    
print(Solution().climbStairs(5))
