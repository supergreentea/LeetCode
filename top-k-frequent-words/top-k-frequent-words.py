class Word:
    
    def __init__(self, word, frequency):
        self.word, self.frequency = word, frequency
    
    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.word > other.word
        return self.frequency < other.frequency

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        min_heap = []
        counter = Counter(words)
        heapq.heapify(min_heap)
        for word, count in counter.items():
            heapq.heappush(min_heap, Word(word, count))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        ans = []
        while len(min_heap) > 0:
            ans.append(heapq.heappop(min_heap).word)
        return ans[::-1]