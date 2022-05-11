class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        longest = 0
        i = 0
        for j in range(len(s)):
            while s[j] in Set:
                Set.remove(s[i])
                i += 1
            Set.add(s[j])
            length = j - i + 1
            longest = max(longest, length)
        return longest