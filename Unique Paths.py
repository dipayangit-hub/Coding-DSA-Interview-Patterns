class Solution(object):
    #memoization
    # def uniquePaths(self, m, n):
    #     return self.dfs(0,0,m,n,[])
        
    # def dfs(self,i,j,m,n,dp):
    #     if len(dp)==0:
    #         dp=[[-1 for _ in range(n)] for _ in range(m)]
    #     if i>=m or j>=n:
    #         return 0
    #     elif i==m-1 and j==n-1:
    #         return 1
    #     if dp[i][j]!=-1:
    #         return dp[i][j]
    #     #have separate counts for all paths and let parent maintain the acumulation all correct paths of its child
    #     dp[i][j]=self.dfs(i+1,j,m,n,dp)+ self.dfs(i,j+1,m,n,dp)
    #     #starting pint accumulates the no. of total paths to end node, hence returning it
    #     return  dp[i][j]

    #Tabulation
    # def uniquePaths(self, m, n):
        #initialize all zeroes
        # dp=[[0 for _ in range(n)] for _ in range(m)]
        
        # i,j=0,0
        # for i in range(m):
        #     for j in range(n):
        #         #for rows or columns with 0, i.e. first column or row cell, no. of paths can always be 1 as either down or up will not be there
        #         if i==0 or j==0:
        #             dp[i][j]=1
        #         else:
        #             # for other cells its a summation of up and left cells
        #             dp[i][j]=dp[i-1][j]+dp[i][j-1]

        # return dp[m-1][n-1]

    
    #Tabulation - optimized
    def uniquePaths(self, m, n):
        #array for holding values for all columns in previous row(for 1st row no. of paths is always 1)
        prev_r=[1 for _ in range(n)]
        for i in range(1,m):
            #array for holding current row values , where first column value no. of paths is always 1
            curr_r=[0 for _ in range(n)]
            curr_r[0]=1
            #current_cell path= previous row same column path and previous column same row path
            for j in range(1,n):
                curr_r[j]=prev_r[j]+curr_r[j-1]
            #make previous row as current row for calculating next row
            prev_r=curr_r
        #return the last column value for previous array(which is last row)
        return prev_r[n-1]
    


    



print(Solution().uniquePaths(3,2))


        

