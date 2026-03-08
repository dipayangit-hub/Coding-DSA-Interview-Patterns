def maximumSubarraySum(nums: list, k: int) -> int:
    left,sum=0,0
    maxsum=0
    visited=set()
    for right in range(len(nums)):
        while visited.__contains__(nums[right]) or len(visited)==k:
            visited.remove(nums[left])
            sum-=nums[left]
            left+=1
        sum+=nums[right]
        visited.add(nums[right])
        if len(visited)==k:
            maxsum=max(maxsum,sum)
    return maxsum


def lengthOfLongestSubstring( s: str) -> int:
    left=0
    maxLen=0
    visited=set()
    for right in range(len(s)):
        while visited.__contains__(s[right]):
            visited.remove(s[left])
            left+=1
        visited.add(s[right])
        maxLen=max(maxLen,right-left+1)

    return maxLen

def minSubArrayLen(target: int, nums:list) -> int:
    left=0
    sum=0
    minsize=float('inf')
    for right in range(len(nums)):
        sum+=nums[right]
        while sum>=target:
            minsize=min(minsize,right-left+1)
            sum-=nums[left]
            left+=1

    return 0 if minsize==float('inf') else minsize

print(minSubArrayLen(11,[1,1,1,1,1,1,1,1]))