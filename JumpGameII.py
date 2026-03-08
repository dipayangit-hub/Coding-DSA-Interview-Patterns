import sys

def jumpGameII(arr:list):
    def recursion(ind,jumps,arr):
        if ind>=len(arr)-1:
            return jumps
        mini=sys.maxsize
        for i in range(1,len(arr)):
            mini=min(mini,recursion(i+ind,jumps+1,arr))

        return mini
    return recursion(0,0,arr)





print(jumpGameII([2,3,1,1,4]))