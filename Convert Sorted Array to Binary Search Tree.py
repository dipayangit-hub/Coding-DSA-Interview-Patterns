class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def recurse(l,r):
            if l>r:
                return None
            mid=l+(r-l)//2
            root=TreeNode(nums[mid])
            root.left=recurse(l,mid-1)
            root.right=recurse(mid+1,r)

            return root
            
        return recurse(0,len(nums)-1)

            
print(Solution().sortedArrayToBST([-10,-3,0,5,9]))