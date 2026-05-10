class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode):
            prev=None
            res=float('inf')

            def inorder(root):
                 nonlocal prev, res
                 if not root:
                      return
                 
                 inorder(root.left)

                 if prev!=None:
                    res=min(res,root.val-prev.val)
                 prev=root

                 inorder(root.right)
            inorder(root)

            return res
                 
    
print(Solution().getMinimumDifference(TreeNode(1,TreeNode(0),TreeNode(5,TreeNode(3)))))