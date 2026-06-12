class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        
        def recurse(grid,x,y,length):
            if length==1:
                return Node(grid[x][y],True,None,None,None,None)
            
            topleft=recurse(grid,x,y,length//2)
            topright=recurse(grid,x,y+length//2,length//2)
            bottomleft=recurse(grid,x+length//2,y,length//2)
            bottomright=recurse(grid,x+length//2,y+length//2,length//2)

            if topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and topleft.val==topright.val and topright.val==bottomleft.val and bottomleft.val==bottomright.val:
                return Node(grid[x][y],True,None,None,None,None)

            return Node(grid[x][y],False,topleft,topright,bottomleft,bottomright)
                    
                    
        return recurse(grid,0,0,len(grid))         
    
print(Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]))

