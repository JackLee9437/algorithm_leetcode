import re

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        lowercases = '[a-z]*'
        new_pattern = lowercases + lowercases.join(pattern) + lowercases

        answer = []
        for query in queries :
            answer.append(True if re.fullmatch(new_pattern, query) else False)
        
        return answer