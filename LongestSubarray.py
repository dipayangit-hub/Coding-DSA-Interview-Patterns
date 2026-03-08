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


   def longestsubarray(self,li:List,k:int):
        l, r = 0, 0
        window_sum = 0
        maxlen = 0
        
        while r < len(li):
            window_sum += li[r]
            
            # Shrink window from left if sum exceeds k
            if window_sum > k:
                window_sum -= li[l]
                l += 1
            
            # Update max length (now sum <= k is guaranteed)
            if window_sum<=k:
                maxlen = max(maxlen, r - l + 1)
            
            # Expand window from right
            r += 1
        
        return maxlen
        
   
           


        
print(Solution().longestsubarray([2,5,1,10,10],14))
# print(Solution().isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1,ListNode(2)))))))        
    
# print(Solution().invertTree(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))))