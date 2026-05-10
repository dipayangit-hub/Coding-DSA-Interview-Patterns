class Solution(object):
    def evalRPN(self, tokens):
        st=[]
        operators=['+','-','*','/']
        for ch in tokens:
            if ch in operators:
                val=st.pop()
                val1=st.pop()
                if ch=='+':
                    res=val1+val
                elif ch=='-':
                    res=val1-val
                elif ch=='*':
                    res=val1*val
                else:
                    res=abs(val1) // abs(val)
                    if (val1 < 0 and val > 0) or (val1 > 0 and val < 0):
                        res = -res
                st.append(res)
            else:
                st.append(int(ch))
        return st.pop()
    
print(Solution().evalRPN(["4","-2","/","2","-3","-","-"]))