class Solution(object):
    def isPalindrome(self, s):
        def isvalid(c):
            return ('a' <= c <= 'z') or ('0' <= c <= '9')
        i,j=0,len(s)-1
        while i<j:
            ch=s[i].lower()
            ch1=s[j].lower()
            while i<j and not isvalid(ch):
                i+=1
                ch=s[i].lower()
            while i<j and not isvalid(ch1):
                j-=1
                ch1=s[j].lower()

            if ch!=ch1:
                return False
            i+=1
            j-=1
            
        return True
    
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))