from collections import deque
class Solution:
    def maxofmin(self,N):
        res=[]
        
        def getminwindow(N,k):
            q=deque()
            mins=[]
            #for 1st k size window
            for i in range(k):
                while len(q) and N[q[-1]]>=N[i]:
                    q.pop()
                q.append(i)
            mins.append(N[q[0]])
            
            l=1
            #for further elements
            for i in range(k,len(N)): 
                while len(q) and q[0]<l:
                    q.popleft()

                while len(q) and N[q[-1]]>=N[i]:
                    q.pop()
                q.append(i)
                mins.append(N[q[0]])
                l+=1
            return mins

        for i in range(1,len(N)+1):
            l=getminwindow(N,i)
            maxv=float('-inf')
            for j in range(len(l)):
                maxv=max(maxv,l[j])
            res.append(maxv)
        return res

print(Solution().maxofmin([1,2,3,4]))

