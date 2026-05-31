class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    root=None
    st=[]
    def __init__(self, root: TreeNode):
        self.root=root
        self.storeleftnodes(self.root)    

    def next(self) -> int:
       if len(self.st):
           node=self.st.pop()
           if node.right:
               self.storeleftnodes(node.right) 
       return node.val
        


    def hasNext(self) -> bool:
        return len(self.st)>0

    def storeleftnodes(self,root):
        while root:
            self.st.append(root)
            root=root.left


bSTIterator =BSTIterator(TreeNode(7,TreeNode(5),TreeNode(15,TreeNode(9),TreeNode(20))))
print(bSTIterator.next())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())
print(bSTIterator.next())
print(bSTIterator.hasNext())
