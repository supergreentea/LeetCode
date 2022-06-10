class Solution:
    def minDeletions(self, s: str) -> int:
        
        frequencies = [0] * 26
        
        for c in s:
            frequencies[ord(c) - ord('a')] += 1
        
        frequencies.sort(reverse = True)
        
        max_allowed_frequency = len(s)
        
        deletions_count = 0
        
        for freq in frequencies:
            if freq > max_allowed_frequency:
                deletions_count += freq - max_allowed_frequency
                freq = max_allowed_frequency
            max_allowed_frequency = max(0, freq - 1)
        
        return deletions_count