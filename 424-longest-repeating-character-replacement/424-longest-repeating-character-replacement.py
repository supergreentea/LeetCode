class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of most frequent char in substring
        # replacements needed = substring length - most frequent char in substring
        # if replacements needed exceed k, move pointers for substring
        
        freq = defaultdict(int)
        l = longest = most_frequent_char = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            most_frequent_char = max(most_frequent_char, freq[s[r]])
            while r - l + 1 - most_frequent_char > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest