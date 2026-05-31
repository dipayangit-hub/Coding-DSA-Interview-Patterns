from collections import defaultdict
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        map=defaultdict(list)
        for i in range(len(equations)):
            num=equations[i][0]
            den=equations[i][1]

            map[num].append([den,values[i]])
            map[den].append([num,1/values[i]])

        res=[]
        for i in range(len(queries)):
            if queries[i][0] not in map or queries[i][1] not in map:
                res.append(-1.0)
                continue
            visited=set()
            ans=-1.0
            def dfs(src,dest,map,temp):
                nonlocal ans
                if src in visited:
                    return ans
                elif src==dest:
                    ans=temp
                    return ans
                visited.add(src)
                for node in map[src]:
                    ans=dfs(node[0],dest,map,temp*node[1])
                    if ans!=-1:
                        return ans
                return ans
            ans=dfs(queries[i][0],queries[i][1],map,1.0)
            res.append(ans)

        return res

print(Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))