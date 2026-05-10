# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head:ListNode, n: int) -> ListNode:
        length=0
        dummy=ListNode(-1)
        dummy.next=head
        temp=head
        while temp:
            length+=1
            temp=temp.next
        
        n=length-n
        curr=head
        prev=dummy
        while n>0:
            curr=curr.next
            prev=prev.next
            n-=1
        prev.next=curr.next
        return dummy.next
    
print(Solution().removeNthFromEnd(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),2))
        
        
           

