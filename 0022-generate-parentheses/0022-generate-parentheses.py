class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        def backtrack(cur: [], leftCount: int, rightCount: int):
            if len(cur) ==  2 * n:
                answer.append("".join(cur))
                return
            if leftCount < n:
                cur.append("(")
                backtrack(cur, leftCount + 1, rightCount)
                cur.pop()
            if rightCount < leftCount:
                cur.append(")")
                backtrack(cur, leftCount, rightCount + 1)
                cur.pop()
        
        backtrack([], 0, 0)
        return answer