from collections import Counter

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
        
        answer = [0] * len(queries)
        for i in range(len(queries)) :
            cur = f(queries[i])
            for j in range(len(words)) :
                if cur < words[j] :
                    answer[i] += 1
        
        return answer