from collections import Counter

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = lambda s : sorted(Counter(s).items())[0][1]
        
        for q in range(len(queries)) :
            queries[q] = f(queries[q])
        
        for w in range(len(words)) :
            words[w] = f(words[w])
        
        answer = [0] * len(queries)
        for i in range(len(queries)) :
            for j in range(len(words)) :
                if queries[i] < words[j] :
                    answer[i] += 1
        
        return answer