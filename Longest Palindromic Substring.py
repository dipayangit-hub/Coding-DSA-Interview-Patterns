class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=0
        maxlen=""
        while i<len(s):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                s1=s[l:r+1]
                if len(maxlen)<len(s1):
                    maxlen=s1
                l-=1
                r+=1
            
            l,r,=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                s1=s[l:r+1]
                if len(maxlen)<len(s1):
                    maxlen=s1
                l-=1
                r+=1
            i+=1
        return maxlen
                        
    
print(Solution().longestPalindrome("tattarrattat"))

