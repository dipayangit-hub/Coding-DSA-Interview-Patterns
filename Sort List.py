class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head

        middle=self.findmiddle(head)
        lefthead=head
        righthead=middle.next
        middle.next=None
        lefthead=self.sortList(lefthead)
        righthead=self.sortList(righthead)        

        return self.merge(lefthead,righthead)
    
    def findmiddle(self,head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next
        return slow
    
    def merge(self,lefthead,righthead):
        dummy=ListNode(float('-inf'))
        temp=dummy
        while lefthead and righthead:
            if lefthead.val<righthead.val:
                temp.next=lefthead
                temp=temp.next
                lefthead=lefthead.next
            else:
                temp.next=righthead
                temp=temp.next
                righthead=righthead.next
        if lefthead:
            temp.next=lefthead
        if righthead:
            temp.next=righthead
        return dummy.next
            

print(Solution().sortList(ListNode(4,ListNode(2,ListNode(1,ListNode(3))))))
                        



