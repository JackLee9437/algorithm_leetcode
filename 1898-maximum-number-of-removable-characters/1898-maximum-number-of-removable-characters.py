class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        if not len(removable) :
            return 0
        
        def check(k) :
            removed = set(removable[:k])
            i = j = 0
            while i < len(s) and j < len(p) :
                if i in removed :
                    i += 1
                    continue
                if s[i] == p[j] :
                    j += 1
                i += 1
            return j == len(p)
        
        answer = 0
        left, right = 0, len(removable)
        while left <= right :
            mid = (left+right) // 2
            # if len(s) - mid < len(p) :
            #     right = mid - 1
            #     continue
            if check(mid) :
                answer = mid
                left = mid + 1
            else :
                right = mid - 1
        
        return answer