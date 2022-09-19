class TrieNode:
    
    def __init__(self):
        self.is_word = False
        self.children = {}
        self.score = 0
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        def add_word(word):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
                cur.score += 1
        
        def get_score(word):
            score = 0
            cur = root
            for c in word:
                cur = cur.children[c]
                score += cur.score
            return score
        
        for word in words:
            add_word(word)
        
        return [get_score(word) for word in words]