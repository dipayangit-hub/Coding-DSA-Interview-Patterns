class Solution:
    def findClosestElements(self, arr, k, x):
        l,r=0,len(arr)-k

        while l<r:
            mid=l+(r-l)//2

            left_val=abs(x-arr[mid])
            right_val=abs(arr[mid+k]-x)

            if left_val>right_val:
                l=mid+1
            else:
                r=mid
        return arr[l:l+k]

        # n = len(arr)

        # # Bubble sort based on:
        # # 1. smaller distance from x
        # # 2. if tie -> smaller number first

        # for i in range(n):
        #     for j in range(0, n - i - 1):

        #         left = abs(arr[j] - x)
        #         right = abs(arr[j + 1] - x)

        #         # swap conditions
        #         if left > right:
        #             arr[j], arr[j + 1] = arr[j + 1], arr[j]

        #         # equal distance -> smaller number first
        #         elif left == right and arr[j] > arr[j + 1]:
        #             arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # # take first k
        # res = arr[:k]

        # # sort final answer in ascending order
        # for i in range(k):
        #     for j in range(0, k - i - 1):
        #         if res[j] > res[j + 1]:
        #             res[j], res[j + 1] = res[j + 1], res[j]

        # return res
    
print(Solution().findClosestElements([1,1,2,3,4,5],4,3))