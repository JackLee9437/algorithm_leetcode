class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 10 ** 5
        
        for left in range(len(nums)-2) :
            if left and nums[left] == nums[left-1] :
                continue
                
            mid = left + 1
            right = len(nums) - 1
            while mid < right :
                val = nums[left] + nums[mid] + nums[right]
                if val > target :
                    right -= 1
                elif val < target :
                    mid += 1
                else :
                    return target
                if abs(val-target) < abs(answer-target) :
                    answer = val
        
        return answer