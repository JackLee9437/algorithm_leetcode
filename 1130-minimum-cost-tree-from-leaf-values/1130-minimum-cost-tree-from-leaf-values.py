class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) == 2 :
            return arr[0] * arr[1]
        
        answer = 0
        while len(arr) > 1 :
            target = arr.index(min(arr))
            if 0 < target < len(arr)-1 :
                answer += min(arr[target-1], arr[target+1]) * arr[target]
            else :
                answer += (arr[1] if target == 0 else arr[target-1]) * arr[target]
            arr.pop(target)
        
        return answer