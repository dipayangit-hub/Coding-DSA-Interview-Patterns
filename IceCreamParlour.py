def icecreamParlor(m, arr):
    for i in range(len(arr)-1):
        if (m-arr[i]) in arr[i+1:]:
            for j,v in enumerate(arr):
                if j!=i and v==(m-arr[i]):
                    return [i+1,j+1]
    return []

print(icecreamParlor(4,[2,2,4,3])) 