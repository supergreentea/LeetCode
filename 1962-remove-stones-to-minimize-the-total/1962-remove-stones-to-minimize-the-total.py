class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        
        for pile in piles:
            heapq.heappush(heap, -1 * pile)
        
        for _ in range(k):
            pile = heapq.heappop(heap)
            pile = math.floor(pile / 2)
            heapq.heappush(heap, pile)
        
        return - 1* sum(heap)