class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        def should_skip(index):
            return not s[index].isalnum()
        
        while l < r:
            if should_skip(l):
                l += 1
            elif should_skip(r):
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        
        return True
                