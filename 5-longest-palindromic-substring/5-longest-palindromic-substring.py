class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, longest = "", 0
        for i in range(len(s)):
            
            # odd palindrome case
            l, r = i, i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > longest:
                    res = s[l : r + 1]
                    longest = length
                l -= 1
                r += 1
            
            # odd palindrome case
            l, r = i , i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > longest:
                    res = s[l : r + 1]
                    longest = length
                l -= 1
                r += 1
        return res