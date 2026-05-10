from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        queue=deque()
        if root:
            queue.append([root.left,root.right])
        
        while len(queue)>0:
            p,q=queue.popleft()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            queue.append([p.left,q.right])
            queue.append([p.right,q.left])
        return True
    
print(Solution().isSymmetric(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))))
