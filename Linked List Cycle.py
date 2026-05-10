class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow,fast=head,head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

a=ListNode(3)
b=ListNode(2)
c=ListNode(0)
d=ListNode(-4)
a.next=b
b.next=c
c.next=d
d.next=b

print(Solution().hasCycle(a))
        

