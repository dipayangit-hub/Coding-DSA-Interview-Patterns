from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        if not root:
            return []
        
        q=deque()
        q.append(root)
        res=[]
        while len(q):
            sum=0
            size=len(q)
            for i in range(size):
                node=q.popleft()
                sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum/size)
        return res
    
print(Solution().averageOfLevels(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))