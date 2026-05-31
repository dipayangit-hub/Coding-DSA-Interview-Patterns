class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        k=k%n
        if k==0:
            return head
        
        size=n-k
        
        curr,prev=head,None
        while size>0:
            prev=curr
            curr=curr.next
            size-=1
        
        point=curr
        prev.next=None
        while curr.next:
            curr=curr.next
        curr.next=head

        return point
    
print(Solution().rotateRight(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),2))



