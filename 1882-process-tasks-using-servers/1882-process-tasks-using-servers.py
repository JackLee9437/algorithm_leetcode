from heapq import heappop, heappush
from collections import deque

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        freeServers = []
        procServers = []
        
        for i in range(len(servers)) :
            heappush(freeServers, (servers[i], i))
        
        ans = []
        
        que = deque()
        for t in range(len(tasks)) :
            que.append(tasks[t])
            while procServers and procServers[0][0] <= t :
                server = heappop(procServers)[1]
                heappush(freeServers, (servers[server], server))
            
            while que and freeServers :
                server = heappop(freeServers)[1]
                task = que.popleft()
                ans.append(server)
                heappush(procServers, (t+task, server))
        
        while que :
            while procServers and procServers[0][0] <= t :
                server = heappop(procServers)[1]
                heappush(freeServers, (servers[server], server))
            
            while que and freeServers :
                server = heappop(freeServers)[1]
                task = que.popleft()
                ans.append(server)
                heappush(procServers, (t+task, server))
            t = procServers[0][0]
        
        return ans
                