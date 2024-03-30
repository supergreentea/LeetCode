class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        N = len(possible)
        for i in range(N):
            if possible[i] == 0:
                possible[i] = -1
        
        total = sum(possible)
        prefix = [0] * N
        prefix[0] = possible[0]
        minLength = N
        if prefix[0] > total - prefix[0]:
            return 1    
        
        for i in range(1, N):
            prefix[i] = prefix[i - 1] + possible[i]
            if prefix[i] > total - prefix[i]:
                minLength = min(minLength, i + 1)
        
        return minLength if minLength != N else -1