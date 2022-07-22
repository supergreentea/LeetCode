class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        min_heap = []
        for score in self.scores.values():
            heappush(min_heap, score)
            if len(min_heap) > K:
                heappop(min_heap)
        top_k_sum = 0
        while min_heap:
            top_k_sum += heappop(min_heap)
        return top_k_sum

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)