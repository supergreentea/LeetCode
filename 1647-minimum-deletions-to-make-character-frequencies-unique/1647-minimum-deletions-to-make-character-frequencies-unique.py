class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - ord('a')] += 1
        freqs.sort(reverse = True)
        max_allowed = len(s)
        
        for freq in freqs:
            if freq > max_allowed:
                deletions += freq - max_allowed
                freq = max_allowed
            
            max_allowed = max(0, freq - 1)
                
        return deletions