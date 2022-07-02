class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_horizontal_diff = max(horizontalCuts[0], h - horizontalCuts[-1])
        
        max_vertical_diff = max(verticalCuts[0], w - verticalCuts[-1])
        
        for i in range(1, len(horizontalCuts)):
            max_horizontal_diff = max(max_horizontal_diff, horizontalCuts[i] - horizontalCuts[i - 1])    
            
        for i in range(1, len(verticalCuts)):
            max_vertical_diff = max(max_vertical_diff, verticalCuts[i] - verticalCuts[i - 1])
        
        return (max_horizontal_diff * max_vertical_diff) % (10 ** 9 + 7)