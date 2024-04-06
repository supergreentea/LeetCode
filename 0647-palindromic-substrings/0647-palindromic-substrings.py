class Solution:
    def countSubstrings(self, s: str) -> int:
        
        @cache
        def isPalindrome(start: int, end: int) -> bool:
            if start == end or (end == start + 1 and s[start] == s[end]):
                return True
            return s[start] == s[end] and isPalindrome(start + 1, end - 1)
        
        N = len(s)
        count = 0
        for start in range(N):
            for end in range(start, N):
                if isPalindrome(start, end):
                    count += 1
        return count