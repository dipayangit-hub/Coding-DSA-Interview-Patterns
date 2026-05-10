class Solution(object):
    def maxArea(self, height):
        l,r=0,len(height)-1
        maxarea=0
        while l<r:
            maxarea=max(maxarea,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxarea
    
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))