class Freq:
    
    def __init__(self, char, count):
        self.char, self.count = char, count
        
    def __lt__(self, other):
        return other.count < self.count

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        heapq.heapify(max_heap)
        if a > 0:
            heapq.heappush(max_heap, Freq("a", a))
        if b > 0:
            heapq.heappush(max_heap, Freq("b", b))
        if c > 0:
            heapq.heappush(max_heap, Freq("c", c))
        
        output = ""
        while max_heap:
            c = heapq.heappop(max_heap)
            if len(output) > 1 and c.char == output[-1]:
                if len(max_heap) == 0:
                    return output
                next_c = heapq.heappop(max_heap)
                output += next_c.char
                next_c.count -= 1
                if next_c.count > 0:
                    heapq.heappush(max_heap, next_c)
                heapq.heappush(max_heap, c)
            else:
                if c.count >= 2:
                    output += c.char * 2
                    c.count -= 2
                else:
                    output += c.char
                    c.count -= 1
                if c.count > 0:
                    heapq.heappush(max_heap, c)
        return output