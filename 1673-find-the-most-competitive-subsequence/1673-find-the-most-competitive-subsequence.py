class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        rst = []
        poplimit = len(nums)-k
        for i in range(len(nums)) :
            while poplimit > 0 and rst and rst[-1] > nums[i] :
                rst.pop()
                poplimit -= 1
            rst.append(nums[i])
            i += 1
        
        return rst[:k]