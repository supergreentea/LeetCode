class Solution:
    def countSubstrings(self, s: str) -> int:
        # time: O(N ^ 2)
        # space: O(1)
        
        count = 0
        
        def expandAroundCenter(left: int, right: int) -> None:
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left, right = left - 1, right + 1
        
        for i in range(len(s)):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i + 1)
        
        return count