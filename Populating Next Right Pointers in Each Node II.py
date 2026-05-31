from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        queue=deque()
        if root:
            queue.append(root)
            queue.append(None)

        prev=None
        while len(queue):
            curr=queue.popleft()
            
            if curr:
                 if curr.left:
                     queue.append(curr.left)
                 if curr.right:
                     queue.append(curr.right)
                 if prev:
                     prev.next=curr
            else:
                if len(queue)!=0:
                    queue.append(None)
            prev=curr
            
        
        return root
    
print(Solution().connect(Node(1,Node(2,Node(4),Node(5)),Node(3,None,Node(7)))))
             
            
