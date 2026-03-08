def search(nums: list, target: int):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1



def searchMatrix(matrix: list, target: int):
    left=0
    m,n=len(matrix),len(matrix[0])
    right=m*n-1
    while left<=right:
        mid=(left+right)//2
        r=mid//n
        c=mid%n
        if matrix[r][c]==target:
            return True
        elif matrix[r][c]<target:
            left=mid+1
        else:
            right=mid-1
    return False



def search(nums: list, target: int):
    left= 0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[left]<=nums[mid]:
            #check if left side is sorted and update window
            if target>=nums[left] and target<=nums[mid]:
                right=mid-1
            else:
                left=mid+1
        elif nums[right]>=nums[mid]:
            #checking if right side is sorted and update window
            if target>=nums[mid] and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1

    return -1


def shipWithinDays(weights: list, days: int) -> int:
    left,right=0,0
    for i in weights:
        left=max(left,i)
        right+=i
    while left<right:
        mid=left+(right-left)//2 # To avoid overflow
        if canShip(weights,days,mid):
            #if this works properly, either this can be the minimum or something less than that, update window
            right=mid
        else:
            left=mid+1
    return left 

def canShip(weights,days,min):
    sum=0
    daycount=1
    for i in weights:
        if sum+i>min:
            daycount+=1
            sum=0
        sum+=i
    return daycount<=days



shipWithinDays([1,2,3,4,5,6,7,8,9,10],5)