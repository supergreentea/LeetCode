class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        right[n-1] = height[n-1]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        res = 0
        for i in range(1, n-1):
            if height[i] < left[i] and height[i] < right[i]:
                res += min(left[i], right[i]) - height[i]
        return res