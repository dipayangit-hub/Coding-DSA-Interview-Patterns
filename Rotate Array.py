class Solution(object):
    def reverse(self,nums,i,j):
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        
    def rotate(self, nums, k):
        n=len(nums)
        #if k>size of array, do modulus as ex- K=5 and n=4 , the arrangement of elements at K=1 is similar to k=5 asat k=size of array, all elements will be in initial position
        if k>n:
            k%=n
        #total array reverse first
        self.reverse(nums,0,n-1)
        #array reverse till k-1
        self.reverse(nums,0,k-1)
        #array reverse till last from k
        self.reverse(nums,k,n-1)   
        return nums
    

print(Solution().rotate([1,2,3,4,5,6,7],8))