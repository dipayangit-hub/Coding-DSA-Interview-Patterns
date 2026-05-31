class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res=[]

        def backtrack(path,sum,index):
            if sum>target:
                return
            elif sum==target:
                res.append(path[:])
                return
            
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(path,sum+candidates[i],i+1)
                path.pop()
            
        
        backtrack([],0,0)
        return res
    
print(Solution().combinationSum2([10,1,2,7,6,1,5],8))