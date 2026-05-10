class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [self.getleftbound(nums,target),self.getrightround(nums,target)]
    
    def getleftbound(self,nums,target):
        l,r=0,len(nums)-1
        index=-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                index=mid
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return index

    def getrightround(self,nums,target):
        l,r=0,len(nums)-1
        index=-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                index=mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return index    
    
print(Solution().searchRange([5,7,7,8,8,10],8))
