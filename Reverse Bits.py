class Solution:
    def reverseBits(self, n: int) -> int:
        res=0 #all 32 bits are initialized as 0

        for i in range(32):
            #do right shift of all bits and and logical and with 1 to separate out single bit
            bit=(n>>i) & 1
            #0 or 1 should be 1 placed at the end in res
            res=res | (bit << (31-i))

        return res

print(Solution().reverseBits(43261596))