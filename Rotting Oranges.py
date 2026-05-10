from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        minutes=0
        fresh=0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue=deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1                
                    
        while len(queue) and fresh>0:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for dir in dirs:
                    row,col=r+dir[0],c+dir[1]
                    if row>=0 and col>=0 and row<m and col<n and grid[row][col]==1:
                        grid[row][col]=2
                        fresh-=1
                        queue.append([row,col])
            if len(queue):
                minutes+=1

        return minutes if fresh==0 else -1
    
print(Solution().orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))

    
