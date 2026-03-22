class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res=[]
        for i in range(len(nums)):
            #duplicate check for i
            if i>0 and nums[i-1]==nums[i]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==0:
                    temp=[nums[i],nums[l],nums[r]]
                    res.append(temp)
                    l+=1
                    r-=1
                    #duplicate check for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    #duplicate check for r
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum<0:
                    l+=1
                else:
                    r-=1
        return list(res)


        



print(Solution().threeSum([1,2,0,1,0,0,0,0]))