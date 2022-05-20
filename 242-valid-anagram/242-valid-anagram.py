class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = [0] * 26
        
        def charToIndex(c):
            return ord(c) - ord('a')
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            charCount[charToIndex(s[i])] += 1
            charCount[charToIndex(t[i])] -= 1
        
        for count in charCount:
            if count != 0:
                return False
        
        return True