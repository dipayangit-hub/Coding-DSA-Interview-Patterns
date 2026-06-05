class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        l,r=0,len(n)-1
        while l<r:
            if n[l]!=n[r]:
                return False
            l+=1
            r-=1
        return True

print(Solution().isPalindrome(-121))