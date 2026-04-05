class Solution(object):
    def productExceptSelf(self, nums):
        res=[1]*len(nums)
        #prefix calculation without creating separate array
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]
        #suffiX calc without creating separate array
        suffix=1
        for i in range(len(res)-2,-1,-1):
            suffix*=nums[i+1]
            #for every index the product of its prefix and suffix is the result, For [1,2,3,4]-> for arr[2], res=(2*1)*4
            res[i]*=suffix

        return res    
            
    

print(Solution().productExceptSelf([1,2,3,4]))