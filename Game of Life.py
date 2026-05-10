class Solution(object):
    def gameOfLife(self, board):
        m= len(board)
        n= len(board[0])

        dir=[[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]

        for i in range(m):
            for j in range(n):
                activeneightbours=0
                activeneightbours=self.getactive(board,i,j,dir)
                if (activeneightbours<2 or activeneightbours>3) and board[i][j]==1:
                    board[i][j]=-2 #intermediate state
                if activeneightbours==3 and board[i][j]==0:
                    board[i][j]=3 #intermediate state

        #update to 0s and 1s from intermediate state
        self.update_matrix(board,m,n)

    def getactive(self,board,i,j,dir):
        active=0
        for d in dir:
            r=i+d[0]
            c=j+d[1]

            if r>=0 and r<len(board) and c>=0 and c<len(board[0]) and (board[r][c]==1 or board[r][c]==-2):
                active+=1
        
        return active



    def update_matrix(self,board,m,n):
        for i in range(m):
            for j in range(n):
                if board[i][j]==-2:
                    board[i][j]=0
                elif board[i][j]==3:
                    board[i][j]=1
        

print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
                    
                        
                        
                    
