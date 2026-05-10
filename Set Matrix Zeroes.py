class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        firstrow,firstcol=False,False
        #first make the first row and first column as zero depending on zeros in the rest of the inner matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i==0:
                        firstrow=True
                    if j==0:
                        firstcol=True
                    matrix[i][0]=0
                    matrix[0][j]=0
        #next-> convert the inner natrix to 0s depending on if there is a zero in first row or first column
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        #check if there is an actual 0 in first row / column, mark entire first row and col as 0
        if firstcol:
            for i in range(m):
                matrix[i][0]=0
        if firstrow:
            for j in range(n):
                matrix[0][j]=0


                    
        return matrix


print(Solution().setZeroes([[1,0,3]]))

