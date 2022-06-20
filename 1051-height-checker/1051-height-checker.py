class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy = heights.copy()
        
        counts = [0] * 101
        
        for height in heights:
            counts[height] += 1
        
        num_previous_items = 0
        for i in range(101):
            count = counts[i]
            counts[i] = num_previous_items
            num_previous_items += count
        
        for height in heights:
            copy[counts[height]] = height
            counts[height] += 1
        
        ans = 0
        
        for i in range(len(heights)):
            if heights[i] != copy[i]:
                ans += 1
        
        return ans