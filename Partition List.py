class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        s,l=ListNode(-1),ListNode(-1)
        s1,l1=s,l
        temp=head
        while temp:
            if temp.val<x:
                s1.next=temp
                s1=s1.next
            else:
                l1.next=temp
                l1=l1.next
            temp=temp.next
        
        l1.next=None
        s1.next=l.next
        return s.next
        
                
    
print(Solution().partition(ListNode(1,ListNode(4,ListNode(3,ListNode(2,ListNode(5,ListNode(2)))))),3))



        