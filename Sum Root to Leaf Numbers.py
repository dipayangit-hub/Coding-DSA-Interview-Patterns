class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.traverse(root,0)
    
    def traverse(self,root,cursum):
        if not root:
            return 0
        cursum=cursum*10+root.val
        if not root.left and not root.right:
            return cursum
        return self.traverse(root.left,cursum) + self.traverse(root.right,cursum)
        

print(Solution().sumNumbers(TreeNode(4,TreeNode(9,TreeNode(5),TreeNode(1)),TreeNode(0))))
            