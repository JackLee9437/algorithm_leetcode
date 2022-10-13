from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e5)
        
        graph = [[] for _ in range(n+1)]
        for u, v, w in times :
            graph[u].append((w, v))
        
        distance = [INF] * (n+1)
        distance[k] = 0
        heap = [(0, k)]
        while heap :
            dist, node = heappop(heap)
            if distance[node] < dist :
                continue
            for w, to in graph[node] :
                if dist + w < distance[to] :
                    distance[to] = dist + w
                    heappush(heap, (distance[to], to))
        answer = max(distance[1:])
        if answer == INF :
            return -1
        return answer
