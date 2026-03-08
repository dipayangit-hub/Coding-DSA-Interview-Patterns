
class Solution:
    def expressionevaluation(self,s:str):
        st=[]
        for i in s:
            if i.isdigit():
                st.insert(0,i)
            else:
                a=st.pop(0)
                b=st.pop(0)
                res=self.performop(int(a),int(b),i)
                st.insert(0,res)
        return st[0]
    def performop(self,a,b,op):
        if op=='*':
            return a*b
        elif op=='/':
            return a/b
        elif op=='+':
            return a+b
        else:
            return a-b


        
# print(Solution().candyProblem([0,2,4,3,2,1,1,3,5,6,4,0,0]))
print(Solution().expressionevaluation('1+8-6'))