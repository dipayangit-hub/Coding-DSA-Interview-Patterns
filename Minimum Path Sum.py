class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[-1 for _ in range(n)]
        prev=[-1 for _ in range(n)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                sum=float('inf')
                if i!=m-1:
                    sum=min(sum,prev[j])
                if j!=n-1:
                    sum=min(sum,dp[j+1])
                if i==m-1 and j==n-1:
                    sum=0
                dp[j]=sum+grid[i][j]
            prev=dp[:]
        return dp[0]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))