class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        answer = []
        
        for query in queries :
            i = j = 0
            while j < len(query) :
                alpha = query[j]
                if i < len(pattern) and alpha == pattern[i] :
                    i += 1
                elif ord(alpha) < ord('a') :
                    break
                j += 1
            if i < len(pattern) or j < len(query):
                answer.append(False)
            else :
                answer.append(True)
        
        return answer