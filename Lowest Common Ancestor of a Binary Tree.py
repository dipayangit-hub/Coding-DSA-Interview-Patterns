class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        elif root==p or root==q:
           return root
        
        llca=self.lowestCommonAncestor(root.left,p,q)
        rlca=self.lowestCommonAncestor(root.right,p,q)

        if llca and rlca:
            return root
        elif llca:
            return llca
        else:
            return rlca
        
        
        

       
p=TreeNode(5)
p_rr=TreeNode(4)
root=TreeNode(3)
p_l=TreeNode(6)
p_r=TreeNode(2)
p_rl=TreeNode(7)

r_r=TreeNode(1)
q=TreeNode(0)
r_rr=TreeNode(8)

root.left=p
root.right=r_r
p.left=p_l
p.right=p_r
p_r.left=p_rl
p_r.right=p_rr
r_r.left=q
r_r.right=r_rr
print(Solution().lowestCommonAncestor(root,p,q))
