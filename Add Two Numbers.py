class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head=ListNode(0)
        p=head
        c=0
        while l1 or l2 or c:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            sum=val1+val2+c
            c=sum//10
            p.next=ListNode(sum%10)
            p=p.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        
        return head.next

print(Solution().addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))), ListNode(5,ListNode(6,ListNode(4)))))
