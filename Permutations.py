class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]

        def backtrack(nums,l):
            if len(l)==len(nums):
                res.append(l[:])
                return


            for num in nums:
                if len(l)>0 and num in l:
                    continue
                l.append(num)
                backtrack(nums,l)
                l.pop()
                
        backtrack(nums,[])
        return res
    
print(Solution().permute([1,2,3]))

            