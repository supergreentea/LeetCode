class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # replacements needed in a substring = length substring - most frequent char in substring
        max_length = 1
        i = 0
        n = len(s)
        char_freq = defaultdict(int)
        for j in range(n):
            c = s[j]
            char_freq[c] += 1
            replacements = j - i + 1 - max(char_freq.values())
            while replacements > k:
                char_freq[s[i]] -= 1
                i += 1
                replacements = j - i + 1 - max(char_freq.values())
            max_length = max(max_length, j - i + 1)
        return max_length
                
        