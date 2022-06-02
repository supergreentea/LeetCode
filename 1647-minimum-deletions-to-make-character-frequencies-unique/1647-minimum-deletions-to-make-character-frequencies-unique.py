class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord('a')] += 1    
            
        frequency.sort(reverse=True)
        
        max_allowed_freq = len(s)
        for freq in frequency:
            
            if freq > max_allowed_freq:
                deletions += freq - max_allowed_freq
                freq = max_allowed_freq
            
            max_allowed_freq = max(0, freq - 1)
        
        return deletions