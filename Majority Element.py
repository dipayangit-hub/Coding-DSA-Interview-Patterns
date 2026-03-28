class Solution(object):
    def majorityElement(self, nums):
        count,el=0,0
        n=len(nums)
        #Moore's algorithm
        for i in range(n):
            if count==0:
                el=nums[i]
                count=1
                continue
            if nums[i]==el:
                count+=1
            else:
                count-=1
        #verify if majority element actually ecists for the element for which we got count>0
        count==0
        for i in range(n):
            if el==nums[i]:
                count+=1
            if count>(n//2):
                return el
        return -1


print(Solution().majorityElement([2,2,1,1,1,2,2]))