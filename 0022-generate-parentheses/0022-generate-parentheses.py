class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def backtrack(combination: List[int], left: int, right: int):
            if len(combination) == 2 * n:
                answer.append("".join(combination))
                return
            if left < n:
                combination.append("(")
                backtrack(combination, left + 1, right)
                combination.pop()
            if right < left:
                combination.append(")")
                backtrack(combination, left, right + 1)
                combination.pop()
        
        backtrack([], 0, 0)
        return answer