class Solution(object):
    def findDuplicate(self, nums):
        slow,fast=0,0
        while True:
            # move slow by 1, fast by 2, referring to the indices and the vallues of nums array as nums.length == n + 1 and 1 <= nums[i] <= n
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        slow=0
        while slow!=fast:
            #move by same speed once they end up at same index in previous loop as it indicates a cycle(similar to cycle in linkedlist list) and the very first index, where they become equal next again is the result
            slow=nums[slow]
            fast=nums[fast]
        
        return slow



print(Solution().findDuplicate([1,3,4,2,2]))