def superReducedString(s):
    st=[]

    for ch in s:
        if len(st)==0:
            st.append(ch)
        else:
            if st[-1]==ch:
                st.pop()
            else:
                st.append(ch)
    return "".join(st) if len(st)>0 else "Empty String"
        
  


print(superReducedString('abbaccdd'))