def subsets(arr):
    #i->index, curr-> current result , res -> final result List<List<int>>
    def backtrack(i,arr,curr,res):
        #add curr to final result
        res.append(curr.copy())
        for i in range(i,len(arr)):
            #add element to current result
            curr.append(arr[i])
            #check for all combinations
            backtrack(i+1,arr,curr,res)
            #remove newly added elemnt
            curr.pop(-1)
        return res

    
    return backtrack(0,arr,[],[])


def ratinamaze(mat:list):
    n=len(mat)
    visited=[[False for _ in range(n)]for _ in range(n)]
    res=[]
    if mat[0][0]==1:
        backtrack(0,0,n,mat,"",visited,res)
    return res

def backtrack(i,j,n,mat,curr,visited,res):
        #base condition- last cell
        if i==n-1 and j==n-1:
            res.append(curr)
            return
        dirs=[[1,0,'D'],[0,-1,'L'],[0,1,'R'],[-1,0,'U']]
        visited[i][j]=True

        # recurse accross each direction
        for dir in dirs:
            nextRow=i+dir[0]
            nextcol=j+dir[1]
            move=dir[2]

            if nextRow>=0 and nextcol>=0 and nextRow<n and nextcol<n and not visited[nextRow][nextcol] and mat[nextRow][nextcol]==1:
                backtrack(nextRow,nextcol,n,mat,curr+move,visited,res)
        # backtrack removes the strings formed- DDRU-> wiith first backtrack -> DDR
        # make visited false as we are assuming the path isnt traversed yet and we will follow some other path which might go through this
        visited[i][j]=False
       

print(ratinamaze([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]))

