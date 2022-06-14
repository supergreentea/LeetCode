"""
Maintain a max heap for the most frequent letter
Try to use 2 of the most frequent letter at a time
If most frequent letter was used previously, use 1 of the next most frequent letter
This is to maximize opportunitites to use the most frequent letter. If we use 2 of the next most frequent letter,
we may end up in a situation where we've exhausted all of the less frequent letters before we were able to use up the most frequent character.
"""

class CharFreq:
    
    def __init__(self, char, freq):
        self.char, self.freq = char, freq
    
    def __lt__(self, other):
        return self.freq > other.freq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for char, freq in [("a", a), ("b", b), ("c", c)]:
            if freq > 0:
                heap.append(CharFreq(char, freq))
        heapq.heapify(heap)
        res = ""
        while heap:
            most_freq = heapq.heappop(heap)
            if len(res) > 0 and res[-1] == most_freq.char:
                if not heap:
                    return res
                next_most_freq = heapq.heappop(heap)
                res += next_most_freq.char
                next_most_freq.freq -= 1
                if next_most_freq.freq > 0:
                    heapq.heappush(heap, next_most_freq)
                heapq.heappush(heap, most_freq)
            else:
                num_to_use = 1 if most_freq.freq < 2 else 2
                res += num_to_use * most_freq.char
                most_freq.freq -= num_to_use
                if most_freq.freq > 0:
                    heapq.heappush(heap, most_freq)
        return res
        
        
        
            
