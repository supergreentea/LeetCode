class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def expandAroundCenter(centerA: int, centerB: int) -> None:
            nonlocal count
            while centerA >= 0 and centerB < len(s) and s[centerA] == s[centerB]:
                count += 1
                centerA -= 1
                centerB += 1
        
        for i in range(len(s)):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i + 1)
        
        return count
                