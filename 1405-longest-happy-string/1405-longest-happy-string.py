class Freq:
    def __init__(self, char, count):
        self.char = char
        self.count = count
        
    def __lt__(self, other):
        return self.count > other.count
    
    def __repr__(self):
        return f'[Char: {self.char}, Count: {self.count}]'

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freqs = [Freq("a", a), Freq("b", b), Freq("c", c)]
        heap = list(filter(lambda x : x.count > 0, freqs))

        heapq.heapify(heap)
        res = ""
        while heap:
            print(heap)
            print(res)
            prev = cur = heapq.heappop(heap)
            
            if len(res) >= 1 and res[-1] == cur.char:
                if not heap: # last element in heap forces us to break condition
                    return res
                cur = heapq.heappop(heap) # get another element
                heapq.heappush(heap, prev) # push prev element back to heap
                
            t = min(cur.count, 2) if prev == cur else 1 # always choose 1 if less frequent char is used
            res += t * cur.char
            cur.count = cur.count - t
            if cur.count > 0:
                heapq.heappush(heap, cur)
                        
        return res