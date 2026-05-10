class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        
        dp=[-1 for _ in range(n)]
        prev=[-1 for _ in range(n)]

        dp[n-1]=1
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                    continue
                elif i==m-1 and j==n-1:
                    continue
                count=0
                if i<m-1:
                    count+=prev[j]
                if j<n-1:
                    count+=dp[j+1]
                
                dp[j]=count
            prev=dp[:]
        return dp[0]
    
print(Solution().uniquePathsWithObstacles([[1]]))
