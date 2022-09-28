class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = int(1e9) + 7
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)) :
            dp[i][i] = 1

        def dnc(l, r) :
            nonlocal mod
            if dp[l][r] :
                return dp[l][r]
            if l > r :
                return 0
            
            result = 0
            for c in set(s[l:r+1]) :
                left, right = s.find(c, l, r+1), s.rfind(c, l, r+1)
                if left == right :
                    result += 1
                else :
                    result += 2 + dnc(left+1, right-1)
            dp[l][r] = result % mod
            return dp[l][r] 
        
        return dnc(0, len(s)-1)
        
        