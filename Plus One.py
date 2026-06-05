class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        c=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]=digits[i]+c
                return digits
            sum=digits[i]+c
            c=sum//10
            sum%=10
            digits[i]=sum

        return [1]+digits

print(Solution().plusOne([8,9,9,9]))