class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        cur_power = max_power = 1
        prev_char = s[0]
        
        for i in range(1, len(s)):
            cur_char = s[i]
            if cur_char == prev_char:
                cur_power += 1
                max_power = max(max_power, cur_power)
            else:
                prev_char = cur_char
                cur_power = 1
        
        return max_power