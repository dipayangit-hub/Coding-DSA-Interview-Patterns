class Solution(object):
    def reverseWords(self, s):
        i,j=len(s)-1,len(s)-1
        res=""
        while j>=0 and j<=i:
            if s[j]==" ":
                res+=s[j+1:i+1]
                res+=" "
                while j>=0 and s[j]==" ":
                    j-=1
                i=j
            else:
                j-=1
            
        if i>=0:
            res+=s[0:i+1]
            
        return res.strip()
            
            
            
print(Solution().reverseWords(" the sky is blue "))