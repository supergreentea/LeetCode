class Solution:
    def reverseWords(self, s: str) -> str:
        res = deque([])
        
        word = ""
        for c in s:
            if c == " ":
                if len(word) > 0:
                    res.appendleft(word)
                    word = ""
                else:
                    continue
            else:
                word += c
        if word:
            res.appendleft(word)
        
        return " ".join(res)