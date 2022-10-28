from collections import deque

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        window = deque()
        
        for i in range(min(k-1, len(s))) :
            window.append(s[i])
        
        binCodes = set()
        target = 2 ** k
        for i in range(k-1, len(s)) :
            window.append(s[i])
            binCodes.add(''.join(window))
            if len(binCodes) == target :
                return True    
            window.popleft()
        
        return False