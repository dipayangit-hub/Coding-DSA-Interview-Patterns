import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int):
        pq=[]
        for i in nums:
            heapq.heappush(pq,i)
            if len(pq)>k:
                heapq.heappop(pq)
        return pq[0]
print(Solution().findKthLargest([3,2,1,5,6,4],2))