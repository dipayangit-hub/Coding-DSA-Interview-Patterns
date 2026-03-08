import heapq

# overiding comparator logic

class HeapKey:
    def __init__(self,key,ref_dict):
        self.key=key
        self.ref_dict=ref_dict

    def __lt__(self,other):
        return self.ref_dict[self.key]<self.ref_dict[other.key]

class Solution(object):
    def topKFrequent(self, nums, k):
        pq=[]
        map={}
        for i in nums:
            map[i]=map.setdefault(i,0)+1
        for key in map.keys():
            heapq.heappush(pq,HeapKey(key,map))
            if len(pq)>k:
                heapq.heappop(pq)
        res=[]
        while len(pq)>0:
            res.append(heapq.heappop(pq).key)
        return res

# using tuple for (value,key) where value is getting compared due to it being in index 0 in tuple

class Solution(object):
    def topKFrequent(self, nums, k):
        pq=[]
        map={}
        for i in nums:
            map[i]=map.setdefault(i,0)+1
        for key in map:
            heapq.heappush(pq,(map[key],key))
            if len(pq)>k:
                heapq.heappop(pq)
        res=[]
        while len(pq)>0:
            value,key=heapq.heappop(pq)
            res.append(key)
        return res

    def kthSmallest(self, matrix, k):
        n=len(matrix)
        pq=[]
        for i in range(n*n):
            heapq.heappush(pq,-matrix[i//n][i%n])
            if len(pq)>k:
                heapq.heappop(pq)
        return -heapq.heappop(pq)
print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))

