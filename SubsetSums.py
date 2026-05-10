class Solution:
    def subsetSums(self, arr):
            res=[]
            self.sum_recurse(arr,0,0,res)
            return res
    def sum_recurse(self,arr,i,sum,res):
          if i>=len(arr):
                res.append(sum)
                return res
          self.sum_recurse(arr,i+1,sum+arr[i],res) #take
          self.sum_recurse(arr,i+1,sum,res) #not take



print(Solution().subsetSums([2,3]))

        

