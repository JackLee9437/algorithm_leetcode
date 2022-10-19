from collections import defaultdict

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        numbers = defaultdict(int)
        for n in arr :
            numbers[n] += 1
        
        combination = [
            None,
            lambda x : x,
            lambda x : x * (x-1) // 2,
            lambda x : x * (x-1) * (x-2) // 6
        ]
        
        answer = 0
        keys = sorted(numbers.keys())
        for l in range(len(keys)) :
            for m in range(l, len(keys)) :
                rval = target-keys[l]-keys[m]
                if rval < keys[m] :
                    break
                if rval in numbers :
                    vals = defaultdict(int)
                    vals[keys[l]] += 1
                    vals[keys[m]] += 1
                    vals[rval] += 1
                    cnt = 1
                    for key, val in vals.items() :
                        if numbers[key] < val :
                            cnt = 0
                            break
                        cnt *= combination[val](numbers[key])
                    # print(f"({keys[l]}, {keys[m]}, {rval})", cnt)
                    answer += cnt
                         
        return answer % MOD