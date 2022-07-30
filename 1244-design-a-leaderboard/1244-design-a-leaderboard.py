from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sorted_scores = SortedDict()
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sorted_scores[-score] = self.sorted_scores.get(-score, 0) + 1
        else:
            old_score = self.scores[playerId]
            new_score = old_score + score
            self.scores[playerId] = new_score
            
            self.sorted_scores[-old_score] -= 1
            if self.sorted_scores[-old_score] == 0:
                del self.sorted_scores[-old_score]
            
            self.sorted_scores[-new_score] = self.sorted_scores.get(-new_score, 0) + 1

    def top(self, K: int) -> int:
        count = total = 0
        for score, score_count in self.sorted_scores.items():
            for _ in range(score_count):
                total += -score
                count += 1
                if count == K:
                    break
            if count == K:
                break
        return total
        

    def reset(self, playerId: int) -> None:
        score = self.scores[playerId]
        del self.scores[playerId]
        
        self.sorted_scores[-score] -= 1
        if self.sorted_scores[-score] == 0:
            del self.sorted_scores[-score]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)