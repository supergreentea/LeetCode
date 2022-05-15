class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # strategy: sliding window. number of replacements needed = length of window - most frequent character count in that window
        # we can update the most frequent character count
        
        maxf = 0
        l = 0
        count = defaultdict(int)
        longest = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest