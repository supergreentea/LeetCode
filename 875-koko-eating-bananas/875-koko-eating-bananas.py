class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        
        while low < high:
            eating_speed = (low + high) // 2
            
            eating_time = sum(math.ceil(pile / eating_speed) for pile in piles)
            
            if eating_time <= h:
                high = eating_speed
            else:
                low = eating_speed + 1
        
        return high