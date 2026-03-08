class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        dummy=ListNode(0,head)
        prev,cur=head,head.next
        while cur:
            if cur.val>=prev.val:
                prev,cur=cur,cur.next
                continue
            temp=dummy
            while temp.next.val<=cur.val:
                temp=temp.next
            prev.next=cur.next
            cur.next=temp.next
            temp.next=cur
            cur=prev.next


        return dummy.next
    
print(Solution().insertionSortList(ListNode(2,ListNode(4,ListNode(1,ListNode(3))))))
