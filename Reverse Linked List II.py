class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy=ListNode(-1)
        dummy.next=head
        prefix,curr=dummy,head
        c=1
        while c<left:
            prefix=prefix.next
            curr=curr.next
            c+=1
        
        prev=None
        next=None
        c=left
        start=curr
        while c<=right:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            c+=1
        
        prefix.next=prev
        start.next=curr

        
        return dummy.next
    
print(Solution().reverseBetween(ListNode(4,ListNode(8,ListNode(15,ListNode(16,ListNode(23,ListNode(42)))))),3,5))


        


        