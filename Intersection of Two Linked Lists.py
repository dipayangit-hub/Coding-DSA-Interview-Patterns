class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1,p2=headA,headB

        while p1!=p2:
            if p1:
                p1=p1.next
            else:
                p1=headB
            

            if p2:
                p2=p2.next
            else:
                p2=headA
        
        return p1

        

common=ListNode(8,ListNode(4,ListNode(5)))
print(Solution().getIntersectionNode(ListNode(4,ListNode(1,common)),ListNode(5,ListNode(6,ListNode(1,common)))))
