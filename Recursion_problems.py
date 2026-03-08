#parameterized
def sumoffirstNnos(i,sum):
        if i<1:
              print(sum)
              return
        sumoffirstNnos(i-1,sum+i)
    
#functional
def factorial(i):
    if i<1:
          return 1
    return i*factorial(i-1)

def reverse_array(arr:list):
      def swap(l):
            r=len(arr)-l-1
            t=arr[l]
            arr[l]=arr[r]
            arr[r]=t
      def recurse(l):
            if l>=len(arr)//2:
                  return
            swap(l)
            recurse(l+1)
      recurse(0)
      return arr

def palindrome(s:str):       
    def recurse(l):
        if l>=len(s)//2:
              return True
        if s[l]!=s[len(s)-l-1]:
              return False
        return recurse(l+1)

    return recurse(0)

def fibonacci(n:int):
      if n<=1:
            return n
      return fibonacci(n-1)+fibonacci(n-2)

def printallsubsequences(arr:list):  
      def fetchsubsequences(i,res):
            if i>=len(arr):
                  print(res)
                  return 
            res.append(arr[i])
            fetchsubsequences(i+1,res)
            res.remove(arr[i])
            fetchsubsequences(i+1,res)
      fetchsubsequences(0,[])

def printallsubsequencewithsumasK(arr:list,k:int):
         def fetchsubsequences(i,sum,res):
            if sum==k:
                  print(res)
                  return
            elif i>=len(arr) or sum>k:
                  return 
            res.append(arr[i])
            fetchsubsequences(i+1,sum+arr[i],res)
            res.remove(arr[i])
            fetchsubsequences(i+1,sum,res)
         fetchsubsequences(0,0,[])   

def print1subsequencewithsumasK(arr:list,k:int):
         def fetchsubsequences(i,sum,res):
            if sum==k:
                  print(res)
                  return True
            elif i>=len(arr) or sum>k:
                  return False
            
            res.append(arr[i])
            if fetchsubsequences(i+1,sum+arr[i],res)==True:
                  return True
            res.remove(arr[i])
            if fetchsubsequences(i+1,sum,res)==True:
                  return True
            return False
         return fetchsubsequences(0,0,[])

def countsubsequences(arr:list,k:int):
      def count(i,sum,res):
             if sum==k:
                  return 1
             elif i>=len(arr) or sum>k:
                  return 0
             
             res.append(arr[i])
             l=count(i+1,sum+arr[i],res)
             res.remove(arr[i])
             r=count(i+1,sum,res) 
             return l+r
      return count(0,0,[])



def main():
    # sumoffirstNnos(3,0)
    # print(factorial(4))
    # print(reverse_array([1,2,3,4,5]))
    # print(palindrome('MADAM'))
    # print(fibonacci(4))
    # print(printallsubsequences([3,1,2]))
      print(countsubsequences([3,1,2],3))


main()