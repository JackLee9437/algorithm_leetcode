class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        heights = [0] * (m+1)
        
        answer = 0
        for row in matrix :
            for i in range(m) :
                heights[i] = heights[i]+1 if row[i] == '1' else 0
            stk = [-1]
            for col in range(m+1) :
                while heights[col] < heights[stk[-1]] :
                    h = heights[stk.pop()]
                    w = col-1-stk[-1]
                    answer = max(answer, h*w)
                stk.append(col)
        
        return answer