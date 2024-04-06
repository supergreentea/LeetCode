class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def expand(left: int, right: int) -> None:
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return count