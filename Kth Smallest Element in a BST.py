class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #Recursive
        # def inorder(root,k):
        #     if not root:
        #         return None,k
        #     ans,k=inorder(root.left,k)
        #     if ans is not None:
        #         return ans,k
        #     k-=1
        #     if k==0:
        #         return root.val,k
        #     return inorder(root.right,k)
        
        # ans,_=inorder(root,k)
        # return ans

        #Iterative
        st=[]
        while len(st)>0 or root:
            while root:
                st.append(root)
                root=root.left
            
            root=st.pop()
            k-=1

            if k==0:
                return root.val
            
            root=root.right


print(Solution().kthSmallest(TreeNode(5,TreeNode(3,TreeNode(2,TreeNode(1)),TreeNode(4)),TreeNode(6)),4))