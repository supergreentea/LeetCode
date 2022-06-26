class Word:

    def __init__(self, word, freq):
        self.word, self.freq = word, freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word

class Solution:
            
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        heap = []
        counter = collections.Counter(words)
        for word, count in counter.items():
            heapq.heappush(heap, Word(word, count))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        
        return res[::-1]
        
    
    