from collections import deque
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n=len(board)
        seen=[False for _ in range(n*n+1)]
        seen[0]=True
        seen[1]=True
        level=0
        queue=deque()
        queue.append(1)
        maxel=n*n
        while len(queue):
            size=len(queue)
            for i in range(size):
                curr=queue.popleft()

                if curr==maxel:
                    return level
                
                for next in range(curr+1,min(curr+7,n*n+1)):
                    dest=next
                    r,c=self.calboardpositions(next,n)

                    if board[r][c]!=-1:
                        dest=board[r][c]

                    if not seen[dest]:
                        seen[dest]=True
                        queue.append(dest)
            level+=1
        return -1    
                    

            

    def calboardpositions(self,next,n):
        #counting is starting with 1 (adjusting offset with -1)
        r=(next-1)//n
        c=(next-1)%n
        #for odd rows you misty be writing in reveerse order(original matrix in reverse oredr)
        if r%2==1:
            c=n-c-1
        #as its starting from bottom
        r=n-r-1

        return r,c
    
print(Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))

    