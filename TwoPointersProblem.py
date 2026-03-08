def twosum(arr:list,target:int):
    l,r=0,len(arr)-1
    while l<r:
        if arr[l]+arr[r]==target:
            return [l+1,r+1]
        elif arr[l]+arr[r]<target:
            l+=1
        else:
            r-=1     
    return []   


def removeDuplicates(nums:list):
   j=1
   for i in range(1,len(nums)):
       if nums[i]!=nums[j-1]:
           nums[j]=nums[i]
           j+=1
   return j

print(removeDuplicates([0,1,1,2,2,2,3,3,3,3,4]))