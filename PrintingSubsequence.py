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


   def subsequence(self,l:list):
       def recursion(i,arr):
          if i>=len(l):
              print(arr)
              return
          arr.append(l[i])
          recursion(i+1,arr) #take
          arr.pop()
          recursion(i+1,arr) #not take
       recursion(0,[])


        
print(Solution().subsequence([3,2,1]))
# print(Solution().isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1,ListNode(2)))))))        
    
# print(Solution().invertTree(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))))