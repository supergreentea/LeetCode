class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of most frequent char in substring
        # replacements needed = substring length - most frequent char in substring
        # if replacements needed exceed k, move pointers for substring
        
        freq = defaultdict(int)
        l = longest = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest