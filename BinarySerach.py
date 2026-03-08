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


   def binarysearch(self,li:List,target):
        def search(li,low,high,target):
            if low>high:
                return -1
            mid=int(low +(high-low)/2)
            if li[mid]==target:
                return mid
            elif li[mid]<target:
                return search(li,mid+1,high,target)
            return search(li,low,mid-1,target)
        return search(li,0,len(li)-1,target)



   
           


        
print(Solution().binarysearch([3,4,6,7,9,12,16,17],6))
# print(Solution().isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1,ListNode(2)))))))        
    
# print(Solution().invertTree(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))))