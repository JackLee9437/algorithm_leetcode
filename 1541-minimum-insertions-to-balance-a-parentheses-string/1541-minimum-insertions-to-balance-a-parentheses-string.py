class Solution:
    def minInsertions(self, s: str) -> int:
        opencnt = 0
        s = s.replace('))', ']')
        
        answer = 0
        for c in s :
            if c == "(" :
                opencnt += 1
            else :
                if c == ')':
                    answer += 1
                
                if opencnt :
                    opencnt -= 1
                else :
                    answer += 1
                
        if opencnt :
            answer += opencnt * 2
        
        return answer