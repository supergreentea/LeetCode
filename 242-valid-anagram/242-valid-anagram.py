class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = [0] * 26
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            charCount[ord(s[i]) - ord('a')] += 1
            charCount[ord(t[i]) - ord('a')] -= 1
        
        for n in charCount:
            if n != 0:
                return False
        
        return True