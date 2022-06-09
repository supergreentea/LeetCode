class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        curr = 0
        while curr < len(height):
            while len(stack) > 0 and height[curr] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = curr - stack[-1] - 1
                bounded_height = min(height[curr], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(curr)
            curr += 1
        return ans
                