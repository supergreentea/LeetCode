class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        last_seen_word1, last_seen_word2 = -1, -1
        shortest_dist = math.inf
        
        for index, word in enumerate(wordsDict):
            if word == word1:
                if last_seen_word2 != -1:
                    shortest_dist = min(shortest_dist, index - last_seen_word2)
                last_seen_word1 = index
            elif word == word2:
                if last_seen_word1 != -1:
                    shortest_dist = min(shortest_dist, index - last_seen_word1)
                last_seen_word2 = index
        
        return shortest_dist
                