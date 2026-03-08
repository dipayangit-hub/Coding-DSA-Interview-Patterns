def stones(n, a, b):
    res=set()
    if a>b:
        a,b=b,a
    for i in range(n):
        res.add(i*a+(n-1-i)*b)
    return sorted(list(res))

print(stones(4,10,100))