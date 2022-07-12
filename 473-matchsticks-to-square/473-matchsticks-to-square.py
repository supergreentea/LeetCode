class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        num_sticks = len(matchsticks)
        counter = Counter(matchsticks)
        sticks_used = 0
        stick_total = sum(matchsticks)
        if stick_total % 4 != 0:
            return False
        target_length = stick_total // 4
        memo = {}
        
        def backtrack(target_length, partial_side, formed, required):
            nonlocal sticks_used
            memo_key = str(dict(counter))
            if memo_key in memo:
                return memo[memo_key]
            if formed == required and sticks_used == num_sticks:
                return True
            if partial_side == target_length:
                return backtrack(target_length, 0, formed + 1, required)
            for length, count in counter.items():
                if length <= target_length - partial_side and counter[length] > 0:
                    # use the stick
                    counter[length] -= 1
                    sticks_used += 1
                    if backtrack(target_length, partial_side + length, formed, required):
                        return True
                    counter[length] += 1
                    sticks_used -= 1
            memo[memo_key] = False
            return False
        
        return backtrack(target_length, 0, 0, 4)
        
        
        
                    
            
            
            