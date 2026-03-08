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


    def middleoflinkedlist(self, head: ListNode):
        slow,fast=head,head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow



   
           


        
print(Solution().middleoflinkedlist(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))))
# print(Solution().isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1,ListNode(2)))))))        
    
# print(Solution().invertTree(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))))