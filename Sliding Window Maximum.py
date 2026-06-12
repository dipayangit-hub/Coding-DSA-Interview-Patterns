from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q=deque()
        res=[]
        #for 1st k size window
        for i in range(k):
            while len(q) and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        
        l=1
        #for further elements
        for i in range(k,len(nums)): 
            while len(q) and q[0]<l:
                q.popleft()

            while len(q) and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
            l+=1
        
        return res

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))


