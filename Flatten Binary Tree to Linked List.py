class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    next=None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root==None:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.left=None
        root.right=self.next
        self.next=root
        return self.next
        

print(Solution().flatten(TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,None,TreeNode(6)))))
        