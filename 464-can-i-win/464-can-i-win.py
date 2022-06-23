class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        sum_of_all_moves = ((maxChoosableInteger + 1) * maxChoosableInteger) / 2
        if sum_of_all_moves < desiredTotal:
            return False
        
        used = ['0'] * (maxChoosableInteger + 1)
        memo = {}
        
        def backtrack(desiredTotal):
            memo_string = ''.join(used)
            if memo_string in memo:
                return memo[memo_string]
            if desiredTotal <= maxChoosableInteger:
                for move in range(1, maxChoosableInteger + 1):
                    if used[move] == '0' and move >= desiredTotal:
                        return True
            
            for move in range(1, maxChoosableInteger + 1):
                if used[move] == '0':
                    used[move] = '1'
                    if not backtrack(desiredTotal - move):
                        memo[memo_string] = True
                        used[move] = '0'
                        return True
                    used[move] = '0'
            
            memo[memo_string] = False
            return False
        
        return backtrack(desiredTotal)