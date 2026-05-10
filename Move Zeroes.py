class Solution(object):
    def moveZeroes(self, nums):
        insertpos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insertpos]=nums[i]
                insertpos+=1
        #make remaining elements as 0
        while insertpos<len(nums):
            nums[insertpos]=0
            insertpos+=1
        return nums


    

print(Solution().moveZeroes([0,1,5,0,12,0,9]))