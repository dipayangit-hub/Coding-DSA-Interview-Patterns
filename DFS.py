class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) ->TreeNode:
        if root==None:
            return None
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
            if not root:
                 return 0
            
            sum=0
            if root.left and root.left.left==None and root.left.right==None:
                 sum+=root.left.val
            
            sum+=self.sumOfLeftLeaves(root.left)
            sum+=self.sumOfLeftLeaves(root.right)
            return sum
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
         if not root:
              return False
         if root.left==None and root.right==None:
              return True if targetSum==root.val else False
         
         left=self.hasPathSum(root.left,targetSum-root.val)
         right=self.hasPathSum(root.right,targetSum-root.val) 
         return left or right       
          
    def isBalanced(self, root: TreeNode) -> bool:
         if root==None:
              return True
         return False if self.checkheight(root)==-1 else True

    def checkheight(self,root):
         if root==None:
              return 0
         l=self.checkheight(root.left)
         if l==-1:
              return -1
         r=self.checkheight(root.right)
         if r==-1:
              return -1

         if abs(l-r)>1:
              return -1
         
         return max(l,r)+1

#recursive
#     def maxDepth(self, root: TreeNode) -> int:
     #     if not root:
     #          return 0
     #     l=self.maxDepth(root.left)
     #     r=self.maxDepth(root.right)
     #     return max(l,r)+1

#iterative

    def maxDepth(self, root: TreeNode) -> int:
         if not root:
              return 0
         st=[]
         st.append([root,1])
         maxdepth=0
         while len(st)>0:
               node,depth=st.pop()
               maxdepth=max(depth,maxdepth)
               if node.left:
                    st.append([node.left,depth+1])
               if node.right:
                    st.append([node.right,depth+1])
         return maxdepth


print(Solution().maxDepth(TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(9))),TreeNode(3,None,TreeNode(5)))))