class Leaderboard:

    def __init__(self):
        self.player_scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.player_scores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for score in self.player_scores.values():
            heappush(heap, score)
            if len(heap) > K:
                heappop(heap)
        score_sum = 0
        while heap:
            score_sum += heappop(heap)
        return score_sum

    def reset(self, playerId: int) -> None:
        self.player_scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)