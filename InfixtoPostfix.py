def infixtopostfix(str):
    st=[]
    ans=''
    for c in str:
        if (c>='A' and c<='Z') or (c>='a' and c<='z') or (c>='0' and c<='9'):
            ans+=c
        elif c == '(':
            st.append(c)
        elif c==')':
                while len(st)>0 and st[-1]!='(':
                     ans+=st.pop()
                st.pop()
        else:
             while len(st)>0 and priority(c)<=priority(st[-1]):
                    ans+=st.pop()
             st.append(c)

    while len(st)>0:
         ans+=st.pop()
    return ans

def priority(c):
     if c=='^':
          return 3
     elif c=='*' or c=='/':
          return 2
     elif c=='+' or c=='-':
          return 1
     else:
          return -1              



print(infixtopostfix('a+b*(c^d-e)'))