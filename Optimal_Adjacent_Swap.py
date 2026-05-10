def max_sum_optimal_swap(nums):
    #Find total sum of array(sum+=arr_element*index)
#     maxsum=calc(nums)

#     for i in range(len(nums)-1):
#         nums[i+1],nums[i]=nums[i],nums[i+1]

#         maxsum=max(maxsum,calc(nums))

#         nums[i],nums[i+1]=nums[i+1],nums[i]
#     return maxsum

# def calc(nums):
#     sum=0
#     for i in range(len(nums)):
#         sum+=nums[i]*i
#     return sum

    #optimal approach, for chnage in adjacent indices -> a⋅i+b⋅(i+1) -> after swap-> b⋅i+a⋅(i+1), change in sum= a-b
    # curr_sum=sum(nums[i]*i for i in range(len(nums)))
    # maxsum=curr_sum
    # for i in range(len(nums)-1):
    #     a,b=nums[i],nums[i+1]
    #     delta=a-b
    #     maxsum=max(maxsum,curr_sum+delta)
    # return maxsum

    #dp
    dp=[(0,0) for _ in range(len(nums)+1)]
    for i in range(len(nums)):
        #not take or not swap
        no_swap_sum=dp[i][0]+i*nums[i]
        no_swap_count=dp[i][1]
        best_sum, best_count = no_swap_sum, no_swap_count
        #swap
        if i>0:
            swap_sum=dp[i-1][0]+(i-1)*nums[i]+i*nums[i-1]
            swap_count=dp[i-1][1]+1
            if swap_sum>no_swap_sum:
                best_sum=swap_sum
                best_count=swap_count
        dp[i+1]=(best_sum,best_count)
            
    return dp[-1][1]

print(max_sum_optimal_swap([1,9,7,3,2]))