class Freq:
    
    def __init__(self, char, count):
        self.char, self.count = char, count
        
    def __lt__(self, other):
        return self.count > other.count

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        heapq.heapify(heap)
        if a > 0:
            heapq.heappush(heap, Freq("a", a))
        if b > 0:
            heapq.heappush(heap, Freq("b", b))
        if c > 0:
            heapq.heappush(heap, Freq("c", c))
        
        res = ""
        
        while heap:
            cur = heapq.heappop(heap)
            if len(res) > 0 and res[-1] == cur.char: 
                if not heap:
                    return res
                t = cur
                cur = heapq.heappop(heap) # pop 2nd most frequent
                res += cur.char
                cur.count -= 1
                if cur.count > 0:
                    heapq.heappush(heap, cur)
                heapq.heappush(heap, t)
            else:
                if cur.count >= 2:
                    res += cur.char * 2
                    cur.count -= 2
                else:
                    res += cur.char
                    cur.count -= 1
                if cur.count > 0:
                    heapq.heappush(heap, cur)
        
        return res
                
        