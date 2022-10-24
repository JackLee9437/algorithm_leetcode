class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        getSlope = lambda a, b : (b[1]-a[1]) / (b[0]-a[0]) if b[0]-a[0] != 0 else int(1e9)
        
        slopes = set()
        for i in range(1, len(coordinates)) :
            slopes.add(getSlope(coordinates[0], coordinates[i]))
        
        return len(slopes) == 1