def pivotIndex(nums: list) -> int:
    total=0
    for i in range(len(nums)):
        total+=nums[i]
    left=0
    for i in range(len(nums)):
        right=total-left-nums[i]
        if left==right:
            return i
        left+=nums[i]
    return -1


def subarraySum(nums: list, k: int) -> int:
    map={}
    sum,count=0,0
    map[0]=1
    for i in range(len(nums)):
        sum+=nums[i]
        if sum-k in map:
            count+=map[sum-k]
        map[sum]=map[sum]+1 if sum in map else 1
    return count

def checkSubarraySum(nums: list, k: int) -> bool:
    map={}
    sum=0
    map[0]=-1
    for i in range(len(nums)):
        sum+=nums[i]
        rem=sum%k
        if rem in map:
            if i-map[rem]>1:
                return True
        else:
            map[rem]=i
    return False

# pivotIndex([1,7,3,6,5,6])
# print(subarraySum([1,-1,0],0))
print(checkSubarraySum([23,2,6,4,7],6))