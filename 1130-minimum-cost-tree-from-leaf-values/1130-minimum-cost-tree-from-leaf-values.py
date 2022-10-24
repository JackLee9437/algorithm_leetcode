class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) == 2 :
            return arr[0] * arr[1]
        
        dp = [[0 for _ in range(len(arr))] for __ in range(len(arr))]
        for i in range(len(arr)-1) :
            dp[i][i+1] = arr[i] * arr[i+1]
        
        for size in range(3, len(arr)+1) :
            for i in range(len(arr)-size+1) :
                for j in range(i+size-1, len(arr)) :
                    dp[i][j] = int(1e9)
                    for k in range(i, j) :
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + max(arr[i:k+1]) * max(arr[k+1:j+1]))
                        
        return dp[0][len(arr)-1]