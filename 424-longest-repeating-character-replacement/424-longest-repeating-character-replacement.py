class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = maxf = l = 0
        Dict = defaultdict(int)
        for r in range(len(s)):
            Dict[s[r]] += 1
            maxf = max(maxf, Dict[s[r]])
            while r - l + 1 - maxf > k:
                Dict[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen