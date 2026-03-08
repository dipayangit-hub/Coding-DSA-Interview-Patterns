class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    slow,fast=head,head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False


def detectCycle(head: ListNode) -> ListNode:
    slow,fast=head,head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            fast=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
    return None


def isHappy( n: int) -> bool:
    def sq(n):
        ans=0
        while n>0:
            r=n%10
            n//=10
            ans+=r*r
        return ans
    slow,fast=sq(n),sq(sq(n))
    if slow==fast:
        return True
    while slow!=fast:
        if slow==1 or fast==1:
            return True
        slow=sq(slow)
        fast=sq(sq(fast))
       
    return False



        
    

# l = ListNode(3)
# l.next = ListNode(2)
# l.next.next = ListNode(0)
# l.next.next.next = l.next
print(isHappy(1))