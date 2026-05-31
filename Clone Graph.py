from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        #BFS
        # q=deque()
        # map={}
        # head=None
        # if node:
        #     q.append(node)
        #     head=Node(node.val)
        #     map[node.val]=head
        # while len(q):
        #     node=q.popleft()
        #     for neighbor in node.neighbors:
        #         if neighbor.val not in map:
        #             map[neighbor.val]=Node(neighbor.val)
        #             q.append(neighbor)
        #         map[node.val].neighbors.append(map[neighbor.val])        
        # return head

        #DFS
        map={}
        if not node:
            return None
        map[node.val]=Node(node.val)
        def dfs(node):
            for neighbor in node.neighbors:
                if neighbor.val not in map:
                    map[neighbor.val]=Node(neighbor.val)
                    dfs(neighbor)
                map[node.val].neighbors.append(map[neighbor.val])  
        
        dfs(node)
        return map[node.val]
        
    
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Connect neighbors
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Input to function
root = node1
print(Solution().cloneGraph(root))

                    

        