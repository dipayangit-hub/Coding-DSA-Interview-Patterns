def prefixtopostfix(s:str):
    st=[]
    for c in s[::-1]:
        if (c>='A' and c<='Z') or (c>='a' and c<='z') or (c>='0' and c<='9'):
         st.append(c)
        else:
         if len(st)>=2:
            a=st.pop()
            b=st.pop()
            ans=a+b+c
            st.append(ans)
    return st.pop()







print(prefixtopostfix('/-AB*+DEF'))