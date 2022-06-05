class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            m = (l + r) // 2
            h_spent = 0
            for pile in piles:
                h_spent += math.ceil(pile / m)
            
            if h_spent <= h:
                r = m
            else:
                l = m + 1
        return r