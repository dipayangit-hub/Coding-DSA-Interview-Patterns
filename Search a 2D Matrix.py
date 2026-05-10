class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int):
        m=len(matrix)
        n=len(matrix[0])
        l,r=0,(m*n)-1

        while l<=r:
            mid=(l+r)//2
            row=mid//n
            c=mid%n
            if matrix[row][c]==target:
                return True
            elif matrix[row][c] < target:
                l=mid+1
            else:
                r=mid-1
        return False
    
print(Solution().searchMatrix([[1,1]],2))