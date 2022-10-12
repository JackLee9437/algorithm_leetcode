class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        res = 0
        cur = []
        
        for start, end in intervals :
            if not cur or cur[1] < start :
                res += 2
                cur = [end-1, end]
            elif cur[0] < start :
                res += 1
                if cur[1] == end :
                    cur = [end-1, end]
                else :
                    cur = [cur[1], end]
        
        return res