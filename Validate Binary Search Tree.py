class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def isBST(root,min,max):
            if not root:
                return True
            
            if root.val<=min:
                    return False
            
            if root.val>=max:
                    return False
        
            return isBST(root.left,min,root.val) and isBST(root.right,root.val,max)
        
        return isBST(root,float('-inf'),float('inf'))
    

print(Solution().isValidBST(TreeNode(2,TreeNode(2),TreeNode(2))))