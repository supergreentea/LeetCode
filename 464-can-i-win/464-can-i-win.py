class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        memo = {}
        used = ['0'] * (maxChoosableInteger + 1)
        if desiredTotal > sum(range(1, maxChoosableInteger + 1)):
            return False
        
        def backtrack(desiredTotal):
            memo_string = ''.join(used)
            if memo_string in memo:
                return memo[memo_string]
            if desiredTotal <= maxChoosableInteger:
                for option in range(1, maxChoosableInteger + 1):
                    if option >= desiredTotal and used[option] == '0':
                        return True
            
            for option in range(1, maxChoosableInteger + 1):
                if used[option] == '0':
                    used[option] = '1'
                    if not backtrack(desiredTotal - option):
                        memo[memo_string] = True
                        used[option] = '0'
                        return True
                    used[option] = '0'
            
            memo[memo_string] = False
            return False

        return backtrack(desiredTotal)