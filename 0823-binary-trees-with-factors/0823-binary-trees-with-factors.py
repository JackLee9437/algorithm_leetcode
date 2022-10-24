from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        
        dp = defaultdict(int)
        for n in arr :
            dp[n] += 1
        
        arr.sort()
        for i in range(1, len(arr)) :
            for j in range(i) :
                if (not arr[i] % arr[j]) and (tmp:= arr[i] // arr[j]) in dp :
                    dp[arr[i]] += dp[arr[j]] * dp[tmp]
        
        return sum(dp.values()) % MOD