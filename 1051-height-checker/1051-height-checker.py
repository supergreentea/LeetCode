class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy = heights.copy()
        counts = [0] * 101
        for height in heights:
            counts[height] += 1
        i = 0
        for j in range(101):
            while counts[j] > 0:
                copy[i] = j
                i += 1
                counts[j] -= 1
        ans = 0
        for i in range(len(heights)):
            if copy[i] != heights[i]:
                ans += 1
        return ans
        