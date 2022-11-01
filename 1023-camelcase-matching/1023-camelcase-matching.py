class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        answer = []
        
        for query in queries :
            i = 0
            for alpha in query :
                if i < len(pattern) and alpha == pattern[i] :
                    i += 1
                elif ord(alpha) < ord('a') :
                    answer.append(False)
                    break
            else :
                if i < len(pattern) :
                    answer.append(False)
                else :
                    answer.append(True)
        
        return answer