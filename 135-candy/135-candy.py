class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = 0
        
        left_to_right = [1] * len(ratings)
        right_to_left = [1] * len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left_to_right[i] = left_to_right[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_to_left[i] = right_to_left[i + 1] + 1
        
        for i in range(len(ratings)):
            candies += max(left_to_right[i], right_to_left[i])
        
        return candies