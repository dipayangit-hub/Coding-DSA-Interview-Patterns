from collections import defaultdict, deque
def topoSort_dfs():
    st=[]
    adj = defaultdict(list) 
    adj[5].append(0)
    adj[5].append(2)
    adj[2].append(3)
    adj[3].append(1)
    adj[4].append(0)
    adj[4].append(1)

    V=6
    visited=[False for _ in range(V)]

    for i in range(V):
        if not visited[i]:
            dfs(i,visited,st,adj)

    res=[]
    while len(st)>0:
        res.append(st.pop())
    return res
    
def dfs(node, visited, st, adj):
        visited[node]=True
        neighbours=adj[node]
        for j in neighbours:
            if not visited[j]:
                dfs(j,visited,st,adj)
        st.append(node)


#Kahn's Algorithm
def top_sort_bfs():
    adj = defaultdict(list) 
    adj[5].append(0)
    adj[5].append(2)
    adj[2].append(3)
    adj[3].append(1)
    adj[4].append(0)
    adj[4].append(1)


    V=6
    queue=deque()

    #step 1: Count indegrees of all nodes
    indegree=[0 for _ in range(V)]
    for i in range(V):
         for j in adj[i]:
              indegree[j]+=1
    
    #Step 2: Push all the indegree=0 nodes in the queue
    for i in range(V):
         if indegree[i]==0:
              queue.append(i)

    res=[]
    
    #process queue
    while len(queue)>0:
         node=queue.popleft()
         res.append(node)
         for i in adj[node]:
              indegree[i]-=1
              if indegree[i]==0:
                   queue.append(i)

    #check for cycle or valid oredr is followed or not
    if len(res)!=V:
         print("Cycle is detected")

    return res


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        queue=deque()
        adj = defaultdict(list)
        indegree=[0 for _ in range(numCourses)]
        for nodes in prerequisites:
             adj[nodes[1]].append(nodes[0])
             indegree[nodes[0]]+=1
        
        for i in range(len(indegree)):
             if indegree[i]==0:
                  queue.append(i)
        res=[]
        while len(queue)>0:
             node=queue.popleft()
             res.append(node)
             for v in adj[node]:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)
        return res


    def canFinish(self, numCourses, prerequisites):
        queue=deque()
        adj = defaultdict(list)
        indegree=[0 for _ in range(numCourses)]
        for nodes in prerequisites:
             adj[nodes[1]].append(nodes[0])
             indegree[nodes[0]]+=1
        
        for i in range(len(indegree)):
             if indegree[i]==0:
                  queue.append(i)
        processed=0
        while len(queue)>0:
             node=queue.popleft()
             processed+=1
             for v in adj[node]:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)


        return False if processed!=numCourses else True
                         
                  
                       
             


print(Solution().canFinish(4,[[1,0],[2,0],[3,1],[3,2]]))

                    

