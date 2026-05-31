class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast=head,head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        #reverse 3nd half
        shead=self.reverse(slow.next)
        temp1,temp2=head,shead
        while temp2:
            if temp1.val!=temp2.val:
                return False
            temp1=temp1.next
            temp2=temp2.next
        
        return True

    def reverse(self,head):
        curr,prev=head,None
        while curr:
            nxt=curr.next
            curr.next=prev

            prev=curr
            curr=nxt
        return prev
        
        

print(Solution().isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1))))))
        
