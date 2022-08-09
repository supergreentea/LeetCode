class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        
        @lru_cache
        def dfs(start = 0):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start : end] in wordSet and dfs(end):
                    return True
            return False
        
        return dfs()
            