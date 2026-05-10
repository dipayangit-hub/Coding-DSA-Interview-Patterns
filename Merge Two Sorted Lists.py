# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        res=ListNode()
        head=res
        while list1 and list2:
            if list1.val<=list2.val:
                head.next=ListNode(list1.val)
                list1=list1.next
            else:
                head.next=ListNode(list2.val)
                list2=list2.next
            head=head.next

        while list1:
             head.next=ListNode(list1.val)
             list1=list1.next
             head=head.next

        while list2:
            head.next=ListNode(list2.val)
            list2=list2.next
            head=head.next
        return res.next

print(Solution().mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))), ListNode(1,ListNode(3,ListNode(4)))))
