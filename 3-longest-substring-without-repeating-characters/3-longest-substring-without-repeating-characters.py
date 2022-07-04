class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            c = s[r]
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            longest = max(longest, r - l + 1)
        return longest
            