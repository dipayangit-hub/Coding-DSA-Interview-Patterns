class Solution(object):
    def strStr(self, haystack, needle):
       m=len(haystack)
       n=len(needle)
       #iterate till length haystck_len-needle_len as any char coming after that cant form entire needle string
       for i in range(m-n+1):
            j=0
            while j<n and haystack[i+j]==needle[j]:
                j+=1
            if j==n:
                return i
       return -1
print(Solution().strStr("saybutsad","sad"))

