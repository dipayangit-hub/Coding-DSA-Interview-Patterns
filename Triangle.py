class Solution:
    def minimumTotal(self, triangle: list[list[int]]):
        m=len(triangle)
        for r in range(m-2,-1,-1):
            for c in range(len(triangle[r])): 
                triangle[r][c]+=min(triangle[r+1][c],triangle[r+1][c+1])
        return triangle[0][0]



print(Solution().minimumTotal([[-1],[2,3],[1,-1,-3]]))