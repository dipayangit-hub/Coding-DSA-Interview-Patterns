class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])        
        for i in range(n):
            for j in range(m):
                    if word[0]==board[i][j] and self.backtrack(board,n,m,i,j,"",word,0):
                            return True
        return False
        
    def backtrack(self,board,n,m,i,j,s,word,k):
        if i<0 or i==n or j<0 or j==m or board[i][j]=='*':
            return False
        ch=board[i][j]
        s+=ch
        board[i][j]='*'
        if s==word:
            return True
        elif word[k]!=ch:
            board[i][j]=ch
            return False
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        for dir in dirs:
            r=i+dir[0]
            c=j+dir[1]
            if self.backtrack(board,n,m,r,c,s,word,k+1):
                return True
        board[i][j]=ch
        return False
print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB"))
