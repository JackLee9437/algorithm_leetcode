class Solution:
    def minInsertions(self, s: str) -> int:
        opencnt = 0
        
        answer = 0
        i = 0
        while i < len(s) :
            if s[i] == "(" :
                opencnt += 1
            else :
                if opencnt :
                    opencnt -= 1
                else :
                    answer += 1
                if i == len(s)-1 or s[i+1] != ')':
                    answer += 1
                else :
                    i += 1  
            i += 1
        
        if opencnt :
            answer += opencnt * 2
        
        return answer