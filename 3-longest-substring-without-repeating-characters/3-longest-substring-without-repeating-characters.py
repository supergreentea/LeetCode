class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in Set:
                Set.remove(s[l])
                l += 1
            length = r - l + 1
            maxLength = max(length, maxLength)
            Set.add(s[r])
        return maxLength
                