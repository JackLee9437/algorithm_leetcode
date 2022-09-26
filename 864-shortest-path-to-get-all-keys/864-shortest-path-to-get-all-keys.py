from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        lenKey = 0
        startingPoint = None
        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if grid[r][c].isalpha() and ord("a") <= ord(grid[r][c]) :
                    lenKey += 1
                elif grid[r][c] == "@" :
                    startingPoint = (r, c)
        target = (1 << lenKey) - 1
        
        visited = set()
        dirx = [[1,0],[0,1],[-1,0],[0,-1]]
        que = deque([(*startingPoint, 0, 0)])
        while que :
            r, c, keys, dist = que.popleft()
            if keys == target :
                return dist
            if (r, c, keys) in visited :
                continue
            visited.add((r, c, keys))
            
            for dr, dc in dirx :
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) :
                    if grid[nr][nc].isalpha() :
                        if ord("Z") >= ord(grid[nr][nc]) :
                            if keys & (1 << (ord(grid[nr][nc]) - ord("A"))) :
                                que.append((nr, nc, keys, dist+1))
                        else :
                            newKeys = keys | (1 << (ord(grid[nr][nc]) - ord("a")))
                            que.append((nr, nc, newKeys, dist+1))
                    elif grid[nr][nc] in ".@" :
                        que.append((nr, nc, keys, dist+1))

        return -1