class Solution(object):
    def subarraysDivByK(self, nums, k):
        map={}
        sum=0
        count=0
        map[0]=1
        for i in range(len(nums)):
            sum+=nums[i]
            #prefix sum
            rem=sum%k
            if rem<0:
                #if rem is negative store the positive counterpart in the map - (-2%6)=-2 which is same as (-2+6)%6=4
                rem+=k
            if rem in map:
                #store the count of previous occurences of the remainder in map and get it when seen same remainder again
                count+=map[rem]
            map[rem]=map.setdefault(rem,0)+1
        return count




print(Solution().subarraysDivByK([4,5,0,-2,-3,1],5))