class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right>left:
            right=right&(right-1)
        return right

    

print(Solution().rangeBitwiseAnd(left = 0, right = 0))