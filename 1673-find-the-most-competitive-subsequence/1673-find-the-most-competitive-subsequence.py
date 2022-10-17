class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        rst = [nums[0]]
        i = 1
        while i < len(nums) - k + len(rst) :
            while rst and rst[-1] > nums[i] and len(nums)-i-1 >= k-len(rst) :
                rst.pop()
            if len(rst) < k :
                rst.append(nums[i])
            i += 1
        print(rst)
        if len(rst) < k :
            rst += nums[len(rst)-k:]
        
        return rst