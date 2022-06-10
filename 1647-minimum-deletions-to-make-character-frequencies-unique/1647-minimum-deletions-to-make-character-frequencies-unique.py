class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = [0] * 26
        for c in s:
            frequencies[ord(c) - ord('a')] += 1
        
        frequencies.sort(reverse = True)
        
        upper_bound = len(s)
        deletions = 0
        
        for n in frequencies:
            if n > upper_bound:
                deletions += n - upper_bound
                n = upper_bound
            upper_bound = max(n - 1, 0)
        
        return deletions