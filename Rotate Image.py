class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        
        #First transpose matrix
        #diagonal stays same and if we draw a line on diagonal , the other elements can be swapped
        #for 0-> travel from 1 to 3, for 1-> 2 to 3, for 2->1
        for i in range(n-1):
            for j in range(i+1,n):
                #swap it
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        #2nd -> reverse every row
        for i in range(n):
            j,k=0,n-1
            while j<k:
                matrix[i][j],matrix[i][k]=matrix[i][k],matrix[i][j]
                j+=1
                k-=1
        return matrix

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))