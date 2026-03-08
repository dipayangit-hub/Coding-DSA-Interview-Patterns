def postfixtoinfix(s:str):
   st=[]
   for c in s:
      if (c>='A' and c<='Z') or (c>='a' and c<='z') or (c>='0' and c<='9'):
         st.append(c)
      else:
         if len(st)>=2:
            a=st.pop()
            b=st.pop()
            ans='('+b+c+a+')'
            st.append(ans)
   return st.pop()





print(postfixtoinfix('AB-DE+F*/'))