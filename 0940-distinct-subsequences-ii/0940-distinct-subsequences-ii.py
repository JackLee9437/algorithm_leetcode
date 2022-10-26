class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        
        last = {}
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        
        for i in range(len(s)) :
            dp[i+1] = dp[i] * 2
            if s[i] in last :
                dp[i+1] -= dp[last[s[i]]]
            last[s[i]] = i
        
        return (dp[len(s)] - 1) % MOD