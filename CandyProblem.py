
class Solution:


   def candyProblem(self,arr:list):
    sum,i=1,1
    n=len(arr)
    while i<n:
      if arr[i]==arr[i-1]:
        sum+=1
        i+=1
        continue
      peak=1

      while i<n and arr[i]>arr[i-1]:
        peak+=1
        sum+=peak
        i+=1

      down=1
      while i<n and arr[i]<arr[i-1]:
        sum+=down
        down+=1
        i+=1
      if down>peak:
        sum+=(down-peak)
    return sum


        
# print(Solution().candyProblem([0,2,4,3,2,1,1,3,5,6,4,0,0]))
print(Solution().candyProblem([0,2,4,7,6,5,4,3,2,1,1,1,2,3,4,2,1,1,1]))
