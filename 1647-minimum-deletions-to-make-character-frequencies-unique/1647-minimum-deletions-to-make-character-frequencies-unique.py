class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = [0] * 26
        for c in s:
            frequencies[ord(c) - ord('a')] += 1
        
        frequencies.sort(reverse = True)
        
        deletions_count = 0
        
        max_allowed = math.inf
        
        for freq in frequencies:
            if freq > max_allowed:
                deletions_count += freq - max_allowed
                freq = max_allowed
            max_allowed = max(0, freq - 1)
        
        return deletions_count
        
        