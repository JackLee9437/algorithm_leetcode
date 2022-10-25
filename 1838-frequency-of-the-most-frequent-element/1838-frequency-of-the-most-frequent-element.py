class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        preSum = nums[:]
        for i in range(1, len(preSum)) :
            preSum[i] += preSum[i-1]
        
        answer = 1
        for j in range(1, len(nums)) :
            left, right = 0, j
            i = j
            while left <= right :
                mid = (left+right) // 2
                if nums[j] * (j-mid+1) <= preSum[j] - (preSum[mid-1] if mid > 0 else 0) + k :
                    i = mid
                    right = mid - 1
                else :
                    left = mid + 1
            answer = max(answer, j-i+1)
        
        return answer
        
        
        
        
        
        
    def maxFrequency_slidingWindow(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l = r = 0
        curSum = 0
        answer = 0
        while r < len(nums) :
            curSum += nums[r]
            
            while nums[r] * (r-l+1) > curSum + k :
                curSum -= nums[l]
                l += 1
            
            answer = max(answer, r-l+1)
            r += 1
        
        return answer