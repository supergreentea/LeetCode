class Solution:
    def reverseWords(self, s: str) -> str:
        res = deque([])
        
        word = []
        for c in s:
            if c == " ":
                if len(word) > 0:
                    res.appendleft("".join(word))
                    word = []
                else:
                    continue
            else:
                word.append(c)
        if word:
            res.appendleft("".join(word))
        
        return " ".join(res)