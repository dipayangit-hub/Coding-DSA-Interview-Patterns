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


def maxArea(height: list):
    i,j=0,len(height)-1
    area=0
    while i<j:
        area=max(area,(j-i)*(min(height[i],height[j])))
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return area


print(maxArea([1,8,6,2,5,4,8,3,7]))
