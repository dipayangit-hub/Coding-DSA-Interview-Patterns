from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        res=[]
        queue=deque()
        c=0
        queue.append(root)
        while len(queue)>0:
            temp=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if c%2!=0:
                    temp.insert(0,node.val)
                else:
                    temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
            c+=1
        return res
    
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=deque()
        queue.append(root)
        height=1
        while len(queue)>0:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if node.right==None and node.left==None:
                    return height
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            height+=1
        return height
    

    def maxLevelSum(self, root: TreeNode) -> int:
            if not root:
                return 0
            queue=deque()
            queue.append(root)
            maxsum,maxlevel=float('-inf'),0
            height=1
            while len(queue)>0:
                size=len(queue)
                sum=0
                for i in range(size):
                    node=queue.popleft()
                    sum+=node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if maxsum < sum:
                    maxsum,maxlevel=sum,height
                height+=1
            return maxlevel
        
print(Solution().maxLevelSum(TreeNode(1,TreeNode(7,TreeNode(7),TreeNode(-8)),TreeNode(0))))