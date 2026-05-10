class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        maxlevel=0
        def traverse(root,level,res):
            nonlocal maxlevel
            if not root:
                return
            if maxlevel<level:
                maxlevel=level
                res.append(root.val)
            traverse(root.right,level+1,res)
            traverse(root.left,level+1,res)
        res=[]
        traverse(root,1,res)
        return res
    
print(Solution().rightSideView(TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(5))),TreeNode(3))))
        