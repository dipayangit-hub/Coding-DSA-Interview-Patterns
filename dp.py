def climbingStairs(n, dp=None):
    if dp is None:
        dp = [-1] * (n + 1)
    
    if n <= 1:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    
    l = climbingStairs(n - 1, dp)
    r = climbingStairs(n - 2, dp)
    dp[n] = l + r
    return dp[n]

#memoization
def frogjump(n,heights:list,dp=None):
    if dp is None:
        dp = [-1] * (n + 1)
    if n==0:
        return 0
    if dp[n] != -1:
        return dp[n]
    
    l=frogjump(n-1,heights,dp)+abs(heights[n]-heights[n-1])

    if n>1:
        r=frogjump(n-2,heights,dp)+abs(heights[n]-heights[n-2])
        dp[n]= min(l,r)
    else:
        dp[n]=l
    return dp[n]

#Tabulation
def frogjump1(n,heights:list):
    prev,curr,prev2=0,0,0
    for i in range(1,n):
        l=prev+abs(heights[i]-heights[i-1])
        if i>1:
            r=prev2+abs(heights[i]-heights[i-2])
            curr=min(l,r)
        else:
            curr=l
        prev2=prev
        prev=curr
    return prev


def frogkjumps(n, heights: list, k: int, dp=None):
    if dp is None:
        dp = [-1] * (n + 1)
    if n == 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    
    min_cost = float('inf')
    # Try all possible jumps from 1 to k
    for i in range(1, k + 1):
        if n >= i:
            cost = frogkjumps(n - i, heights, k, dp) + abs(heights[n] - heights[n - i])
            min_cost = min(min_cost, cost)
    
    dp[n] = min_cost
    return dp[n]

def main():
    # print(climbingStairs(3))
    print(frogkjumps(3,[10,20,30,10],2))

main()