def infixtoprefix(s:str):
    s=reverse_replace(s)
    st=[]
    ans=''
    for c in s:
        if (c>='A' and c<='Z') or (c>='a' and c<='z') or (c>='0' and c<='9'):
            ans+=c
        elif c == '(':
            st.append(c)
        elif c==')':
                while len(st)>0 and st[-1]!='(':
                     ans+=st.pop()
                st.pop()
        else:
             if c=='^':
                  while len(st)>0 and priority(c)<=priority(st[-1]):
                       ans+=st.pop()
             else:
                  while len(st)>0 and priority(c)<priority(st[-1]):
                       ans+=st.pop()
             st.append(c)

    while len(st)>0:
         ans+=st.pop()
    return ans[::-1]


def priority(c):
     if c=='^':
          return 3
     elif c=='*' or c=='/':
          return 2
     elif c=='+' or c=='-':
          return 1
     else:
          return -1     

def reverse_replace(s:str):
    rev_s=s[::-1]
    rev_s = ''.join(')' if ch == '(' else '(' if ch == ')' else ch for ch in rev_s)
    return rev_s




print(infixtoprefix('(A+B)*C-D+F'))