class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def backtrack(index = 0):
            if index == len(s):
                return True
            for i in range(index, len(s)):
                if i + 1 <= len(s) and s[index : i + 1] in wordDict:
                    if backtrack(i + 1):
                        return True
            return False
        
        return backtrack()