class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]

        def backtrack(open,close,s,res):
            if open==0 and close==0:
                res.append(s)
                return

          
            if open>0:
                backtrack(open-1,close,s+"(",res)
            if close>0 and close>open:
                backtrack(open,close-1,s+")",res)
        
        backtrack(n,n,"",res)
        return res
   
                

print(Solution().generateParenthesis(1))