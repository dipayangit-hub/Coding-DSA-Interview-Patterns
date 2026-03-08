from collections import deque
import heapq

class MyQueue(object):
    def __init__(self):
        st1,st2=[],[]
        self.st1=st1
        self.st2=st2

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st1.append(x)        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.st2)==0:
            while len(self.st1)>0:
                self.st2.append(self.st1.pop())
        return self.st2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.st2)==0:
            while len(self.st1)>0:
                self.st2.append(self.st1.pop())

        return self.st2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.st1)==0 and len(self.st2)==0

# obj = MyQueue()
# obj.push(1)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# param_4 = obj.empty()

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class Solution(object):
    def levelOrder(self, root):
        queue=deque()
        res=[]
        if root==None:
            return res
        queue.append(root)
        res.append([root.val])
        while len(queue)>0:
            temp=[]
            size=len(queue)
            for i in range(size):
                q=queue.popleft() 
                if q.left!=None:
                    queue.append(q.left)
                    temp.append(q.left.val)
                if q.right!=None:
                    queue.append(q.right)
                    temp.append(q.right.val)
            if len(temp)>0:    
                res.append(temp)
        return res   
    
    def findKthLargest(self, nums, k):
        pq=[]
        for i in nums:
            heapq.heappush(pq,i)
            if len(pq)>k:
                heapq.heappop(pq)
        return pq[0]
    
# print(Solution().levelOrder(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))
print(Solution().findKthLargest([3,2,1,5,6,4],2))
           
               
        
