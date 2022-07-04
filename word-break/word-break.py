class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def word_break(s):
            if s == "":
                return True
            for word in wordDict:
                word_start = s.find(word)
                if word_start != -1:
                    left_half = s[:word_start]
                    right_half = s[word_start + len(word):]
                    if word_break(left_half) and word_break(right_half):
                        return True
            return False
        
        return word_break(s)