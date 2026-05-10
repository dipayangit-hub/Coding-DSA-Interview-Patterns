class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        temp=head
        map={}
        while temp:
            map[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if temp.next:
                map[temp].next=map[temp.next]
            if temp.random:
                map[temp].random=map[temp.random]
            temp=temp.next
        return map[head] if head else head


nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]

# Step 2: connect next pointers
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

# Step 3: connect random pointers
nodes[0].random = None
nodes[1].random = nodes[0]
nodes[2].random = nodes[4]
nodes[3].random = nodes[2]
nodes[4].random = nodes[0]

# head
head = nodes[0]
print(Solution().copyRandomList(head))
            

