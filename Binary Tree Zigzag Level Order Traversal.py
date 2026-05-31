from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        
        q=deque()
        q.append(root)
        level=0
        res=[]
        while len(q):
            temp=[]
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if level%2==0:
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
            level+=1
        return res

                    
print(Solution().zigzagLevelOrder(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))
        