class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        
        for i in range(len(rating)):
            left_less, left_greater, right_less, right_greater = 0, 0, 0, 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    left_less += 1
                else:
                    left_greater += 1
            for j in range(i + 1, len(rating)):
                if rating[j] < rating[i]:
                    right_less += 1
                else:
                    right_greater += 1
            teams += left_less * right_greater + left_greater * right_less
        
        return teams