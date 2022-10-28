from collections import deque

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        window = deque()
        
        for i in range(k-1) :
            if i >= len(s) :
                break
            window.append(s[i])
        
        binCodes = set()
        for i in range(k-1, len(s)) :
            window.append(s[i])
            binCodes.add(''.join(window))
            window.popleft()
        
        if len(binCodes) == 2 ** k :
            return True
        return False