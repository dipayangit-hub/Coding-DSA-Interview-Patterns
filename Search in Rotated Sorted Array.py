class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[l]:
                if target>=nums[l] and target<=nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            elif nums[mid]<=nums[r]:
                if target>=nums[mid] and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
    
print(Solution().search([4,5,6,7,0,1,2,3,4],6))
