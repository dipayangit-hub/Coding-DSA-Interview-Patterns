class Solution:
    def solve(self, board: list[list[str]]):
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=='O':
                    self.dfs(board,i,j,m,n)

        for i in range(m):
            for j in range(n):
                if board[i][j]=='M':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        return board
        
    
    def dfs(self,board,i,j,m,n):
        if i<0 or j<0 or i==m or j==n or board[i][j]=='X' or board[i][j]=='M':
            return
        board[i][j]='M'
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        for dir in dirs:
            r=i+dir[0]
            c=j+dir[1]
            self.dfs(board,r,c,m,n)


print(Solution().solve([["X","X","X","X","X"],["X","O","O","X","O"],["X","X","O","X","O"],["X","O","X","O","X"],["O","O","X","X","X"]]))
