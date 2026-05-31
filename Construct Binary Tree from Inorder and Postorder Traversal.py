class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        inorderMap={}
        for i in range(len(inorder)):
            inorderMap[inorder[i]]=i
        rootIndex=-1
        def split_tree(inorderMap,postorder,left,right):
            nonlocal rootIndex
            if left>right:
                return None
            root=TreeNode(postorder[rootIndex])
            mid=inorderMap[postorder[rootIndex]]
            rootIndex-=1
            root.right=split_tree(inorderMap,postorder,mid+1,right)
            root.left=split_tree(inorderMap,postorder,left,mid-1)
            return root
        return split_tree(inorderMap,postorder,0,len(inorder)-1)
    
print(Solution().buildTree([4, 2, 5, 1, 6, 3, 7],[4, 5, 2, 6, 7, 3, 1]))