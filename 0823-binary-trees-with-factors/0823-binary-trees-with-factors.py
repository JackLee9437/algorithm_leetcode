from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        answer = len(arr)
        
        dp = defaultdict(int)
        for n in arr :
            dp[n] += 1
        
        candidates = []
        for i in range(len(arr)) :
            for j in range(len(arr)) :
                if (mult := arr[i] * arr[j]) in dp :
                    candidates.append((arr[i], arr[j], mult))
        candidates.sort(key=lambda x : x[2])
        for a, b, val in candidates :
            multi = dp[a] * dp[b]
            answer += multi
            dp[val] += multi
        
        return answer % MOD