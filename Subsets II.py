class Solution(object):
    def subsetsWithDup(self, nums):
        res=[]
        l=[]
        nums.sort()
        self.subsets(nums,0,res,l)
        return res
    
    def subsets(self,nums,i,res,l):
        if i>=len(nums):
            res.append(l[:])
            return res
        #take
        l.append(nums[i])
        self.subsets(nums,i+1,res,l)
        #skipping duplicate values
        index=i+1
        while index<len(nums) and nums[index]==nums[index-1]:
            index+=1
        #nottake
        l.pop()
        self.subsets(nums,index,res,l)

print(Solution().subsetsWithDup([1,2,2,3 ]))