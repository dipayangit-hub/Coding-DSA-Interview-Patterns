class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])

        dp=[0 for _ in range(m)]
        maxsq=0

        for i in range(n):
            prev_diag=0
            for j in range(m):
                temp=dp[j]
                if i==0 or j==0:
                    dp[j]=int(matrix[i][j])
                elif matrix[i][j]=="1":
                    dp[j]=min(prev_diag,dp[j-1],dp[j])+1
                else:
                    dp[j]=0
                maxsq=max(maxsq,dp[j])
                prev_diag=temp
        
        return maxsq**2


print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))

