class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                break

        if not fast or not fast.next:
            return None
        
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        
        return slow
    

A=ListNode(3)
a=ListNode(2)
b=ListNode(0)
c=ListNode(-4)
A.next=a
a.next=b
b.next=c
c.next=a
print(Solution().detectCycle(A))
