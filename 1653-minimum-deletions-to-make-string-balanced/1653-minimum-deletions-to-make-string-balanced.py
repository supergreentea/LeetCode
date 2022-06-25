class Solution:
    def minimumDeletions(self, s: str) -> int:
        counter = Counter(s)
        a_left = b_left = 0
        a_right, b_right = counter["a"], counter["b"]
        
        best = a_right
        
        for c in s:
            best = min(best, b_left + a_right)
            if c == "a":
                a_left += 1
                a_right -= 1
            else:
                b_left += 1
                b_right -= 1
        
        best = min(best, b_left + a_right)
        
        return best