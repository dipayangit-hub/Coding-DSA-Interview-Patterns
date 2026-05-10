class Solution(object):
    def majorityElement(self, nums):
        #moore's algo for 2 majority elements as for occuring n/3 times, max number of elements can be 2
        count1,count2=0,0
        el1,el2=0,0
        n=len(nums)
        for i in range(n):
            #consider 2 majority elements with 2 diff window depending on when count is 0 for each
            if el1==nums[i]:
                count1+=1
            elif el2==nums[i]:
                count2+=1
            elif count1==0:
                el1=nums[i]
                count1=1
            elif count2==0:
                el2=nums[i]
                count2=1
            else:
                count1-=1
                count2-=1
        count1,count2=0,0
        for i in range(n):
            if el1==nums[i]:
                count1+=1
            elif el2==nums[i]:
                count2+=1
        
        res=[]
        #Verify if the majority elements actually has count > n/3
        if count1>(n//3):
            res.append(el1)
        if count2>(n//3):
            res.append(el2)
        return res
            
print(Solution().majorityElement([2,1,1,3,1,4,5,6]))