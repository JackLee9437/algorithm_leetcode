from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        perfectSquares = []
        i = 1
        while (tmp := i ** 2) <= n :
            perfectSquares.append(tmp)
            i += 1
        
        dp = [0] * (n+1)
        que = deque([(0, 0)])
        while que :
            num, cnt = que.popleft()

            if num == n :
                return cnt
            
            for i in range(len(perfectSquares)-1, -1, -1) :
                tmp = num+perfectSquares[i]
                if tmp <= n and not dp[tmp] :
                    dp[tmp] = cnt+1
                    que.append((tmp, cnt+1))