def alternate(s):
    chars=list(set(s))
    n=len(chars)
    max_len=0

    for i in range(n):
        for j in range(i+1,n):
            c1,c2=chars[i],chars[j]

            filtered=[c for c in s if c==c1 or c==c2]
        
            valid=True

            for k in range(1,len(filtered)):
                if filtered[k]==filtered[k-1]:
                    valid=False
                    break
            if valid:
                max_len=max(max_len,len(filtered))

    return max_len

print(alternate('beabeefeab'))