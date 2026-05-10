import heapq
def subarray_sum(nums,k):
    map={}
    map[0]=1
    count=0
    prefix_sum=0
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        val=prefix_sum-k
        if val in map:
            count+=map[val]
        map[prefix_sum]=map.get(prefix_sum,0)+1
    return count


def longest_substring(s):
    l,r=0,0
    maxsubs=0
    seen=set()
    while r<len(s):
        while l<=r and s[r] in seen:
            seen.remove(s[l])
            l+=1


        maxsubs=max(maxsubs,r-l+1)
        r+=1

    return maxsubs

def kth_largest_el(nums,k):
    pq=[]
    for num in nums:
        heapq.heappush(pq,num)
        if len(pq)>k:
            heapq.heappop(pq)
    return pq[0]

def threesum(nums):
    nums.sort()
    i,res=0,[]
    while i<len(nums)-2:
        while i>0 and i<len(nums)-2 and nums[i-1]==nums[i]:
            i+=1
        l,r=i+1,len(nums)-1
        while l<r:
            sum=nums[i]+nums[l]+nums[r]
            if sum==0:
                res.append([nums[i],nums[l],nums[r]])

                while l<r and nums[l+1]==nums[l]:
                    l+=1

                while l<r and nums[r-1]==nums[r]:
                    r-=1
                l+=1
                r-=1
            elif sum<0:
                l+=1
            else:
                r-=1
        i+=1
    return res


def merge_intervals(intervals):
    intervals.sort(key=lambda x:x[0])
    res=[]
    res.append(intervals[0])
    for i in range(1,len(intervals)):
        if intervals[i][0]<=res[-1][1]:
            res[-1][1]=max(res[-1][1],intervals[i][1])
        else:
            res.append(intervals[i])
    return res

def prefix_mul(nums):
    n=len(nums)
    res=[1]*n

    prefix=1
    for i in range(n):
        res[i]=prefix
        prefix*=nums[i]
    suffix=1
    for i in range(n-1,-1,-1):
        res[i]*=suffix
        suffix*=nums[i]
    return res
        
def maximum_sum(nums):
    sum,maxsum=nums[0],nums[0]

    for i in range(1,len(nums)):
        sum=max(sum+nums[i],nums[i])
        maxsum=max(maxsum,sum)
    return maxsum

def stocks(nums):
    minp,maxprofit=float('inf'),0
    for price in nums:
        minp=min(minp,price)
        maxprofit=max(maxprofit,price-minp)
    return maxprofit

def brackets(s):
    st=[]
    map={
        '(':')',
        '{':'}',
        '[':']'
    }
    for ch in s:
        if ch in map.keys():
            st.append(ch)
        else:
            if not st:
                return False
            c=st.pop()
            if map[c]!=ch:
                return False
    return len(st)==0

def greedy(nums):
    maxjump=0
    for i in range(len(nums)):
        if i>maxjump:
            return False
        maxjump=max(maxjump,nums[i]+i)
    return True

def subsets(nums):
    res=[]
    def recurse(nums,i,lists):
        if i>=len(nums):
            res.append(lists[:])
            return
        lists.append(nums[i])
        recurse(nums,i+1,lists)
        lists.pop()
        recurse(nums,i+1,lists)
    recurse(nums,0,[])
    return res


# print(subarray_sum([1,2,3,-3,1,1,1],3))   
# print(longest_substring("bbbb"))
# print(kth_largest_el([3,2,1,4,3,5,5,6],4))
# print(threesum([-1,0,1,2,-1,-4]))
# print(merge_intervals([[1,3],[8,10],[2,6],[15,18]]))
# print(prefix_mul([1,2,3,4]))
# print(maximum_sum([-2,1,-3,4,-1,2,1,-5,4]))
# print(stocks([7,1,5,3,6,4]))
# print(brackets('{[]}'))
# print(greedy([2,3,1,1,4]))
print(subsets([1,2,3]))

