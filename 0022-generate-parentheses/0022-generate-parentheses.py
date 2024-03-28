class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #time: 2^N
        #space: 2^N
        ans = []
        
        def backtrack(combination: List[str] = [], left: int = 0, right: int = 0) -> None:
            if len(combination) == 2 * n:
                ans.append("".join(combination[:]))
                return
            if left < n:
                combination.append("(")
                backtrack(combination, left + 1, right)
                combination.pop()
            if left > right:
                combination.append(")")
                backtrack(combination, left, right + 1)
                combination.pop()
        
        backtrack()
        return ans