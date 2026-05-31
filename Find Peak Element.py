class Solution:
    def findPeakElement(self, nums: list[int]):
        if len(nums)==1:
            return 0
        l,r=0,len(nums)-1
        #check if 1st and las elements are peaks , return them , else do binary search
        if nums[l]>nums[l+1]:
            return l
        elif nums[r]>nums[r-1]:
            return r
        l+=1
        r-=1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                l=mid+1
            elif nums[mid]<nums[mid-1]:
                r=mid-1
print(Solution().findPeakElement([6,7,10,7,7]))