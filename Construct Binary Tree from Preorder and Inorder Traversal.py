class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        inordermap={}
        for i in range(len(inorder)):
            inordermap[inorder[i]]=i
        rootIndex=0
        def split_tree(preorder,inordermap,left,right):
            nonlocal rootIndex
            if left>right:
                return None
            root=TreeNode(preorder[rootIndex])
            rootIndex+=1
            mid=inordermap[root.val]

            root.left=split_tree(preorder,inordermap,left,mid-1)
            root.right=split_tree(preorder,inordermap,mid+1,right)
            return root
        return split_tree(preorder,inordermap,0,len(inorder)-1)
    
Solution().buildTree([3,9,20,15,7],[9,3,15,20,7])


