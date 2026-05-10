class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
       dummy=ListNode(-1)
       dummy.next=head
       prev,curr=dummy,head
       while curr:
           if curr.next!=None and curr.val==curr.next.val:
                while curr.next!=None and curr.val==curr.next.val:
                    curr=curr.next
                prev.next=curr.next
           else:
               prev=prev.next
           curr=curr.next

       return dummy.next


print(Solution().deleteDuplicates(ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))))