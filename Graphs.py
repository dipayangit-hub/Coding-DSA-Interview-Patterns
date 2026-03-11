from collections import deque
def create_adj_matrix():
    v=3
    mat=[[0] * v for _ in range(v)]
    addEdges(mat,0,1)
    addEdges(mat,0,2)
    addEdges(mat,1,2)
    return mat

def addEdges(mat:list,i,j):
    #undirected- adding both directions
    mat[i][j]=1
    mat[j][i]=1


def create_adj_list():
    v=3 
    #dictionary
    # adj = {i: [] for i in range(v)}
    #list of lists
    adj = [[] for _ in range(v)]
    addEdges_list(adj,0,1)
    addEdges_list(adj,0,2)
    addEdges_list(adj,1,2)
    return adj

def addEdges_list(adj,i,j):
    #undirected- adding both directions
    adj[i].append(j)
    adj[j].append(i)

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        oldcolor=image[sr][sc]
        rows=len(image)
        cols=len(image[0])

        if oldcolor!=color:
            self.dfs(image, sr,sc,rows,cols,color,oldcolor)

        return image
    
    def dfs(self,image, sr, sc,rows,cols,newcolor, oldcolor):
        if sr<0 or sc<0 or sr>=rows or sc>=cols or image[sr][sc]!=oldcolor:
            return
        image[sr][sc]=newcolor
        self.dfs(image,sr-1,sc,rows,cols,newcolor,oldcolor)
        self.dfs(image,sr+1,sc,rows,cols,newcolor,oldcolor)
        self.dfs(image,sr,sc-1,rows,cols,newcolor,oldcolor)
        self.dfs(image,sr,sc+1,rows,cols,newcolor,oldcolor)

    def orangesRotting(self, grid):
        queue=deque()
        m=len(grid)
        n=len(grid[0])
        freshOrange=0
        time=-1
        for  r in range(m):
            for c in range(n):
                if grid[r][c]==2:
                    queue.append([r,c])
                elif grid[r][c]==1:
                    freshOrange+=1
        
        if freshOrange==0:
            return 0
        if len(queue)==0:
            return -1
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while len(queue)>0:
            size=len(queue)
            while size>0:
                r,c=queue.popleft()
                for dir in directions:
                    newR=r+dir[0]
                    newC=c+dir[1]
                    if newR>=0 and newC>=0 and newR<m and newC<n and grid[newR][newC]==1:
                        grid[newR][newC]=2
                        queue.append([newR,newC])
                        freshOrange-=1
                size-=1
            time+=1         

    
        return time if freshOrange==0 else -1

print(Solution().orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))