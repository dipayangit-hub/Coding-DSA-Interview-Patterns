import heapq
from collections import defaultdict

def dijkstra_algo():
    v=5
    adj = defaultdict(list)   
    #{node:[adjacent_node,weight]}
    adj[0].append([1,2])
    adj[1].append([0,2])

    adj[0].append([2,4])
    adj[2].append([0,4])

    adj[1].append([2,1])
    adj[2].append([1,1])

    adj[2].append([3,7])
    adj[3].append([2,7])

    adj[2].append([4,3])
    adj[4].append([2,3])

    adj[3].append([4,1])
    adj[4].append([3,1])

    return dijkstra(v,adj,0)


def dijkstra(v:int,adj:defaultdict,src:int):
    dist=[float('inf') for _ in range(v)]
    dist[src]=0
    pq=[]
    heapq.heappush(pq,[0,src]) #access min distance node first-> compare by weight

    while len(pq)>0:
        currwt,currnode=heapq.heappop(pq)
        # skip outdated heap entries and replaces the need for visited nodes list
        if currwt > dist[currnode]:
            continue
        for node, wt in adj[currnode]:
            distance=currwt+wt
            if distance<dist[node]:
                dist[node]=distance
                heapq.heappush(pq,[distance,node])
    return dist

print(dijkstra_algo())