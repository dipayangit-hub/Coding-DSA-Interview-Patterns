class Solution:
    def numIslands(self, grid: list[list[str]]):
        m=len(grid)
        n=len(grid[0])
        seen=[[False for _ in range(n)] for _ in range(m)]
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and seen[i][j]==False:
                    self.dfs(grid,m,n,i,j,seen)
                    count+=1
        return count  

    def dfs(self,grid,m,n,i,j,seen):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]=="0" or seen[i][j]==True:
            return
        seen[i][j]=True
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        for dir in dirs:
            r,c=i+dir[0],j+dir[1]
            self.dfs(grid,m,n,r,c,seen)
        

print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))