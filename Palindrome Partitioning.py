class Solution:
    def partition(self, s: str):
        res=[]
        def combinations(s,l):
            if len(s)==0:
                res.append(l[:])
                return        
            for i in range(len(s)):
                part=s[:i+1]
                if self.ispalindrome(part):
                    l.append(part)
                    combinations(s[i+1:],l)
                    l.pop()
        combinations(s,[])
        return res

    def ispalindrome(self,s):
            l,r=0,len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
    
print(Solution().partition("aab"))