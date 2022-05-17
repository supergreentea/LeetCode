class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        l, longest = 0, 0
        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l += 1
            Set.add(s[r])
            longest = max(longest, r - l + 1)
        return longest