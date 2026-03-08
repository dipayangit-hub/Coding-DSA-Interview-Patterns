from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
            if root==None:
              return 0
            lcount=self.maxDepth(root.left)
            rcount=self.maxDepth(root.right)

            return max(lcount,rcount)+1

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if q==None and p==None:
            return True
        elif p==None or q==None:
            return False
        elif p.val!=q.val:
            return False
        return  self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

#recursive solution
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def compare(p,q):
    #         if q==None and p==None:
    #             return True
    #         elif p==None or q==None:
    #             return False
    #         elif p.val!=q.val:
    #             return False
    #         return  compare(p.left,q.left) and compare(p.right,q.right)
        
        # return compare(root.left,root.right) if root else True
    
#iterative solution
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque()

        if root:
            queue.append((root.left, root.right))

        while queue:
            p, q = queue.popleft()

            if p is None and q is None:
                continue
            if p is None or q is None or p.val != q.val:
                return False

            queue.append((p.left, q.right))
            queue.append((p.right, q.left))

        return True
    
print(Solution().isSymmetric(TreeNode(1,TreeNode(2,None,TreeNode(3,None, TreeNode(4,TreeNode(5),None))), TreeNode(2,TreeNode(3,TreeNode(4,None,TreeNode(5)), None)))))