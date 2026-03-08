import heapq
import itertools

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# overiding comparator logic

class Heap:
     def __init__(self,key):
        self.key=key

     def __lt__(self,other):
        return self.key.val < other.key.val
     
class Solution(object):
    def mergeKLists(self, lists):
        pq=[]
        head,curr=ListNode(0),None
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, Heap(lists[i]))
        while len(pq)>0:
            node=heapq.heappop(pq).key
            if curr:
                curr.next=ListNode(node.val)
                curr=curr.next
            else:
                curr=ListNode(node.val)
                head.next=curr
            if node.next:
                heapq.heappush(pq,(Heap(node.next)))
            
        return head.next

#passing tuple of node_val, counter(using generator function), node) 
class Solution(object):
    def mergeKLists(self, lists):
        pq=[]
        head,curr=ListNode(0),None
        counter = itertools.count()
        for i in range(len(lists)):
            node=lists[i]
            if node:
                heapq.heappush(pq, (node.val,next(counter),node))
        while len(pq)>0:
            node_val,index,node=heapq.heappop(pq)
            if curr:
                curr.next=node
                curr=curr.next
            else:
                curr=node
                head.next=curr
            if node.next:
                heapq.heappush(pq,(node.next.val,next(counter),node.next))
            
        return head.next

    def kSmallestPairs(self, nums1, nums2, k):
        pq,res=[],[]
        for i in range(min(len(nums1),k)):
                heapq.heappush(pq,(nums1[i]+nums2[0],[i,0]))
        while k>0 and len(pq)>0:
            i,j=heapq.heappop(pq)[1]
            res.append([nums1[i],nums2[j]])
            k-=1
            if j+1<len(nums2):
                heapq.heappush(pq,(nums1[i]+nums2[j+1],[i,j+1]))
           
        return res
# a=ListNode(1,ListNode(4,ListNode(5)))
# b=ListNode(1,ListNode(3,ListNode(4)))
# c=ListNode(2,ListNode(6))
print(Solution().kSmallestPairs([1,2,11],[2,4,6],3))