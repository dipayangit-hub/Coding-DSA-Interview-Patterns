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


   def validparenthesis(self,s:str):
       stack=[]
       opening=['(','{','[']
       closing=[')','}',']']
       c=0
       for i in s:
           if i in opening:
               stack.append(i)
           elif i in closing:
               if not stack:
                   return False
               top=stack[-1]
               if (top == opening[0] and i==closing[0]) or (top == opening[1] and i==closing[1]) or (top == opening[2] and i==closing[2]):
                   stack.pop()
               else:
                   return False
           elif i =='*':
               c+=1
       if not stack:
           return True
    
       return False
           


        
print(Solution().validparenthesis('(*)[{}()]'))
# print(Solution().isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1,ListNode(2)))))))        
    
# print(Solution().invertTree(TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))))