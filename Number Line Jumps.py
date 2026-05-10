def kangaroo(x1, v1, x2, v2):
    if v1==v2:
        return "YES" if x1==x2 else "NO"
    t=(x2-x1)/(v1-v2)
    return "YES" if t>=0 and t==int(t) else "NO"

print(kangaroo(0,2,5,3))