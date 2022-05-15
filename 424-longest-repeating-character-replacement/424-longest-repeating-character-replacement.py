class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        Dict = defaultdict(int)
        maxf = 1
        l = 0
        for r in range(len(s)):
            c = s[r]
            Dict[c] += 1
            maxf = max(maxf, Dict[c])
            while r - l + 1 - maxf > k:
                Dict[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen