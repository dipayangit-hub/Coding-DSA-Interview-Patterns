class Solution:
    def myPow(self, x: float, n: int) -> float:
        #for negative n, make x=1/x and n=-n
        if n<0:
           x=1/x
           n=abs(n)
        ans=1
        #take binary form of n to reduce time complexity of iteration to log n
        while n>0:
            #if 1 only then multiply it to answer else overall result will be 0 , but increment x=x*x as power moves in the format 1,2,4,..
            if n%2==1:
                ans*=x
            x*=x
            n//=2
        return ans
       
print(Solution().myPow(2.0000, -2))