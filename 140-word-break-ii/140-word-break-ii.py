class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []
        
        def backtrack(start = 0, sentence = []):
            if start == len(s):
                output.append(" ".join(sentence))
                return
            
            for word in wordDict:
                if start + len(word) <= len(s) and s[start : start + len(word)] == word:
                    sentence.append(word)
                    backtrack(start + len(word), sentence)
                    sentence.pop()
        
        backtrack()
        return output