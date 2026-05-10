class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        def recurse(candidates,start,target,l):
            if target==0:
                res.append(l[:])
                return
            for i in range(start,len(candidates)):
                if target-candidates[i]>=0:
                    l.append(candidates[i])
                    recurse(candidates,i,target-candidates[i],l)
                    l.pop()
        recurse(candidates,0,target,[])       
        return res

print(Solution().combinationSum([2,3,5],8))