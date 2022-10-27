from heapq import heappop, heappush

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        freeServers = []
        procServers = []
        
        for i in range(len(servers)) :
            heappush(freeServers, (servers[i], i, 0))
        
        ans = []
        
        for t in range(len(tasks)) :
            while procServers and procServers[0][0] <= t or not freeServers:
                ctime, weight, server = heappop(procServers)
                heappush(freeServers, (weight, server, ctime))
            
            weight, server, ctime = heappop(freeServers)
            ans.append(server)
            heappush(procServers, (max(t, ctime)+tasks[t], weight, server))
        
        return ans
                