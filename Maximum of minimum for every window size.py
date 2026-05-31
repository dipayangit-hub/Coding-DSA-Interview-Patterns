from os import *
from sys import *
from collections import *
from math import *
from collections import deque

def maxMinWindow(n,arr):
    res=[float('-inf')]*n
    l=0
    for k in range(1,n+1):
        c,l=0,0
        temp=[]
        for r in range(len(arr)):
            temp.append(arr[r])
            c+=1
            if c==k:
                temp.sort()
                res[k-1]=max(res[k-1],temp[0])
                temp.remove(arr[l])
                l+=1
                c-=1
    return res

def maxwindow(k,arr):
    q=deque()
    res=[]
    for i in range(len(arr)):
        while len(q) and q.__getitem__(0)<=(i-k):
            q.popleft()
        
        if len(q):
            print(q.__getitem__(-1))
            print(arr[q.__getitem__(-1)])
        while len(q) and arr[q.__getitem__(-1)<=arr[i]]:
            q.pop()
        
        q.append(i)

        if i>=k-1:
            res.append(arr[q.__getitem__(0)])
    return res

# print(maxMinWindow(4,[1,2,3,4]))
print(maxwindow(2,[2,1,3,4]))
        


