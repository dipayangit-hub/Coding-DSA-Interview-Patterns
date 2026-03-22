class Solution(object):
    def smallestNumber(self, n):
        k=n.bit_length()
        for i in range(k):
            if n & (1<<i) ==0:
                n=n|(1<<i)
        return n
    

print(Solution().smallestNumber(5))


# | Expression | In words                   | Value |
# | ---------- | -------------------------- | ----- |
# | `1 << 0`   | 1 shifted left by 0 places | 1     |
# | `1 << 1`   | 1 shifted left by 1 place  | 2     |
# | `1 << 2`   | 1 shifted left by 2 places | 4     |
# | `1 << 3`   | 1 shifted left by 3 places | 8     |
