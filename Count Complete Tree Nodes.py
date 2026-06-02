from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        lh,rh=1,1

        l,r=root,root

        while l.left:
            l=l.left
            lh+=1
        
        while r.right:
            r=r.right
            rh+=1
        
        if lh==rh:
            return (2**lh-1)
        else:
            left=self.countNodes(root.left)
            right=self.countNodes(root.right)
            return 1+left+right

        

left=TreeNode(2,TreeNode(4),TreeNode(5))
right=TreeNode(3,TreeNode(6))
print(Solution().countNodes(TreeNode(1,left,right)))