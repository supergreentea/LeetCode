class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        max_left = [0] * n
        
        max_right = [0] * n
        
        max_left[0], max_right[n - 1] = height[0], height[n - 1]
        
        total = 0
        
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])
        
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
        
        for i in range(1, n - 1):
            if height[i] < max_left[i] and height[i] < max_right[i]:
                total += min(max_left[i], max_right[i]) - height[i]
        
        return total