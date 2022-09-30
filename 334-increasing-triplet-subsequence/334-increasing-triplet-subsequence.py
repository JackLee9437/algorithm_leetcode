class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        accMin = nums[:]
        accMax = nums[:]
        
        for i in range(1, len(accMin)) :
            accMin[i] = min(accMin[i], accMin[i-1])
        for i in range(len(accMax)-2, -1, -1) :
            accMax[i] = max(accMax[i], accMax[i+1])
            
        for i in range(1, len(nums)-1) :
            if accMin[i] < nums[i] < accMax[i] :
                return True
        return False