from collections import defaultdict
class Solution(object):
    # def isValidSudoku(self, board):
    #     n=len(board)
    #     pos_map=defaultdict(list)
    #     for i in range(n):
    #         for j in range(n):
    #             if board[i][j]!=".":
    #                 if self.validitycheck(board,i,j,pos_map):
    #                     pos_map[board[i][j]].append([i,j])
    #                 else:
    #                     return False
    #     return True
        
    
    # def validitycheck(self,board,r,c,pos_map):
    #     val=board[r][c]
    #     if val in pos_map:
    #         for l in pos_map[val]:
    #             if (l[0]//3)==(r//3) and (l[1]//3)==(c//3):
    #                 return False
    #             if r==l[0] or c==l[1]:
    #                 return False
    
    #     return True
    
     def isValidSudoku(self, board):
          rows=[set() for _ in range(9)]
          cols=[set() for _ in range(9)]
          boxes=[set() for _ in range(9)]

          for i in range(9):
               for j in range(9):
                    val=board[i][j]
                    if val!=".":
                         box=(i//3)*3+(j//3)
                         if val in rows[i] or val in cols[j] or val in boxes[box]:
                              return False
                         rows[i].add(val)
                         cols[j].add(val)
                         boxes[box].add(val)
          return True

board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]     
print(Solution().isValidSudoku(board))