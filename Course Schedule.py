from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        map=defaultdict(list)
        indegree=[0]*numCourses

        q=deque()

        for prerequisite in prerequisites:
            map[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]]+=1
        
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        
        processed=0

        while len(q):
            node=q.popleft()
            processed+=1
            for neighbour in map[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        
        return processed==numCourses
    

print(Solution().canFinish(3,[[1,0],[1,2],[2,1]]))

        
        
