def prefix_sum(nums,k):
    sum=0
    map={}
    map[0]=1
    count=0
    for i in range(len(nums)):
        sum+=nums[i]

        if (sum-k) in map:
            count+=map[sum-k]
        map[sum]=map.get(sum,0)+1
    return count
        
    
print(prefix_sum([1, 2, 1, 2, 1],3))