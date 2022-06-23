class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-1 * pile for pile in piles]
        heapq.heapify(heap)
        for _ in range(k):
            pile = heapq.heappop(heap) # -5 // 2 = -3
            heapq.heappush(heap, pile // 2)
        return -1 * sum(heap)