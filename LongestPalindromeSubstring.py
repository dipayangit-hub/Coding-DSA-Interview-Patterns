class Solution(object):
    def longestPalindrome(self, s):
        lps = ""

        for i in range(len(s)):

            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(lps) < (r - l + 1):
                    lps = s[l:r+1]
                l -= 1
                r += 1

            # even length palindrome
            l, r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(lps) < (r - l + 1):
                    lps = s[l:r+1]
                l -= 1
                r += 1

        return lps




        


print(Solution().longestPalindrome("acacbbaaab"))