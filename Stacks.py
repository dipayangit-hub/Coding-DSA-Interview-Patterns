class Solution(object):
    def isValid(self, s):
        stack=[]
        opening=['(','{','[']
        closing=[')','}',']']
        for i in s:
            if i in opening:
                  stack.append(i)
            else:
                 j=closing.index(i)
                 if len(stack)==0 or stack[-1]!=opening[j]:
                      return False
                 stack.pop()
        return False if len(stack)>0 else True


    def nextGreaterElement(self, nums1, nums2):
         stack=[]
         map={}
         res=[]
         for i in nums2:
            while len(stack)>0 and stack[-1]<i:
                 map[stack.pop()]=i
            stack.append(i)
            map[i]=-1

         for i in nums1:
              res.append(map[i])
      
         return res           

    def simplifyPath(self, path):
         stack=[]
         words=path.split('/')
         for word in words:
              if word=="" or word=='.':
                   continue
              elif word=='..':
                   if len(stack)>0:
                    stack.pop()
              else:
                   stack.append(word)
         str="/"
         for i in stack:
              str+=i+"/"
              
         return str[:len(str)-1] if len(str)>1 else str   
                   

print(Solution().simplifyPath("/../"))