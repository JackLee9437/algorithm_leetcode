class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = {
            "+" : (lambda a, b : a+b),
            "-" : (lambda a, b : a-b),
            "*" : (lambda a, b : a*b),
            "/" : (lambda a, b : ((a//abs(a) if a != 0 else 1)*(b//abs(b)))*(abs(a)//abs(b)))
        }
        
        stk = []
        for token in tokens :
            try :
                stk.append(int(token))
            except :
                b = stk.pop()
                a = stk.pop()
                stk.append(calc[token](a, b))
        
        return stk.pop()