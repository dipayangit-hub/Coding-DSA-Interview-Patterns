
#Memoization
def fibonacci(n:int,dp:list=None):
    if dp is None:
        dp=[-1]*(n+1)

    if dp[n]!=-1:
        return dp[n]
    
    if n<=1:
        return n
    dp[n]=fibonacci(n-1,dp)+fibonacci(n-2,dp)
    return dp[n]

#Tabulation
def fibonacci_1(n:int):
    prev2,prev=0,1
    for i in range(2, n+1):
        curr=prev+prev2
        prev2=prev
        prev=curr
    return prev
    

def frog_jump(n,heights:list,k):
    dp=[0]*n
    for i in range(1,n):
        minJump=float('inf')
        for j in range(1,k):
            if i-j>=0:
                jump=dp[i-j]+abs(heights[i]-heights[i-j])
                minJump=min(minJump,jump)
        dp[i]=minJump
    return dp[-1]

def main():
    # print(fibonacci_1(4))
    print(frog_jump(6,[30,10,60,10,60,50],2))


main()