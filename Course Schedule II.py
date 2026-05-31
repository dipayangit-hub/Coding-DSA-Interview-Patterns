from collections import deque,defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        map=defaultdict(list)
        indegree=[0]*numCourses

        q=deque()

        for prerequisite in prerequisites:
            map[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]]+=1

        
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)

        res=[]

        while len(q):
            node=q.popleft()
            res.append(node)
            for neighbour in map[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)

        return res if len(res)==numCourses else []
    

print(Solution().findOrder(3,[[1,0],[2,1]]))