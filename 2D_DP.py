class Solution(object):
    #top down
    # def minPathSum(self, grid):
    #     def recurse(grid,i,j,dp):
    #         if len(dp)==0:
    #             dp=[[-1 for _ in range(j+1)] for _ in range(i+1)]
    #         if i<0 or j<0:
    #             return float('inf')
    #         if i==0 and j==0:
    #             return grid[0][0]
    #         if dp[i][j]!=-1:
    #             return dp[i][j]
    #         top=recurse(grid,i-1,j,dp)
    #         left=recurse(grid,i,j-1,dp)
    #         dp[i][j]=grid[i][j]+min(top,left)
    #         return dp[i][j]
            
    #     return recurse(grid,len(grid)-1,len(grid[0])-1,[])

    #bottom up
    # def minPathSum(self, grid):
    #     m=len(grid)
    #     n=len(grid[0])
    #     dp=[[-1 for _ in range(n)] for _ in range(m)]

    #     for i in range(m):
    #         for j in range(n):
    #             if i==0 and j==0:
    #                 dp[i][j]=grid[0][0]
    #                 continue
    #             top=float('inf') if i==0 else dp[i-1][j]
    #             left=float('inf') if j==0 else dp[i][j-1]
    #             dp[i][j]=grid[i][j]+min(top,left)

    #     return dp[m-1][n-1]
    
    #space optimization
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        prev=[-1]*n
        for i in range(m):
            curr=[-1]*n
            for j in range(n):
                if i==0 and j==0:
                    curr[j]=grid[i][j]
                    continue
                top=float('inf') if i==0 else prev[j]
                left=float('inf') if j==0 else curr[j-1]
                curr[j]=grid[i][j]+min(top,left)
            prev=curr

        return curr[n-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
            
