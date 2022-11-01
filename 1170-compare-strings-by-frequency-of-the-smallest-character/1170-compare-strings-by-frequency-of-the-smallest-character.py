class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s) :
            sc = 'z'
            count = 0
            for c in s :
                if c < sc :
                    sc = c
                    count = 1
                elif c == sc :
                    count += 1
            return count
        
        for w in range(len(words)) :
            words[w] = f(words[w])
        words.sort(reverse=True)
        
        answer = [0] * len(queries)
        for i in range(len(queries)) :
            cur = f(queries[i])
            count = 0
            
            left, right = 0, len(words)-1
            while left <= right :
                mid = (left + right) // 2
                if words[mid] > cur :
                    count = mid + 1
                    left = mid + 1
                else :
                    right = mid - 1
            
            answer[i] = count
        
        return answer