class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        if len(set(nums)) == 1 :
            return 0
        
        arr = sorted(zip(nums, cost))
        cnt = 0
        total = sum(cost)
        half = total // 2
        target = 0
        for num, c in arr :
            cnt += c
            if cnt > half :
                target = num
                break
        
        return sum(c*abs(target-num) for num, c in arr)