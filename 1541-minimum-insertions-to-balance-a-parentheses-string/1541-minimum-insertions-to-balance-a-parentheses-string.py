class Solution:
    def minInsertions(self, s: str) -> int:
        stk = []
        
        answer = 0
        i = 0
        while i < len(s) :
            if s[i] == "(" :
                stk.append(1)
            else :
                if stk :
                    stk.pop()
                else :
                    answer += 1
                if i == len(s)-1 or s[i+1] != ')':
                    answer += 1
                else :
                    i += 1  
            i += 1
        
        if stk :
            answer += len(stk) * 2
        
        return answer