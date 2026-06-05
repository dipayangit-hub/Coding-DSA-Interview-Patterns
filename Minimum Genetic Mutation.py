from collections import deque,defaultdict
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if startGene==endGene:
            return 0
        adj=defaultdict(list)
        for i in range(len(bank)):
            if self.diff(bank[i],startGene):
                adj[bank[i]].append(startGene)
                adj[startGene].append(bank[i])
        
        for i in range(len(bank)):
            for j in range(i+1,len(bank)):
                if self.diff(bank[i],bank[j]):
                    adj[bank[i]].append(bank[j])
                    adj[bank[j]].append(bank[i])

        c=0
        q=deque()
        q.append(startGene)
        seen=set()
        seen.add(startGene)
        while len(q):
            size=len(q)
            for i in range(size):
                node=q.popleft()
                for neighbour in adj[node]:
                    if neighbour not in seen:
                        q.append(neighbour)
                        seen.add(neighbour)
            c+=1
            if endGene in seen:
                return c
        return -1

    def diff(self,start,end):
        if len(start)!=len(end):
            return 0
        c=0
        for i in range(len(start)):
            if start[i]!=end[i]:
              c+=1

        return c if c==1 else 0 

print(Solution().minMutation(startGene = "AAAACCCC", endGene = "CCCCCCCC", bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))
        