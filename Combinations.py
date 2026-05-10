class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
      res=[]
      def backtrack(start,l):
         if len(l)==k:
            res.append(l[:])
            return
         for i in range(start,n+1):
            l.append(i)
            backtrack(i+1,l)
            l.pop()
      
      backtrack(1,[])
      return res
    
print(Solution().combine(4,2))

         