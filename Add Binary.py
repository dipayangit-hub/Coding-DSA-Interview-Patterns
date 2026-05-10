class Solution:
    def addBinary(self, a: str, b: str):
        carry=0
        res=""
        i=len(a)-1
        j=len(b)-1

        while i>=0 or j>=0 or carry:
            sum=carry
            if i>=0:
                sum+=int(a[i])
                i-=1
            if j>=0:
                sum+=int(b[j])
                j-=1
            
            res=str(sum%2)+res
            carry=sum//2

        return res

           
print(Solution().addBinary("11","1"))


