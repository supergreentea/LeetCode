class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        def count(n):
            return (n * (n + 1)) // 2
        
        if len(ratings) <= 1:
            return len(ratings)
        
        candies = up = down = old_slope = 0
        
        for i in range(1, len(ratings)):
            new_slope = 0
            if ratings[i] > ratings[i - 1]:
                new_slope = 1
            if ratings[i] < ratings[i - 1]:
                new_slope = -1
            
            if (old_slope > 0 and new_slope == 0) or (old_slope < 0 and new_slope >= 0):
                candies += count(up) + count(down) + max(up, down)
                up = 0
                down = 0
            
            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1
            else:
                candies += 1
            
            old_slope = new_slope
        
        candies += count(up) + count(down) + max(up, down) + 1
        return candies
            