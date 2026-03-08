from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:


   def noofsubarrays(self,li:List,k:int):
        map={}
        pref_sum,c=0,0
        i=0
        map.__setitem__(0,1)
        while i<len(li):
            pref_sum+=li[i]
            rem=pref_sum-k
            c+=map.get(rem,0)
            map.__setitem__(pref_sum,map.get(pref_sum,0)+1)
            i+=1
        return c
   
           


        
print(Solution().noofsubarrays([1,2,3,-3,1,1,1,4,2,-3],3))
# print(Solution().isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1,ListNode(2)))))))        
    
# print(Solution().invertTree(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))))