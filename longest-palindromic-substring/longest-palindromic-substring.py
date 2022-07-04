class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_start = ans_end = 0
        
        def expand_around_center(i, j):
            nonlocal ans_start
            nonlocal ans_end
            left, right = i, j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > ans_end - ans_start:
                    ans_start, ans_end = left, right
                left -= 1
                right += 1
        
        for i in range(len(s)):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)
        
        return s[ans_start : ans_end + 1]
        
        