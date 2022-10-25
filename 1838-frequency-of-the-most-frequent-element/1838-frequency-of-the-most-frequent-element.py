class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
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