class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = float(min(x for x, c in enumerate(count) if c > 0))
        maximum = float(max(x for x, c in enumerate(count) if c > 0))
        total = sum(count)
        mean = sum(x * c for x, c in enumerate(count)) / total
        mode = float(max(enumerate(count), key=lambda x : x[1])[0])
        
        target = total // 2 + (1 if total & 1 else 0)
        fcount = 1 if total & 1 else 2
        found = 0
        median = 0
        for val, c in enumerate(count) :
            if found + c < target :
                found += c
            else :
                median += val
                fcount -= 1
                if fcount == 0 :
                    break
                else :
                    if c > target - found :
                        median += val
                        break
                    else :
                        target += 1
                        found += c
        median /= 1 if total & 1 else 2

        return minimum, maximum, mean, median, mode