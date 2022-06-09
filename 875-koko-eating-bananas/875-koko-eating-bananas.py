class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eating_time(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours
        
        l, r = 1, max(piles)
        
        while l < r:
            m = (l + r) // 2
            hours = eating_time(m)
            
            if hours <= h:
                r = m 
            else:
                l = m + 1
        
        return l