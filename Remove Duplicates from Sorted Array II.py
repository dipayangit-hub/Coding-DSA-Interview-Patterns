class Solution(object):
    def removeDuplicates(self, nums):
        j=2
        #Start i and j from 2 as first 2 elements can either be unique or duplicate but problem say atmost 2 duplicates allowed
        for i in range(2,len(nums)):
            #j should always be the element > 2 where the actual issue is
            #The element 2 positions before the current insertion point, hence nums[j-2]; That means we already have 2 copies, so we skip and increment i, keeping j ther to track the duplicate and replace with next unique element
            if nums[i]!=nums[j-2]:
                nums[j]=nums[i]
                j+=1
        return j
    

print(Solution().removeDuplicates([0,0,1,1,1,2,2,2,2,3,3]))