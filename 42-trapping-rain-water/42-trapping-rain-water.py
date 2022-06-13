class Solution:
    def trap(self, height: List[int]) -> int:
        # water trapped at position = min(max from left, max from right) - current height
        ans = 0
        n = len(height)
        max_l, max_r = height[0], height[n - 1]
        l, r = 0, n - 1
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    ans += max_l - height[l]
                l += 1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    ans += max_r - height[r]
                r -= 1
        return ans
                
        